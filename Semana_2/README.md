Minería de Datos 2026 – Semana 2
Alumno: Lionel A. Martinez.

Limpieza, Transformación y Análisis Exploratorio de Datos
Descripción

En esta actividad se trabajó con un dataset de empleados que presentaba problemas comunes en proyectos de análisis de datos, como valores faltantes, inconsistencias y datos atípicos.

El objetivo fue aplicar técnicas de limpieza, transformación y análisis exploratorio (EDA) para mejorar la calidad de los datos y prepararlos para futuros modelos de Machine Learning.

Objetivos
Identificar tipos de datos (numéricos, categóricos, ordinales).
Detectar y corregir errores en los datos.
Aplicar técnicas de limpieza (faltantes, inconsistencias, outliers).
Transformar variables categóricas en numéricas.
Normalizar variables numéricas.
Realizar análisis exploratorio de datos (EDA).
Utilizar un LLM como apoyo metodológico.
Limpieza de Datos

Se realizaron las siguientes acciones:

Corrección de valores inválidos en la variable Edad (valores negativos).
Imputación de valores faltantes en Salario utilizando la mediana.
Normalización de texto en la variable Estado (ej: "ACTIVO" → "Activo").
Detección y eliminación de valores atípicos en Salario mediante el método IQR.

Resultado: Se eliminó un outlier (salario = 200000), mejorando la consistencia del dataset.

Transformación de Datos

Se aplicaron las siguientes transformaciones:

Codificación ordinal en la variable Nivel Educativo:
Licenciado → 0
Ingeniero → 1
Doctorado → 2
Normalización Min-Max en la variable Salario (valores entre 0 y 1).
Creación de nueva variable:
Años hasta jubilación = 65 - Edad

Estas transformaciones permiten que los datos sean utilizados en modelos de aprendizaje automático.

Análisis Exploratorio de Datos (EDA)

Se realizaron visualizaciones y análisis como:

Histograma de la variable Edad.
Gráfico de dispersión entre Edad y Salario.
Cálculo de correlación entre variables.
Hallazgos:
La edad presenta una distribución concentrada en valores intermedios.
Existe una relación positiva entre edad y salario.
No se observan valores extremos luego de la limpieza.
Uso de LLM

Se utilizó ChatGPT como herramienta de apoyo.

Prompt utilizado:

"¿Cómo detectar y eliminar outliers en Python?"

Síntesis:
El modelo sugirió métodos como IQR y Z-score para detectar valores atípicos. Se eligió IQR por no depender de la distribución de los datos.

Validación propia:
El método IQR permitió identificar correctamente el valor extremo en salario (200000), el cual fue eliminado para mejorar el análisis.

Archivos incluidos
AO1_Clase2_Apellido_Nombre.ipynb → Notebook completo
AO1_Clase2_Apellido_Nombre.pdf → Versión exportada
Conclusión

El proceso de limpieza y transformación permitió mejorar significativamente la calidad del dataset.

El análisis exploratorio facilitó la comprensión de los datos y la detección de patrones relevantes, dejando el dataset preparado para futuros modelos de Machine Learning.

Tecnologías utilizadas
Python 
Pandas
Scikit-learn
Seaborn / Matplotlib
Google Colab
