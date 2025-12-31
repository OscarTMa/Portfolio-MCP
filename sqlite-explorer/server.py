import sqlite3
from mcp.server.fastmcp import FastMCP

# Inicializamos el servidor
mcp = FastMCP("Explorador de Datos SQL")

# Función auxiliar para conectar a la BD (simulada en memoria)
def get_db():
    # Usamos ':memory:' para que se borre al cerrar, o pon "ventas.db" para guardar archivo
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # 1. Creamos datos de prueba (Seed Data)
    cursor.execute("CREATE TABLE IF NOT EXISTS ventas (id INTEGER, producto TEXT, cantidad INTEGER, precio REAL, fecha TEXT)")
    
    datos = [
        (1, 'Laptop Pro', 2, 1200.50, '2024-03-01'),
        (2, 'Mouse Gamer', 10, 45.00, '2024-03-02'),
        (3, 'Teclado Mecánico', 5, 80.00, '2024-03-02'),
        (4, 'Monitor 27"', 3, 300.00, '2024-03-03'),
        (5, 'Cable HDMI', 20, 10.00, '2024-03-03')
    ]
    cursor.executemany("INSERT INTO ventas VALUES (?,?,?,?,?)", datos)
    conn.commit()
    return conn

@mcp.tool()
def consultar_base_de_datos(query_sql: str) -> str:
    """
    Ejecuta una consulta SQL de LECTURA (SELECT) sobre la base de datos de ventas.
    Útil para responder preguntas de negocio como '¿Cuál fue el producto más vendido?'.
    """
    # Seguridad básica: Solo permitimos SELECT
    if not query_sql.strip().upper().startswith("SELECT"):
        return "Error: Por seguridad, solo permito consultas SELECT."

    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query_sql)
        columnas = [description[0] for description in cursor.description]
        resultados = cursor.fetchall()
        conn.close()
        
        if not resultados:
            return "La consulta no devolvió resultados."
            
        # Formatear respuesta bonita
        texto = f"Columnas: {', '.join(columnas)}\n"
        for fila in resultados:
            texto += str(fila) + "\n"
        return texto

    except Exception as e:
        return f"Error SQL: {str(e)}"

if __name__ == "__main__":
    mcp.run()