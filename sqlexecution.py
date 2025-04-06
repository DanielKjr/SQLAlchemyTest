from sqlalchemy import create_engine, MetaData, Table, select, text
from sqlalchemy.orm import sessionmaker
from classes import Classes


#ved at lave det til en funktion kan denne forbindelses oprettes uden at have gentagene kode
#(
# noter til BI - når der er defineret funktioner som det her, så køre det kun hvis man kalder det direkte
# ellers så køres alt koden fra top til bund
# findes også i en anden fil, så man kan bruge "from engineCreator import getEngine" og bruge på tværs a filer
#)
def getEngine():
    connectionString = (
    "mssql+pyodbc://localhost\\SQLEXPRESS/master?"
    "driver=ODBC+Driver+17+for+SQL+Server&"
    "trusted_connection=yes&"
    "encrypt=no"
    )
    return create_engine(connectionString)

#den her gør brug af session, det gør at den har transactions som man kender fra sql, hvor den låner forbindelsen fra getengine.
#altså ikke et krav men brugbar at have med
def hentFraSqlMedKlasser():
    Session = sessionmaker(getEngine())
    with Session.begin() as session:
        statement = select(Classes)
        classes_obj = session.scalars(statement).all()
        for row in classes_obj:
          #fordi det er med objekt mapping så kan der tilgåes via property navne, kan være praktisk med tabeller der ofte tilgås
          print(row.BasicClassId, row.Refnr)

def hentFraSqlUdenOpsatKlasse():
    #laver et objekt med db skemaet så den kan læse det
    metadata = MetaData()
    engine = getEngine()
    classes_table = Table("Classes", metadata, autoload_with=engine)
    # opret en forbindelse der lever i dette scope (altså lukkes bagefter)
    with engine.connect() as conn:
        statement = select(classes_table)
        result = conn.execute(statement).fetchall()
        # for hver række i result print (udskriv) række
        for row in result:
         print(row)

def hentMedSql():
    with getEngine().connect() as conn:
        result = conn.execute(text("SELECT BasicClassId, Refnr FROM dbo.Classes"))
        rows = result.fetchall()
        for row in rows:
         print(row)


print("Skriv tallet tilsvarene metoden der skal kaldes:")
print("1: hentFraSqlUdenKlasser \n 2: hentFraSqlUdenOpsatKlasse \n 3: hentMedSql")
userinput = input()
def runFromInput(userinput):
   match userinput:
      case "1": hentFraSqlMedKlasser()
      case "2": hentFraSqlUdenOpsatKlasse()
      case "3": hentMedSql()
runFromInput(userinput)

