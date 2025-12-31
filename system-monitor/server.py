from mcp.server.fastmcp import FastMCP
import psutil # Librería para leer datos del PC
import datetime

# 1. INICIALIZACIÓN
# Creamos el servidor. El nombre 'Monitor' aparecerá en los logs.
mcp = FastMCP("Monitor de Sistema")

# 2. DEFINICIÓN DE HERRAMIENTAS (TOOLS)
# Usamos el decorador @mcp.tool(). Esto le dice a la IA:
# "Oye, aquí hay una función que puedes usar si te preguntan sobre esto".

@mcp.tool()
def obtener_uso_cpu() -> str:
    """
    Devuelve el porcentaje de uso actual de la CPU.
    Úsalo cuando el usuario pregunte si la computadora está lenta o trabajando mucho.
    """
    # Explicación: La IA lee el texto de arriba (docstring) para saber CUÁNDO usar esto.
    uso = psutil.cpu_percent(interval=1)
    return f"El uso de CPU es del {uso}%"

@mcp.tool()
def obtener_memoria_ram() -> str:
    """
    Devuelve el uso de memoria RAM disponible y usada.
    """
    memoria = psutil.virtual_memory()
    gb_usados = round(memoria.used / (1024 ** 3), 2)
    gb_total = round(memoria.total / (1024 ** 3), 2)
    return f"RAM: {gb_usados} GB usados de {gb_total} GB totales."

@mcp.tool()
def obtener_hora_local() -> str:
    """Devuelve la fecha y hora actual del sistema."""
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"La hora local del sistema es: {ahora}"

# 3. EJECUCIÓN
if __name__ == "__main__":
    mcp.run()