import psycopg2

def insert_datos(NOMBRE_USUARIO, PUNTAJE):
    sql = """ INSERT INTO DATOS_JUEGO (NOMBRE_USUARIO, PUNTAJE) VALUES (%s, %s);"""
    
    conn = None
    
    try:
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        database="prueba2",
        password="123456789")
        
        cur = conn.cursor()
        
        cur.execute(sql, (NOMBRE_USUARIO, PUNTAJE))
        
        conn.commit()
        cur.close()

        if conn is not None:
            conn.close()

    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()
