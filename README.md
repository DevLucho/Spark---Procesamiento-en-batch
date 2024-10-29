# Proyecto de Análisis de Datos con PySpark

## Descripción

Este proyecto utiliza PySpark para analizar datos de estudiantes a partir de un archivo CSV almacenado en HDFS. El objetivo es realizar diversas consultas sobre la información de los estudiantes, incluyendo su género, nivel educativo de los padres y puntajes en módulos evaluados.

## Requisitos Previos

Antes de ejecutar el código, asegúrate de tener instalados los siguientes componentes:

- [Apache Spark](https://spark.apache.org/) (versión recomendada: 3.0 o superior)
- [PySpark](https://pypi.org/project/pyspark/) (instalación mediante pip)
- [Hadoop](https://hadoop.apache.org/) (para el sistema de archivos HDFS)
- Python 3.x

## Instalación

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/DevLucho/Spark-Procesamiento-en-batch.git

2. **Asegúrate de que el archivo CSV (u37r-hjmu.csv) esté disponible en HDFS en la ruta:**
  hdfs://localhost:9000/Tarea3/u37r-hjmu.csv

## Ejecución del Código

1. Iniciar Spark: Asegúrate de que tu entorno Spark esté correctamente configurado y que los servicios necesarios estén en ejecución.
2. Ejecutar el Script: Ejecuta el script en un entorno que soporte PySpark:
  ```bash
  spark-submit students_data_analysis.py
