import psycopg2

def DB_init():
    con = psycopg2.connect(database="postgres", user="postgres", password="bitlab", host="127.0.0.1", port="5432")
    print("Database opened successfully")
    cur = con.cursor()

    cur.execute('''CREATE TABLE Misuration(ID INT PRIMARY KEY NOT NULL,CO2  FLOAT  NOT NULL,TEMPERATURE  INT   NOT NULL,HUMIDITY   FLOAT); ''')
    print("Table created successfully")
    con.commit()
    con.close()
def insert_intodb(id:int ,CO2: float,Temperature :float,Humidity: float):
    con = psycopg2.connect(database="postgres", user="postgres", password="bitlab", host="127.0.0.1", port="5432")
    print("Database opened successfully")
    cur = con.cursor()
    cur.execute(f'''INSERT INTO MISURATION(ADMISSION,CO2,TEMPERATURE,HUMIDITY) VALUES ({id},{CO2},{Temperature},{Humidity});''')
    con.commit()
    print("Values succesfully committed")
    con.close()
def DB_query():
    con = psycopg2.connect(database="postgres", user="postgres", password="bitlab", host="127.0.0.1", port="5432")
    print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT* from Misuration")
    rows = cur.fetchall()

    for row in rows:
        
        print("id =", row[0])
        print("CO2=", row[1])
        print("TEMPERATURE =", row[2])
        print("HUMIDITY =", row[3], "n")

    print("Operation done successfully")
    con.close()    