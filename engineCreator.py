from sqlalchemy import create_engine

def getEngine():
    connectionString = (
    "mssql+pyodbc://localhost\\SQLEXPRESS/master?"
    "driver=ODBC+Driver+17+for+SQL+Server&"
    "trusted_connection=yes&"
    "encrypt=no"
    )
    return create_engine(connectionString)