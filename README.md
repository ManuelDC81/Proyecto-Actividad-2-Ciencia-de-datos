# Visualización de Indicadores de Desarrollo Sostenible para El Salvador

Este proyecto está diseñado para obtener y visualizar una serie de indicadores socioeconómicos, ambientales y de delincuencia de El Salvador, vinculándolos a los Objetivos de Desarrollo Sostenible (ODS) de las Naciones Unidas. Utiliza datos disponibles públicamente a través de las APIs del Banco Mundial.

## Características

- Obtención de datos en tiempo real de varias APIs.
- Limpieza y preparación de datos para análisis.
- Visualización de series de tiempo para cada indicador.
- Agrupación de indicadores según su ODS correspondiente.

## Tecnologías Utilizadas

- Python 3
- Pandas: Para el manejo de datos.
- Requests: Para realizar solicitudes HTTP.
- Plotly: Para la visualización de datos.

## Cómo Funciona

1. **Obtención de Datos:** Se realizan solicitudes HTTP a las APIs del Banco Mundial para obtener los datos de los indicadores de interés para El Salvador.
2. **Preparación de Datos:** Los datos obtenidos se limpian, preparan y organizan en DataFrames de Pandas para su análisis.
3. **Visualización:** Se generan gráficas de series de tiempo para cada indicador, agrupadas según el ODS al que están asociadas.

## Cómo Usarlo

1. Asegúrate de tener instalado Python 3 y las librerías mencionadas.
2. Clona este repositorio en tu máquina local.
3. Ejecuta el script principal para ver las visualizaciones.

```python
python main.py
```

## Contribuir

Las contribuciones son siempre bienvenidas. Si tienes alguna sugerencia para mejorar este proyecto, por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT). Siente libre de usarlo, modificarlo y distribuirlo.
