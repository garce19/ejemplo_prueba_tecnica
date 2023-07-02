import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='www..germanrojas123.,',
    database='mydb'
)

cursor = conexion.cursor()

# ¿Cuál fue el año en que se realizaron más votaciones?
query1 = "SELECT year, SUM(voteCount) as totalVotes FROM Election GROUP BY year ORDER BY totalVotes DESC LIMIT 1"
cursor.execute(query1)

result1 = cursor.fetchone()
if result1:
    year = result1[0]
    total_votes = result1[1]
    print(f"1. El año con más votaciones fue {year}, con un total de {total_votes} votos.")
    print('-------------------------------')
    archivo = open('pregunta1.txt', 'w')
    archivo.write(f"El año con más votaciones fue {year}, con un total de {total_votes} votos.")
    archivo.close()

else:
    print("No se encontraron datos de votaciones.")

# ¿Cuál fue el condado con menos votaciones en el 2008?
# Ejecutar la consulta
query2 = "SELECT county.county, election.codeCounty, voteCount FROM Election INNER JOIN County ON Election.codeCounty = County.codeCounty WHERE year = 2008 ORDER BY voteCount ASC LIMIT 1"
cursor.execute(query2)

# Obtener el resultado
result2 = cursor.fetchone()

if result2:
    county = result2[0]
    code_county = result2[1]
    vote_count = result2[2]
    print(f"2. El condado con menos votaciones en 2008 fue {county}, con un total de {vote_count} votos.")
    print('-------------------------------')
    archivo = open('pregunta2.txt', 'w')
    archivo.write(f"El condado con menos votaciones en 2008 fue {county}, con un total de {vote_count} votos.")
    archivo.close()
else:
    print("No se encontraron datos de votaciones en 2008.")

# ¿Cuáles fueron los 3 condados que tuvieron más votaciones por el partido demócrata en los años del 2000 al 2008?
# Ejecutar la consulta
query3 = "SELECT county.county, election.codeCounty, SUM(election.voteCount) as totalVotes FROM Election inner join County ON election.codeCounty = County.codeCounty WHERE year BETWEEN 2000 AND 2008 AND politicalParty = 'democrat' GROUP BY codeCounty ORDER BY totalVotes DESC LIMIT 3;"
cursor.execute(query3)

# Obtener el resultado
results3 = cursor.fetchall()

if results3:
    print("3. Los 3 condados con más votaciones por el partido demócrata entre 2000 y 2008 fueron:")
    for result in results3:
        county = result[0]
        code_county = result[1]
        total_votes = result[2]
        print(f"{county}: {total_votes} votos")
        archivo = open('pregunta3.txt', 'a')
        archivo.write(f"\n{county}: {total_votes} votos")
        archivo.close()
    print('-------------------------------')
else:
    print("No se encontraron datos de votaciones por el partido demócrata entre 2000 y 2008.")

# ¿Cuál partido tuvo menos votaciones en el rango de años de 2012 a 2016?
# Ejecutar la consulta
query4 = "SELECT politicalParty, SUM(voteCount) as totalVotes FROM Election WHERE year BETWEEN 2012 AND 2016 GROUP BY politicalParty ORDER BY totalVotes ASC LIMIT 1"
queryOp = "SELECT politicalParty, SUM(voteCount) as totalVotes FROM Election WHERE year BETWEEN 2012 AND 2016 AND politicalParty != 'other' GROUP BY politicalParty ORDER BY totalVotes ASC LIMIT 1"
cursor.execute(query4)

# Obtener el resultado
result4 = cursor.fetchone()


if result4:
    party = result4[0]
    total_votes = result4[1]
    
    print(f"4. El partido con menos votaciones entre 2012 y 2016 fue {party}, con un total de {total_votes} votos.")
    archivo = open('pregunta4.txt', 'w')
    archivo.write(f"El partido con menos votaciones entre 2012 y 2016 fue {party}, con un total de {total_votes} votos.")
    archivo.close()
    

else:
    print("No se encontraron datos de votaciones entre 2012 y 2016.")

cursor.execute(queryOp) 
resultOp = cursor.fetchone() 
party1 = resultOp[0]
total1 = resultOp[1]
print(f'En caso de que no se quiera tener en cuenta los resultador de "other", el segundo partido menos votado fue: {party1}, con un total de {total1} votos.')
print('-------------------------------')
archivo = open('pregunta4.txt', 'a')
archivo.write(f'\nEn caso de que no se quiera tener en cuenta los resultador de "other", el segundo partido menos votado fue: {party1}, con un total de {total1} votos.')
archivo.close()
cursor.close()
conexion.close()