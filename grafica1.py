import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conexion = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='www..germanrojas123.,',
    database='mydb'
)



query = "SELECT year, politicalParty, SUM(voteCount) as totalVotes FROM Election GROUP BY year, politicalParty"
df = pd.read_sql_query(query, conexion)



# Agrupa los datos por año y partido
df_pivot = df.pivot(index='politicalParty', columns='year', values='totalVotes')

# Genera la gráfica de barras
df_pivot.plot(kind='bar', stacked=False)

# Personaliza la gráfica
plt.xlabel('Partido Político')
plt.ylabel('Total de Votaciones')
plt.title('Comparación del Conteo de Votaciones por Año y por Partido')
plt.ticklabel_format(style='plain', axis='y')

# Muestra la gráfica
plt.show()
