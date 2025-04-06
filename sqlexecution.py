from sqlalchemy import create_engine, MetaData, Table, select, text
from sqlalchemy.orm import sessionmaker
from classes import Classes
from engineCreator import get_sqlalchemy_engine


#ved at lave det til en funktion kan denne forbindelses oprettes uden at have gentagene kode
# hvis det er flere interaktioner i en fil bør der gøres brug af den samme engine
# (advanced) engines er også threadsafe, den indeholer en threadpool hvor der håndteres trådene 
# def getEngine():
#     connectionString = (
#     "mssql+pyodbc://localhost\\SQLEXPRESS/master?"
#     "driver=ODBC+Driver+17+for+SQL+Server&"
#     "trusted_connection=yes&"
#     "encrypt=no"
#     )
#     return create_engine(connectionString)

engine = get_sqlalchemy_engine()
Session = sessionmaker(engine)
#den her gør brug af session, det gør at den har transactions som man kender fra sql, hvor den låner forbindelsen fra getengine.
#altså ikke et krav men brugbar at have med
def hentFraSqlMedKlasser():
    with Session.begin() as session:
        statement = select(Classes)
        classes_obj = session.scalars(statement).all()
        for row in classes_obj:
          #fordi det er med objekt mapping så kan der tilgåes via property navne, kan være praktisk med tabeller der ofte tilgås
          print(row.BasicClassId, row.Refnr)

def hentFraSqlUdenOpsatKlasse():
    #laver et objekt med db skemaet så den kan læse det
    metadata = MetaData()
    classes_table = Table("Classes", metadata, autoload_with=engine)
    # opret en forbindelse der lever i dette scope (altså lukkes bagefter)
    with engine.connect() as conn:
        statement = select(classes_table)
        result = conn.execute(statement).fetchall()
        # for hver række i result print (udskriv) række
        for row in result:
         print(row)

def hentMedSql():
    with engine.connect() as conn:
        # hvis man henter fra dbo schema så behøver man ikke aer specificere
        # result = conn.execute(text("SELECT BasicClassId, Refnr FROM Classes"))
        # hvis andet schema så skal der specificeres, men der er ingen intellisense at hente
        result = conn.execute(text("SELECT Id, Username FROM Undervisning.Players"))
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

