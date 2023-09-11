# TMX to SQL Data Pipeline

This data pipeline is designed to extract translation units from TMX (Translation Memory Exchange) files, convert them into a Pandas DataFrame, and insert the data into a SQL Server database table. This README provides detailed instructions on setting up and running the pipeline.

## Prerequisites

Before running the data pipeline, ensure you have the following prerequisites installed on your system:

- Python 3.x (https://www.python.org/downloads/)
- Pip (Python package manager)
- Microsoft SQL Server installed and running, along with the ODBC Driver 17 for SQL Server (https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server)
- A TMX file containing translation data (e.g., "ar-en.tmx") in the project directory.

## Usage
Follow these steps to run the data pipeline:

1. Place your TMX file (e.g., "ar-en.tmx") in the project directory. Ensure the file contains translation units with both English and Arabic translations.

2. Open the pipeline.py script and ensure the tmx_file_path variable points to the correct TMX file:

    tmx_file_path = "ar-en.tmx"
3. Run the data pipeline:
   python pipeline.py
4. The pipeline will parse the TMX file, create a Pandas DataFrame with translation units, and insert the data into a SQL Server database table named "Translated_Table."

5. You can now access and query the translated data in your SQL Server database for further analysis or use.

## Configuration
To customize the database connection or table schema, modify the following variables in the pipeline.py script:

connection_string: Update this variable to specify your SQL Server connection details.
translated_table: Define the table schema according to your requirements.

