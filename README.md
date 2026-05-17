# Trabajo Final ICD 2026 - IBM HR Analytics

Proyecto para el trabajo final de Introduccion a Ciencia de Datos.

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
