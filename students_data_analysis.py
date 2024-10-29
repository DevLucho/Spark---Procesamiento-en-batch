#Importamos librerias necesarias
from pyspark.sql import SparkSession, functions as F

# Inicializa la sesión de Spark
spark = SparkSession.builder.appName('Tarea3').getOrCreate()

# Define la ruta del archivo .csv en HDFS
file_path = 'hdfs://localhost:9000/Tarea3/u37r-hjmu.csv'

# Lee el archivo .csv
df = spark.read.format('csv').option('header','true').option('inferSchema', 'true').load(file_path)

#imprimimos el esquema
df.printSchema()

# Muestra las primeras filas del DataFrame
df.show(truncate=False)


# Consulta: Mostrar el programa académico que cada estudiante esta cursando y la universidad a la cual se encuentra adscrito.
print("Universidad y Programa Académico al cual el estudiante se encuentra inscrito")
estudiante = df.select ('estu_consecutivo','estu_prgm_academico','inst_nombre_institucion')
estudiante.show()

# Consulta: Contabilizar el número de Estudiantes femeninas y Masculinos
print("Número de Estudiantes Masculinos y Femeninas")
numero = df.groupBy('estu_genero').count()
numero.show()

# Consulta: Mostrar el estrato socioeconómico en el que se encuentra cada uno de los alumnos evaluados
print("Estrato socioeconómico de los evaluados")
estrato = df.select('estu_consecutivo', 'fami_estratovivienda')
estrato.show()

# Consulta: Mostrar el nivel de estudios de los padres de los estudiantes examinados
print("Nivel académico de los padres de los alumnos evaluados")
nivel_academico = df.select('estu_consecutivo','fami_educacionpadre', 'fami_educacionmadre')
nivel_academico.show() 

# Consulta: Mostrar el puntaje de cada uno de los módulos evaluado por el código de los estudiantes
print("Puntaje de cada modulo por Institución de Educación\n")
puntaje = df.select('estu_consecutivo', 'mod_razona_cuantitat_punt', 'mod_comuni_escrita_punt', 'mod_lectura_critica_punt', 'mod_ingles_punt', 'mod_competen_ciudada_punt')
puntaje.show()

# Consulta: Mostrar el departamento al que pertenecen las Instituciones de Educación Superior
print("Departamento al que pertenecen cada una de las Instituciones de Educación Superior\n")
ubicacion = df.select('inst_nombre_institucion', 'estu_inst_departamento')
ubicacion.show(truncate=False)

# Consulta: Mostrar número de Instituciones de Educación Superior
print("Cantidad de Instituciones de Educación Superior\n")
cantidad = df.groupBy('inst_nombre_institucion').count()
cantidad.show(truncate=False)
 
