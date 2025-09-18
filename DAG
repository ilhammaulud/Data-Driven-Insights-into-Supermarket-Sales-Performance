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
    schedule_interval='10,20,30 9 * * 6', # Every Saturday, from 09:10 AM to 09:30 AM, it is done every 10 minutes
    default_args=default_args, 
    catchup=False) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task()
    def extract():
        ''' 
        This function aims to extract data from PostgreSQL (table_m3) and save it in raw CSV format.
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
    def preprocess_data(raw_path: str) -> str: # Function -> str is used to return a string
        '''
        In the preprocess_data process, this function performs transformations and cleaning on the raw data file.
        For the parameters, they are: raw_path (str): The path/location of the raw CVS file from the extraction process.
        For the transformation process: 
        1. Column name normalization 
        2. Converting text to lowercase, stripping whitespace, and removing symbols 
        3. Changing inconsistent column formats 
        4. Handling missing values and dropping duplicates 
        5. Adding a total column
        '''
        
        df = pd.read_csv(raw_path)

        df.columns = (
            df.columns.str.strip() 
            .str.lower()
            .str.replace(' ', '_') 
            .str.replace(r'[^0-9a-zA-z_]', '', regex=True)
        )

        # Converting text to lowercase, stripping whitespace, and removing unnecessary symbols.
        df['invoice_id'] = df['invoice_id'].str.replace(r'\D', '', regex=True)

        # Changing the format of columns that are not appropriate
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['time'] = pd.to_datetime(df['time'], errors='coerce').dt.time
        df['invoice_id'] = df['invoice_id'].astype(int)
        df['quantity'] = df['quantity'].astype('int64')

        # Handling missing values and drop duplicates
        for col in df.select_dtypes(include='object'):
            df[col].fillna('Unknown', inplace=True)
            
        for col in df.select_dtypes(include='number'):
            df[col].fillna(df[col].mean(), inplace=True)
        
        df.drop_duplicates(inplace=True)

        # add a total column
        df['total'] = df['unit_price'] * df['quantity'] + df['tax_5']

        clean_data = '/tmp/P2M3_ilham_maulud_data_clean.csv'
        df.to_csv(clean_data, index=False)
        print("Preprocessed data berhasil")
        return clean_data

    @task()
    def load(clean_data: str):
        '''
        This function loads data into Elasticsearch with optimal configuration.
        For the parameters, they are: clean_data(str): Path/location of the clean CVS file from the preprocessing step.
        For the data loading process: 
        1. Establish a connection to Elasticsearch. 
        2. Read the file. 
        3. Define the index structure mapping. 
        4. Perform a bulk insert of the data.
        '''

        # 1. Making a connection to Elasticsearch
        es = Elasticsearch(hosts=["http://elasticsearch:9200"]
                           , timeout = 30 # Timeout 30 second
                           , max_retries = 3 # Maximum 3 attempts
                           , retry_on_timeout = True # Retry if timeout
                           )
        
        if not es.ping():
            raise ValueError('Elasticsearch gagal terhubung!')
        
        # 2. Reading the clean CSV file
        df = pd.read_csv(clean_data)

        # 3. Defining index mapping
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

    # Creating dependencies between tasks
    raw_data = extract()
    clean_data = preprocess_data(raw_data)
    load_data = load(clean_data)


    start >> raw_data >> clean_data >> load_data >> end
