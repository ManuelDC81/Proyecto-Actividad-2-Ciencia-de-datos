Primero, importamos las bibliotecas pandas, requests y plotly.graph_objs porque necesitamos herramientas para manejar datos, hacer solicitudes a APIs, y crear gráficos, respectivamente.

Definimos cargar_datos_excel(ruta_archivo), una función para cargar un archivo Excel. Usamos pandas para leer el archivo, convertimos la columna 'Año' a formato de fecha, la establecemos como índice del DataFrame, y luego retornamos este DataFrame.

La función obtener_datos(url) hace una solicitud a una URL (que es una API) usando requests. Si la respuesta es exitosa (código 200), intentamos convertir los datos JSON a un DataFrame de pandas, seleccionando solo las columnas 'date' y 'value', renombrándolas a 'Año' y 'Valor', convirtiendo 'Año' a formato de fecha, estableciéndola como índice y descartando filas sin datos. Si algo sale mal, imprimimos un error.

Establecemos ruta_archivo_delincuencia con la ruta de un archivo Excel y lo cargamos usando cargar_datos_excel.

Definimos varias URLs que apuntan a diferentes indicadores económicos y sociales disponibles a través de la API del Banco Mundial, preparándonos para obtener esos datos.

Utilizamos obtener_datos(url) para cada URL definida, almacenando los DataFrames resultantes en variables correspondientes a cada indicador.

Inicializamos una figura de plotly para crear un gráfico interactivo y luego agregamos a este gráfico diferentes series de datos correspondientes a cada uno de los indicadores, como el PIB, el crecimiento económico, etc., usando fig.add_trace.

Finalmente, configuramos el layout del gráfico con un título, etiquetas para los ejes, y un título para la leyenda. Muestramos el gráfico usando fig.show().
