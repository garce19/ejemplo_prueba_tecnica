import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conexion = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='www..germanrojas123.,',
    database='mydb'
)

# Consulta SQL para obtener los datos de votos por partido
query = "SELECT politicalParty, SUM(voteCount) as totalVotes FROM Election GROUP BY politicalParty"

# Obtener los datos de la base de datos y almacenarlos en un DataFrame de pandas
df = pd.read_sql_query(query, conexion)

# Cerrar la conexión a la base de datos
conexion.close()

# Crear el gráfico de pastel
plt.pie(df['totalVotes'], labels=df['politicalParty'], autopct='%1.1f%%')

# Personalizar el gráfico
plt.title('Distribución de Votos entre Partidos')

# Mostrar el gráfico
plt.show()
