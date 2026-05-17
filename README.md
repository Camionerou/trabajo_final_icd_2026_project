# Trabajo Final ICD 2026 - IBM HR Analytics

Proyecto para el trabajo final de Introduccion a Ciencia de Datos.

Notebook en Colab:

https://colab.research.google.com/github/Camionerou/trabajo_final_icd_2026_project/blob/main/notebooks/trabajo_final_icd_2026_ibm_hr_analytics.ipynb

## Objetivo

Predecir si un empleado abandona la empresa voluntariamente usando el dataset IBM HR Analytics.

Variable objetivo:

- `Attrition = Yes`: el empleado se fue.
- `Attrition = No`: el empleado no se fue.

## Dataset

Archivo entregado por el profesor:

- `IBM HR Analytics Employee_TF.csv`

La consigna original esta en:

- `Trabajo Final ICD 2026 IBM HR Analytics.pdf`

## Estructura

- `notebooks/`: notebook principal para trabajar en Google Colab.
- `figuras/`: graficos exportados para usar en el informe.
- `informes/`: informe final y borradores.
- `requirements.txt`: librerias necesarias para ejecutar el analisis.

## Flujo de trabajo

1. Exploracion inicial del dataset.
2. Limpieza y preparacion de datos.
3. Seleccion de variables relevantes.
4. Entrenamiento de dos modelos supervisados.
5. Evaluacion con metricas y matrices de confusion.
6. Comparacion entre modelos.
7. Informe final en lenguaje claro.

## Modelos elegidos

Se trabajara con:

- Regresion Logistica.
- Random Forest.

La Regresion Logistica sirve como modelo simple e interpretable. Random Forest permite comparar contra un modelo mas flexible.

## Ejecucion en Google Colab

La consigna pide usar Google Colab. Para ejecutar el proyecto:

1. Subir este proyecto a GitHub.
2. Abrir `notebooks/trabajo_final_icd_2026_ibm_hr_analytics.ipynb` desde Colab.
3. Asegurarse de que el archivo `IBM HR Analytics Employee_TF.csv` este disponible junto al notebook o en la raiz del proyecto.
4. Ejecutar las celdas en orden.
5. Descargar las figuras generadas en `figuras/` para incorporarlas al informe final.

El notebook esta preparado para leer el CSV tanto si se ejecuta desde la raiz del proyecto como si se ejecuta desde la carpeta `notebooks/`.

## Estado actual

- Proyecto Git inicializado.
- Dataset y consigna incorporados.
- Notebook base creado.
- Exploracion inicial agregada.
- Preparacion de datos y modelos definidos en pipelines.
- Borrador de hallazgos iniciales disponible en `informes/exploracion_inicial.md`.
