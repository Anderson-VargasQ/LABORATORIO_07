import psycopg2

def select_lista():
    sql = """ SELECT NOMBRE_USUARIO, PUNTAJE FROM DATOS_JUEGO;"""
    
    conn = None
    
    try:
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        database="prueba2",
        password="123456789")
        
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                
                if cur is not None:
                    fila = cur.fetchall()
                    return fila
        
        if conn is not None:
            conn.close()
            
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()


