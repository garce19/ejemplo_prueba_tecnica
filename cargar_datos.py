import pandas as pd
import re
import mysql.connector

# Función personalizada para convertir valores de cadena con puntos y comas a enteros
def convert_to_int(value):
    if value == '':
        value = 0
    pos = str(value).find('.')
    if pos == 3:
        if len(str(value)) == 5:
            value = str(value) + '00'
        elif len(str(value)) == 6:
            value = str(value) + '0'
        elif len(str(value)) > 7:
            if int(str(value)[7]) >= 5:
                value += 0.001
                value = str(value)[:7]
    elif pos == 2:
        if len(str(value)) == 5:
            value = str(value) + '0'
        elif len(str(value)) > 6:
            if int(str(value)[6]) >= 5:
                value += 0.001
                value = str(value)[:6]
    
    cleaned_value = re.sub(r'[.,]', '', str(value))  # Eliminar puntos y comas
    try:
        return int(round(float(cleaned_value)))
    except ValueError:
        return 0  # Si ocurre un error en la conversión, retornar cero

# Cargar el archivo de Excel
df = pd.read_excel('counties.xlsx', na_values=['NA', 'NaN', 'inf', '-inf'], converters={'population': convert_to_int, 'area': convert_to_int}, dtype={'codecounty':str})

conexion = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='www..germanrojas123.,',
    database='mydb'
)

cursor = conexion.cursor()

# Limpiar los nombres de los condados en la columna 'County'
df['county'] = df['county'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', str(x)))
df['county'] = df['county'].str.strip()

# Rellenar los valores no válidos con cero
df.fillna(0, inplace=True)

# Convertir las columnas 'population' y 'area' al tipo de datos int
df['population'] = df['population'].astype(int)
df['area'] = df['area'].astype(int)

# Mostrar el DataFrame actualizado
#print(df)

for _,row in df.iterrows():
    code_county = row['codecounty']
    county = row['county']
    population = row['population']
    area = row['area']
    #print((code_county), (county), (population), (area))
    query = "INSERT INTO County (codeCounty, county, population, area) values (%s, %s, %s, %s)"
    values = (code_county, county, population, area)
    cursor.execute(query,values)
conexion.commit()

df2 = pd.read_json('elections.json', dtype={'year': int, 'democrat': int, 'republic': int, 'other': int, 'codecounty':str})

#print(df2)
for _,row in df2.iterrows():
    year = int(row['year'])
    democrat = int(row['democrat'])
    republic = int(row['republic'])
    other = int(row['other'])
    codecounty = str(row['codecounty'])

    queryDemocrat = "INSERT INTO Election (year, voteCount, politicalParty, codeCounty) values (%s, %s, %s, %s)"
    valuesDemocrat = (year, democrat, 'democrat', codecounty)
    try:
        cursor.execute(queryDemocrat, valuesDemocrat)
        conexion.commit()
    except mysql.connector.Error as error:
        print(f"Error en la inserción de Other: {error.errno} ({error.sqlstate}): {error.msg}")
        print(f"Registro: {row}")
        
    queryRepublic = "INSERT INTO Election (year, voteCount, politicalParty, codeCounty) values (%s, %s, %s, %s)"
    valuesRepublic = (year, republic, 'republic', codecounty)
    try:
        cursor.execute(queryRepublic, valuesRepublic)
        conexion.commit()
    except mysql.connector.Error as error:
        print(f"Error en la inserción de Other: {error.errno} ({error.sqlstate}): {error.msg}")
        print(f"Registro: {row}")

    queryOther = "INSERT INTO Election (year, voteCount, politicalParty, codeCounty) values (%s, %s, %s, %s)"
    valuesOther = (year, other, 'other', codecounty)
    try:
        cursor.execute(queryOther, valuesOther)
        conexion.commit()
    except mysql.connector.Error as error:
        print(f"Error en la inserción de Other: {error.errno} ({error.sqlstate}): {error.msg}")
        print(f"Registro: {row}")

cursor.close()
conexion.close()