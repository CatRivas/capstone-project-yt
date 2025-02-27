# YOUTUBE COMMENTS ANALYSIS (ALSO METADA!)

## Version 1

Este repositorio contiene el código y la documentación de mi proyecto Capstone, en el que se extrae información de videos de YouTube mediante la API de YouTube Data v3 utilizando Python.

*** Justificación de la elección de Python como lenguaje de tutoriales a analizar: ***

* Lenguaje más deseado según el Stack Overflow Developer Survey 2024.
* Popularidad y disponibilidad de tutoriales en inglés y español por FreeCodeCamp.

# Sprints del Proyecto

## Sprint 1: Comprension de los datos
Objetivo: Configurar el entorno de trabajo y extraer metadata y comentarios de videos de YouTube.

*** Tareas completadas: ***

* Configuración de un repositorio en GitHub.
* Creación de un .gitignore con la herramienta Gitignore Generator.
* Implementación de la extracción del video ID desde una URL de YouTube.
* Uso de la API de YouTube Data v3 para obtener:
    * Metadata del video (título, canal, visualizaciones, duración, etc.).
    * Comentarios principales (top-level comments).
    * Almacenamiento de la información en archivos CSV.

* Entregables:

    * .gitignore: Archivo que excluye archivos sensibles como .env.
    * .env: Archivo que almacena secretos.
    * data_fetcher.py: Script principal que obtiene metadata y comentarios de videos de YouTube.
    * comments_video_*.csv: Archivos CSV que almacenan comentarios obtenidos.
    * metadata_videos.csv: Archivo CSV con metadata de los videos procesados.



Sprint 2: Optimización del Código y Gestión de Recursos (Pendiente)

🔜 Objetivo: Mejorar el rendimiento y optimización del código, reduciendo el uso de memoria.

🔹 Tareas a realizar:

Optimización del manejo de datos en memoria con pandas.

Reducción de llamadas innecesarias a la API de YouTube.

Implementación de logs para monitorear el rendimiento.

📂 Entregables esperados:

Código optimizado en data_fetcher.py.

Reducción en el consumo de memoria y llamadas a la API.

Sprint 3: Implementación de Análisis de Datos (Pendiente)

🔜 Objetivo: Aplicar análisis exploratorio a los datos obtenidos.

🔹 Tareas a realizar:

Análisis de sentimientos en los comentarios.

Creación de gráficos y métricas sobre los videos y su impacto.

📂 Entregables esperados:

Visualizaciones y análisis descriptivo.

Informe con hallazgos clave.

Sprint 4: Creación de una Interfaz de Usuario (Pendiente)

🔜 Objetivo: Desarrollar una interfaz para facilitar la consulta de datos.

🔹 Tareas a realizar:

Creación de un dashboard interactivo en Streamlit.

Implementación de filtros para explorar videos y comentarios.

📂 Entregables esperados:

Aplicación funcional en Streamlit.

Sprint 5: Documentación Final y Presentación del Proyecto (Pendiente)

🔜 Objetivo: Preparar la documentación completa y presentación del proyecto.

🔹 Tareas a realizar:

Redacción del informe final.

Presentación de resultados y aprendizajes.

📂 Entregables esperados:

Documento final del proyecto.

Presentación lista para compartir.

🛠️ Tecnologías Utilizadas

Python (pandas, googleapiclient, dotenv, urllib)

YouTube Data API v3

CSV para almacenamiento de datos

Git y GitHub para control de versiones
