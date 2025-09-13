# Data-Driven Insights into Supermarket Sales Performance

## Repository Outline

```
1. README.md - General overview of the project
2. P2M3_ilham_maulud_GX.ipynb - Notebook containing the data quality validation framework
3. P2M3_ilham_maulud_ddl.txt - Set of SQL commands used to define the database structure
4. P2M3_ilham_maulud_DAG_graph.jpg - Data processing workflow diagram
5. P2M3_ilham_maulud_conceptual.txt - Answers to conceptual questions
6. P2M3_ilham_maulud_DAG.py - Workflow containing sequential tasks to be executed
7. P2M3_ilham_maulud_data_raw.csv - Raw dataset
8. P2M3_ilham_maulud_data_clean.csv - Cleaned dataset
9. Image folder - Contains introduction, visualizations, and conclusions
```

## Problem Background
The modern retail landscape is becoming increasingly competitive, particularly in the supermarket sector. Sales performance is influenced by multiple factors such as branch location, product type, customer preferences, and promotional strategies. Sales data analysis can help businesses understand consumer behavior, identify best-selling and underperforming products, and optimize future sales strategies.

The “Supermarket Sales” dataset contains transaction records from multiple supermarket branches, including details on products, categories, quantities, prices, discounts, and timestamps. This dataset serves as a solid foundation for comprehensive data exploration and sales analysis.


## Project Output

1. Data Pipeline (Airflow DAG)

- Automated workflow for reading, cleaning, transforming, and validating supermarket data using Great Expectations (GX).
- Ensures data consistency, validity, and compliance with business standards.

2. Data Validation Report

- Data quality verification with Great Expectations.
- Validation includes uniqueness, value ranges, data types, and statistical distributions.
- Results determine whether the dataset is suitable for further analysis.

3. Dashboard (Kibana)

- Interactive visualization of supermarket sales covering product distribution, sales trends, customer segmentation, payment methods, and branch performance.
- Provides actionable business insights for marketing, sales, and management teams.

4. Business Insights & Recommendations

- Narrative analysis from EDA and dashboards.
- Insights focus on sales trends, customer behavior, and promotional strategies to improve profitability.

## Data
The dataset originates from the publicly available Supermarket Sales Dataset on Kaggle, which contains transaction records from multiple branches across three major cities.

Data Characteristics:
- Rows: 1,000 transactions
- Columns: 17 attributes
- No missing values
- Mix of categorical and numerical data types

## Method
This project employs Exploratory Data Analysis (EDA) and Data Validation to identify sales patterns and ensure the quality of the dataset.

Methods used include:

1. Data Cleaning & Preprocessing

- Removed data inconsistencies.
- Validated data types.
- Added derived columns, e.g., Total (calculated as Unit Price × Quantity + Tax).

2. Data Validation with Great Expectations (GX)

- Defined expectations to maintain data quality, such as:
- Unique values for Invoice ID.
- Customer Type limited to “Member” or “Normal.”
- Total ≥ 0.
- Quantity must be an integer.
- Average Rating between 5–10.
- Ensures the dataset is clean and analysis-ready.

3. Exploratory Data Analysis (EDA)

- Distribution analysis.
- Time-based sales trends.
- Customer behavior by type and payment method.
- Visualizations using Kibana (bar charts, pie charts, line charts, etc.).

4. Insights & Business Recommendations

- EDA results are used to provide actionable business insights.
- Supports Marketing, Sales, and Management teams in decision-making.

## Stacks
This project uses a combination of programming languages, tools, and Python libraries to support data analysis and validation:

1. Programming Language

- Python 3.12

2. Python Libraries

- Pandas → Data manipulation and analysis
- Great Expectations (GX) → Data validation and quality assurance
- Numpy → Basic numerical computations

3. Tools

- Apache Airflow → Orchestrating ETL, cleaning, and validation pipelines
- Kibana → Interactive dashboards and visualizations
- Git & GitHub → Version control and collaboration

4. Environment

- Virtual Environment (venv) for dependency isolation

## Reference
- Dataset: [Supermarket Sales Dataset](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)
- [Great Expectations](https://docs.greatexpectations.io)
- [Apache Airflow](https://airflow.apache.org/docs/)
- [Kibana](https://www.elastic.co/guide/en/kibana)
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit)

- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
