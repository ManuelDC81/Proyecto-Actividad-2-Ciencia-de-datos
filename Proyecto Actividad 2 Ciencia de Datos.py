# Importamos las bibliotecas necesarias
import pandas as pd
import requests
import plotly.graph_objs as go

# Definimos una función para cargar datos desde un archivo Excel
def cargar_datos_excel(ruta_archivo):
    df = pd.read_excel(ruta_archivo)  # Cargar datos desde el archivo Excel
    df['Año'] = pd.to_datetime(df['Año'], format='%Y').dt.year  # Convertir la columna de año al formato esperado
    df.set_index('Año', inplace=True)  # Establecer la columna de año como índice
    return df

# Definimos una función para obtener datos desde una URL
def obtener_datos(url):
    response = requests.get(url)  # Realizar una solicitud GET a la URL
    if response.status_code == 200:  # Si la solicitud es exitosa
        data = response.json()  # Convertimos los datos de respuesta a JSON
        if len(data) > 1 and isinstance(data[1], list):  # Verificamos si los datos están en el formato esperado
            df = pd.DataFrame(data[1])  # Creamos un DataFrame desde los datos
            df = df[['date', 'value']]  # Seleccionamos solo las columnas relevantes
            df.columns = ['Año', 'Valor']  # Renombramos las columnas
            df['Año'] = pd.to_datetime(df['Año']).dt.year  # Convertimos la columna de año al formato esperado
            df.set_index('Año', inplace=True)  # Establecemos la columna de año como índice
            df.dropna(inplace=True)  # Eliminamos filas con valores nulos
            return df  # Devolvemos el DataFrame con los datos
        else:
            print("No hay datos disponibles en la respuesta")  # Imprimir un mensaje de error si no hay datos disponibles
            return pd.DataFrame()  # Devolvemos un DataFrame vacío
    else:
        print("Fallo al obtener datos de la API del Banco Mundial")  # Imprimir un mensaje de error si la solicitud falla
        return pd.DataFrame()  # Devolvemos un DataFrame vacío

# Definimos la ruta del archivo Excel que contiene los datos de delincuencia
ruta_archivo_delincuencia = 'C:/Users/Usuario/Documents/CIENCIA DE DATOS/DELINCUENCIA EN EL SALVADOR 20 AÑOS.xlsx'
# Cargamos los datos de delincuencia desde el archivo Excel
df_delincuencia = cargar_datos_excel(ruta_archivo_delincuencia)

# Definimos las URLs para los indicadores económicos, ambientales y de delincuencia
url_pib = "http://api.worldbank.org/v2/country/SLV/indicator/NY.GDP.MKTP.CD?date=1994:2024&format=json"
url_crecimiento_economico = "http://api.worldbank.org/v2/country/SLV/indicator/NY.GDP.MKTP.KD.ZG?date=1994:2024&format=json"
url_inflacion = "http://api.worldbank.org/v2/country/SLV/indicator/FP.CPI.TOTL.ZG?date=1994:2024&format=json"
url_desempleo = "http://api.worldbank.org/v2/country/SLV/indicator/SL.UEM.TOTL.ZS?date=1994:2024&format=json"
url_gasto_publico = "http://api.worldbank.org/v2/country/SLV/indicator/GC.XPN.TOTL.GD.ZS?date=1994:2024&format=json"
url_nivel_pobreza = "http://api.worldbank.org/v2/country/SLV/indicator/SI.POV.DDAY?date=1994:2024&format=json"
url_tasa_alfabetizacion = "http://api.worldbank.org/v2/country/SLV/indicator/SE.ADT.LITR.ZS?date=1994:2024&format=json"
url_emisiones_carbono = "http://api.worldbank.org/v2/country/SLV/indicator/EN.ATM.CO2E.KT?date=1994:2024&format=json"

# Obtenemos los datos de los indicadores económicos, ambientales y de delincuencia desde las URLs
df_pib = obtener_datos(url_pib)
df_crecimiento_economico = obtener_datos(url_crecimiento_economico)
df_inflacion = obtener_datos(url_inflacion)
df_desempleo = obtener_datos(url_desempleo)
df_gasto_publico = obtener_datos(url_gasto_publico)
df_nivel_pobreza = obtener_datos(url_nivel_pobreza)
df_tasa_alfabetizacion = obtener_datos(url_tasa_alfabetizacion)
df_emisiones_carbono = obtener_datos(url_emisiones_carbono)

# Creamos un gráfico con Plotly
fig = go.Figure()

# Agregamos las series al gráfico
fig.add_trace(go.Scatter(x=df_pib.index, y=df_pib['Valor'], mode='lines+markers', name='PIB'))
fig.add_trace(go.Scatter(x=df_crecimiento_economico.index, y=df_crecimiento_economico['Valor'], mode='lines+markers', name='Crecimiento Económico'))
fig.add_trace(go.Scatter(x=df_inflacion.index, y=df_inflacion['Valor'], mode='lines+markers', name='Inflación'))
fig.add_trace(go.Scatter(x=df_desempleo.index, y=df_desempleo['Valor'], mode='lines+markers', name='Tasa de Desempleo'))
fig.add_trace(go.Scatter(x=df_gasto_publico.index, y=df_gasto_publico['Valor'], mode='lines+markers', name='Gasto Público'))
fig.add_trace(go.Scatter(x=df_nivel_pobreza.index, y=df_nivel_pobreza['Valor'], mode='lines+markers', name='Nivel de Pobreza'))
fig.add_trace(go.Scatter(x=df_tasa_alfabetizacion.index, y=df_tasa_alfabetizacion['Valor'], mode='lines+markers', name='Tasa de Alfabetización'))
fig.add_trace(go.Scatter(x=df_emisiones_carbono.index, y=df_emisiones_carbono['Valor'], mode='lines+markers', name='Emisiones de CO2'))
fig.add_trace(go.Scatter(x=df_delincuencia.index, y=df_delincuencia['Homicidios'], mode='lines+markers', name='Tasa de Homicidios'))

# Configuramos el diseño del gráfico
fig.update_layout(title="Indicadores de El Salvador: Económicos, Ambientales y de Delincuencia",
                  xaxis_title='Año',
                  yaxis_title='Valor',
                  legend_title="Indicadores")

# Mostramos el gráfico
fig.show()
