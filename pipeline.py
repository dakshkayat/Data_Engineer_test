import xml.etree.ElementTree as ET
import pandas as pd
import sqlalchemy

# Input TMX file path
tmx_file_path = "ar-en.tmx"
tree = ET.parse(tmx_file_path)
root = tree.getroot()

translation_units = []

# Define the namespace for the 'xml' prefix
namespaces = {"xml": "http://www.w3.org/XML/1998/namespace"}

# Extract translation units from the TMX file
for tu in root.findall(".//tu", namespaces=namespaces):
    # Extract English and Arabic translations
    English = tu.find(".//tuv[@xml:lang='en']/seg", namespaces=namespaces).text
    Arabic = tu.find(".//tuv[@xml:lang='ar']/seg", namespaces=namespaces).text

    # Append translation units to the list
    translation_units.append((English, Arabic))

# Create a Pandas DataFrame from the translation units
df = pd.DataFrame(translation_units, columns=["English", "Arabic"])

# Define your database connection string
connection_string = (
    "mssql+pyodbc://PC\\SQLEXPRESS/Translated_data?"
    "trusted_connection=yes&driver=ODBC Driver 17 for SQL Server"
)

# Create a SQLAlchemy engine for database connection
engine = sqlalchemy.create_engine(connection_string)

# Create a SQLAlchemy metadata object for defining table schema
metadata = sqlalchemy.MetaData()

# Define the table schema for the database
translated_table = sqlalchemy.Table(
    "Translated_Table",
    metadata,
    sqlalchemy.Column("English", sqlalchemy.String(7000)),
    sqlalchemy.Column("Arabic", sqlalchemy.String(7000)),
)

# Create the table in the database if it doesn't already exist
metadata.create_all(engine)

# Insert data from the DataFrame into the database table
df.to_sql("Translated_Table", con=engine, if_exists="replace", index=False)
