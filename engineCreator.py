import json
import os
from sqlalchemy import create_engine

# hent connectionstring fra mssql lagring i settings
def read_connection_info():
    settings_path = os.path.expanduser("~/AppData/Roaming/Code/User/settings.json")  
    with open(settings_path, 'r') as file:
        settings = json.load(file)
    
    # vælger første, burde ændres
    connection_info = settings.get("mssql.connections", [])[0]  # Assuming you're using the first connection
    
    server = connection_info.get("server")
    database = connection_info.get("database")
    # encrypt = connection_info.get("encrypt", True) 

    return server, database


# opret engine ud fra settings
def get_sqlalchemy_engine():
    server, database  = read_connection_info()
   
    connection_string = (
        f"mssql+pyodbc://{server}/{database}?"
        f"driver=ODBC+Driver+17+for+SQL+Server&"
        f"trusted_connection=yes&"
        f"encrypt=no"

    )
    
    return create_engine(connection_string)