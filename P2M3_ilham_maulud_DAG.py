import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.models import Variable
from elasticsearch import Elasticsearch, helpers

default_args= {
    'owner': 'Ilham_Maulud',
    'start_date': datetime(2024, 11, 1)
}

with DAG(
    dag_id = 'P2M3_ilham_maulud_DAG',
    description='ETL Pipeline: Postgres >> Transform >> Elasticsearch',
    schedule_interval='10,20,30 9 * * 6', # Setiap hari sabtu, jam 09.10 AM - 09.30 AM, dilakukan per 10 menit 
    default_args=default_args, 
    catchup=False) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task()
    def extract():
        ''' 
        Fungsi ini bertujuan untuk extract data dari posgres (tabel_m3) dan save kedalam
        bentuk raw CSV
        '''

        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}:5432/{database}"

        engine = create_engine(postgres_url)

        df = pd.read_sql('select * from table_m3', engine)

        raw_path ='/tmp/P2M3_ilham_maulud_data_raw.csv'
        df.to_csv(raw_path, index=False)

        print(f"[EXTRACT] save raw CSV:  {raw_path}")
        return raw_path

    @task()
    def preprocess_data(raw_path: str) -> str: #Fungsi -> str digunakan untuk mengembalikan string
        '''
        Pada proses preprocess_data, fungsi ini akan melakukan transformasi dan pembersihan dari data 
        file mentah yang kita punya.

        untuk parameter adalah : raw_path(str): Path/lokasi file CVS mentah dari proses extract

        untuk proses transformasi :
        1. normalisasi nama kolom
        2. mengkonversi text ke lowercase, stripping whitespace dan penghapusan simbol
        3. mengubah format kolom yang tidak sesuai 
        4. handling missing value dan drop duplicate
        5. menambahkan kolom total
        '''
        
        df = pd.read_csv(raw_path)

        # 1. Normalisasi nama kolom
        df.columns = (
            df.columns.str.strip() # Hapus spasi di awal dan di akhir
            .str.lower() # Lowercase
            .str.replace(' ', '_') # Mengganti spasi dengan underscore
            .str.replace(r'[^0-9a-zA-z_]', '', regex=True) # Hapus simbol
        )

        # 2. Mengkonversi text ke lowercasem stripping whitespace dan penghapusan simbol yang tidak perlu
        df['invoice_id'] = df['invoice_id'].str.replace(r'\D', '', regex=True)

        # 3. Mengubah format kolom yang tidak sesuai
        df['date'] = pd.to_datetime(df['date'], errors='coerce') # Mengubah format menjadi datetime64[ns]
        df['time'] = pd.to_datetime(df['time'], errors='coerce').dt.time # Mengubah format menjadi time
        df['invoice_id'] = df['invoice_id'].astype(int)
        df['quantity'] = df['quantity'].astype('int64')

        # 4. Handilng missing value dan drop duplicate
        # kolom objek
        for col in df.select_dtypes(include='object'):
            df[col].fillna('Unknown', inplace=True)
        
        # Kolom numerik
        for col in df.select_dtypes(include='number'):
            df[col].fillna(df[col].mean(), inplace=True)
        
        # Hapus duplikat
        df.drop_duplicates(inplace=True)

        # 5. menambah kolom total
        df['total'] = df['unit_price'] * df['quantity'] + df['tax_5']


        clean_data = '/tmp/P2M3_ilham_maulud_data_clean.csv'
        df.to_csv(clean_data, index=False)
        print("Preprocessed data berhasil")
        return clean_data

    @task()
    def load(clean_data: str):
        '''
        Fungsi ini memuat data kedalam Elasticsearch dengan konfigurasi yang optimal.

        untuk parameter adalah : clean_data(str): Path/lokasi file CVS clean dari proses preprocess

        untuk proses load data :
        1. membuat koneksi kedalam Elasticsearch
        2. membaca file 
        3. mendefinisikan mapping struktur index
        4. melakukan bulk insert data
        '''

        # 1. Membuat koneksi kedalam Elasticsearch
        es = Elasticsearch(hosts=["http://elasticsearch:9200"]
                           , timeout = 30 # Timeout 30 detik
                           , max_retries = 3 # Maksimal percobaan 3 kali
                           , retry_on_timeout = True # Retry jika timeout
                           )
        
        if not es.ping():
            raise ValueError('Elasticsearch gagal terhubung!')
        
        # 2. Membaca file clean csv
        df = pd.read_csv(clean_data)

        # 3. Mendefinisikan mapping index
        index_name ='supermarket_sales_data_index'
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name)

        # 4. Bulk insert data
        actions = [
            {
                '_index': index_name,
                '_source': row.to_dict()
            }
            for _, row in df.iterrows()
        ]

        helpers.bulk(es, actions)

    # Membentuk dependency antar task
    raw_data = extract()
    clean_data = preprocess_data(raw_data)
    load_data = load(clean_data)

    start >> raw_data >> clean_data >> load_data >> end