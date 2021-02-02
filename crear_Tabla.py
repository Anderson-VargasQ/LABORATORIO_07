import psycopg2

def crear_tablas():
    comandos = (
        """CREATE TABLE DATOS_JUEGO(
            NOMBRE_USUARIO VARCHAR(30) PRIMARY KEY,
            PUNTAJE INTEGER NOT NULL)
        """,
    )
    
    conn = None
    
    try:
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        database="prueba2",
        password="123456789")
        
        cur = conn.cursor()
        
        for comando in comandos:
            cur.execute(comando)
        
        cur.close()
        conn.commit()

        if conn is not None:
            conn.close()
            
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    crear_tablas()
