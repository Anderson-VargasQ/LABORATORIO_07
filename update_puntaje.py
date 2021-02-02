import psycopg2

def update_puntaje(NOMBRE_USUARIO, PUNTAJE):
    sql = """ UPDATE DATOS_JUEGO SET PUNTAJE=%s WHERE NOMBRE_USUARIO=%s;"""
    
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
                cur.execute(sql, (PUNTAJE, NOMBRE_USUARIO))
        
        if conn is not None:
            conn.close()
            
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()
