# Importamos las librerías necesarias para el manejo de datos, solicitudes HTTP y visualización gráfica
import pandas as pd
import requests
import plotly.graph_objs as go

# Definimos una función para obtener datos desde una URL específica y convertirlos en un DataFrame de pandas
def obtener_datos(url):
    try:
        # Realizamos una solicitud GET a la URL
        response = requests.get(url)
        # Verificamos que la respuesta sea exitosa (código de estado 200)
        response.raise_for_status()
        # Convertimos la respuesta en formato JSON a un diccionario de Python
        data = response.json()
        # Verificamos si hay datos disponibles y si el segundo elemento es una lista
        if len(data) > 1 and isinstance(data[1], list):
            # Creamos un DataFrame de pandas con los datos obtenidos
            df = pd.DataFrame(data[1])
            # Seleccionamos y renombramos las columnas de interés
            df = df[['date', 'value']]
            df.columns = ['Año', 'Valor']
            # Convertimos la columna 'Año' al formato de fecha y extraemos solo el año
            df['Año'] = pd.to_datetime(df['Año']).dt.year
            # Establecemos la columna 'Año' como el índice del DataFrame
            df.set_index('Año', inplace=True)
            # Eliminamos filas con valores faltantes
            df.dropna(inplace=True)
            return df
        else:
            print("No hay datos disponibles en la respuesta")
            return pd.DataFrame()
    except requests.RequestException as e:
        # Manejamos cualquier error en la solicitud HTTP
        print(f"Error al obtener datos: {e}")
        return pd.DataFrame()
    
# Definimos una función para cargar datos de múltiples URLs, donde cada URL corresponde a un indicador diferente
def cargar_datos(urls):
    dfs = {}
    for key, url in urls.items():
        dfs[key] = obtener_datos(url)
    return dfs

# Diccionario que contiene las URLs (APIs) de los indicadores de interés para El Salvador
urls = {
    "PIB": "http://api.worldbank.org/v2/country/SLV/indicator/NY.GDP.MKTP.CD?date=1994:2024&format=json",
    "Crecimiento económico" : "http://api.worldbank.org/v2/country/SLV/indicator/NY.GDP.MKTP.KD.ZG?date=1994:2024&format=json",
    "Inflación" : "http://api.worldbank.org/v2/country/SLV/indicator/FP.CPI.TOTL.ZG?date=1994:2024&format=json",
    "Tasa de desempleo" : "http://api.worldbank.org/v2/country/SLV/indicator/SL.UEM.TOTL.ZS?date=1994:2024&format=json",
    "Gasto Público" : "http://api.worldbank.org/v2/country/SLV/indicator/GC.XPN.TOTL.GD.ZS?date=1994:2024&format=json",
    "Nivel de pobreza" : "http://api.worldbank.org/v2/country/SLV/indicator/SI.POV.DDAY?date=1994:2024&format=json",
    "Mortalidad niños < 5 años" : "http://api.worldbank.org/v2/country/SLV/indicator/SH.DYN.MORT?date=1994:2024&format=json",
    "Distribución de los ingresos" : "http://api.worldbank.org/v2/country/SLV/indicator/SI.POV.GINI?date=1994:2024&format=json",
    "Tasa Alfabetización" : "http://api.worldbank.org/v2/country/SLV/indicator/SE.ADT.LITR.ZS?date=1994:2024&format=json",
    "Mujeres en el parlamento" : "http://api.worldbank.org/v2/country/SLV/indicator/SG.GEN.PARL.ZS?date=1994:2024&format=json",
    "Homicidios<br>(por cada 100.000 hab)" : "http://api.worldbank.org/v2/country/SLV/indicator/VC.IHR.PSRC.P5?date=1994:2024&format=json",
    "Emisiones de carbono" : "http://api.worldbank.org/v2/country/SLV/indicator/EN.ATM.CO2E.KT?date=1994:2024&format=json",
    "Acceso a la electricidad" : "http://api.worldbank.org/v2/country/SLV/indicator/EG.ELC.ACCS.ZS?date=1994:2024&format=json",
    "Electricidad provenientes de<br>fuentes de energías renovables" : "http://api.worldbank.org/v2/country/SLV/indicator/EG.ELC.RNWX.KH?date=1994:2024&format=json",
    "Acceso a Internet" : "http://api.worldbank.org/v2/country/SLV/indicator/IT.NET.USER.ZS?date=1994:2024&format=json",
    "Uso telefonía móvil" : "http://api.worldbank.org/v2/country/SLV/indicator/IT.CEL.SETS.P2?date=1994:2024&format=json",
    "Uso Banda Ancha" : "http://api.worldbank.org/v2/country/SLV/indicator/IT.NET.BBND.P2?date=1994:2024&format=json"
}

# Mapeamos cada indicador a un Objetivo de Desarrollo Sostenible (ODS) específico
ods_correspondencia = {
    "pib": "ODS 8: Trabajo decente y crecimiento económico",
    "Crecimiento económico": "ODS 8: Trabajo decente y crecimiento económico",
    "inflacion": "ODS 8: Reducción de las desigualdades",
    "desempleo": "ODS 8: Trabajo decente y crecimiento económico",
    "gasto_publico": "ODS 8: Alianzas para lograr los objetivos",
    "Nivel de pobreza" : "ODS 1: Fin de la pobreza",
    "mortalidad_ninos" : "ODS 3: Salud y bienestar",
    "gini" : "ODS 10: Reducción de las desigualdades",
    "tasa_alfabetizacion" : "ODS 4: Educación de calidad",
    "mujeres_parlamento" : "ODS 5: Igualdad de género",
    "delincuencia_100" : "ODS 16: Paz, justicia e instituciones sólidas",
    "emisiones_carbono" : "ODS 13: Acción por el clima",
    "acceso_electicidad" : "ODS 9: Industria, innovación e infraestructura",
    "elect_renovable" : "ODS 9: Industria, innovación e infraestructura",
    "uso_internet" : "ODS 17: Alianzas para los objetivos",
    "uso_telefono_movil" : "ODS 17: Alianzas para los objetivos",
    "uso_banda_ancha" : "ODS 17: Alianzas para los objetivos"
}

# Cargamos los datos utilizando las URLs definidas anteriormente
dfs = cargar_datos(urls)

# Ordenamos los ODS de menor a mayor
ods_ordenados = [
    "ODS 1: Fin de la pobreza",
    "ODS 3: Salud y bienestar",
    "ODS 4: Educación de calidad",
    "ODS 5: Igualdad de género",
    "ODS 8: Trabajo decente y crecimiento económico",
    "ODS 9: Industria, innovación e infraestructura",
    "ODS 10: Reducción de las desigualdades",
    "ODS 13: Acción por el clima",
    "ODS 16: Paz, justicia e instituciones sólidas",
    "ODS 17: Alianzas para los objetivos"
]

# Agrupamos los indicadores según el ODS al que pertenecen
ods_agrupados = {
    "ODS 1: Fin de la pobreza": ["Nivel de pobreza"],
    "ODS 3: Salud y bienestar": ["Mortalidad niños < 5 años"],
    "ODS 4: Educación de calidad": ["Tasa Alfabetización"],
    "ODS 5: Igualdad de género": ["Mujeres en el parlamento"],
    "ODS 8: Trabajo decente y crecimiento económico": ["PIB", "Crecimiento económico", "Inflación", "Tasa de desempleo","Gasto Público"],
    "ODS 9: Industria, innovación e infraestructura": ["Acceso a la electricidad", "Electricidad provenientes de<br>fuentes de energías renovables"],
    "ODS 10: Reducción de las desigualdades": ["Distribución de los ingresos"],
    "ODS 13: Acción por el clima": ["Emisiones de carbono"],
    "ODS 16: Paz, justicia e instituciones sólidas": ["Homicidios<br>(por cada 100.000 hab)"],
    "ODS 17: Alianzas para los objetivos": ["Acceso a Internet", "Uso telefonía móvil", "Uso Banda Ancha"]
}

# Creamos una figura vacía para la visualización de los datos
fig = go.Figure()

# Añadimos las trazas según la agrupación de ODS
for ods_nombre, indicadores in ods_agrupados.items():
    for indicador in indicadores:
        df = dfs.get(indicador)
        if df is not None:
            fig.add_trace(go.Scatter(x=df.index, y=df['Valor'], mode='lines+markers',
                                     name=f"{ods_nombre} - {indicador}", visible="legendonly"))

# Actualizamos la configuración del layout del gráfico, incluyendo títulos y leyendas
fig.update_layout(title="Indicadores de El Salvador: Socio-Económicos, Ambientales y de Delincuencia",
                  xaxis_title='Año',
                  yaxis_title='Valor',
                  legend_title="Indicadores y ODS correspondientes")

# Mostramos la gráfica
fig.show()
