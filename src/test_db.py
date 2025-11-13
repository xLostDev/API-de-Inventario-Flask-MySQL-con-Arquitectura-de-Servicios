from db import get_connection

conn = get_connection()

if conn:
    print("✅ Conexión exitosa a MySQL")
    conn.close()
else:
    print("❌ Error al conectar")
