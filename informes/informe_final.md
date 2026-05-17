# Informe final - IBM HR Analytics

## 1. Introduccion

Este trabajo analiza un dataset de empleados de IBM con el objetivo de predecir si un empleado abandona la empresa voluntariamente. La variable a predecir es `Attrition`, que puede tomar los valores `Yes` o `No`.

El problema se plantea como una tarea de clasificacion supervisada, porque se cuenta con ejemplos historicos donde ya se conoce si el empleado abandono o no la empresa.

## 2. Descripcion del dataset

El dataset contiene 1470 registros y 35 columnas. Incluye informacion demografica, laboral y de satisfaccion de los empleados.

La variable objetivo esta desbalanceada:

| Attrition | Cantidad | Porcentaje aproximado |
| --- | ---: | ---: |
| No | 1233 | 83.88% |
| Yes | 237 | 16.12% |

Esto significa que la mayoria de los empleados no abandono la empresa. Por eso, ademas de mirar la exactitud general del modelo, tambien es importante analizar que tan bien detecta los casos `Yes`.

## 3. Exploracion inicial

Durante la exploracion se revisaron los tipos de datos, valores faltantes, distribucion de la variable objetivo, variables numericas, variables categoricas y relaciones iniciales entre algunas variables y `Attrition`.

Se detectaron valores faltantes en:

| Columna | Faltantes | Porcentaje aproximado |
| --- | ---: | ---: |
| DistanceFromHome | 147 | 10.00% |
| DailyRate | 73 | 4.97% |
| Age | 44 | 2.99% |

Tambien se detectaron columnas que no aportan informacion porque tienen un unico valor:

- `EmployeeCount`
- `Over18`
- `StandardHours`

Ademas, se decidio eliminar `EmployeeNumber`, ya que es un identificador interno del empleado y no una caracteristica generalizable.

## 4. Visualizaciones exploratorias

El analisis incluye los graficos pedidos por la consigna:

- Boxplot de `MonthlyIncome` segun `Attrition`.
- Violin plot de `Age` segun `Attrition`.
- Mapa de calor de correlaciones.

Tambien se generaron visualizaciones adicionales:

- Distribucion de `Attrition`.
- Tasa de rotacion segun `OverTime`.
- Tasa de rotacion segun `JobRole`.

Primeras observaciones:

- Los empleados con horas extra (`OverTime = Yes`) muestran mayor proporcion de rotacion.
- Los empleados que viajan frecuentemente tambien muestran mayor rotacion.
- El rol `Sales Representative` aparece con una tasa alta de abandono.
- Los empleados solteros presentan una tasa de rotacion mayor que otros estados civiles.

## 5. Preparacion de datos

Antes de entrenar los modelos se realizo:

- Eliminacion de columnas irrelevantes o constantes.
- Separacion entre variables predictoras (`X`) y variable objetivo (`y`).
- Conversion de `Attrition` a valores numericos: `No = 0`, `Yes = 1`.
- Imputacion de valores faltantes numericos con mediana.
- Imputacion de valores faltantes categoricos con el valor mas frecuente.
- Codificacion One-Hot Encoding para variables categoricas.
- Escalado de variables numericas.
- Division train/test con estratificacion.

La estratificacion es importante porque mantiene la proporcion original de empleados que abandonan y no abandonan en los conjuntos de entrenamiento y prueba.

## 6. Modelos utilizados

Se eligieron dos modelos:

### Regresion Logistica

Es un modelo simple e interpretable. Sirve como punto de comparacion inicial y permite observar si existe una relacion razonablemente lineal entre las variables y la probabilidad de abandono.

### Random Forest

Es un modelo basado en muchos arboles de decision. Puede capturar relaciones mas complejas entre las variables y suele tener buen rendimiento en problemas tabulares.

## 7. Evaluacion de modelos

Los modelos se evaluaron con:

- Accuracy.
- Precision para la clase `Yes`.
- Recall para la clase `Yes`.
- F1 para la clase `Yes`.
- Matriz de confusion de cada modelo.

Metricas sobre el conjunto de prueba:

| Modelo | Train Accuracy | Test Accuracy | Precision Yes | Recall Yes | F1 Yes |
| --- | ---: | ---: | ---: | ---: | ---: |
| Random Forest | 1.0000 | 0.8401 | 0.5000 | 0.0638 | 0.1132 |
| Regresion Logistica | 0.7806 | 0.7551 | 0.3529 | 0.6383 | 0.4545 |

La diferencia entre train y test tambien ayuda a interpretar los resultados. Random Forest llego a 100% de accuracy en entrenamiento, pero bajo a 84.01% en prueba. Esto sugiere que el modelo aprendio muy bien los datos de entrenamiento, aunque no necesariamente generaliza igual de bien para detectar los casos `Yes`.

## 8. Interpretacion de matrices de confusion

La Regresion Logistica acerto 222 casos de 294 en el conjunto de prueba. Detecto 30 de los 47 empleados que efectivamente abandonaron la empresa. Su principal debilidad fue que tambien marco como posibles abandonos a varios empleados que en realidad no se fueron.

Random Forest acerto 247 casos de 294, por eso tuvo mayor accuracy. Sin embargo, solo detecto 3 de los 47 empleados que abandonaron la empresa. Esto muestra que, aunque el accuracy sea alto, el modelo casi siempre predice `No` y por eso no resulta tan util si el objetivo principal es anticipar la rotacion.

## 9. Comparacion final

Random Forest obtuvo mejor accuracy general:

- Random Forest: 84.01%
- Regresion Logistica: 75.51%

Pero Regresion Logistica obtuvo mejor rendimiento para detectar empleados que abandonan la empresa:

- Recall Yes de Regresion Logistica: 63.83%
- Recall Yes de Random Forest: 6.38%

En este problema, detectar los casos `Attrition = Yes` es especialmente importante, porque la empresa podria usar el modelo para anticipar posibles renuncias. Por ese motivo, aunque Random Forest tenga mayor exactitud general, la Regresion Logistica resulta mas util para este objetivo.

## 10. Variables importantes

Segun Random Forest, las variables con mayor importancia fueron:

| Variable | Importancia |
| --- | ---: |
| MonthlyIncome | 0.0718 |
| Age | 0.0623 |
| TotalWorkingYears | 0.0528 |
| DailyRate | 0.0487 |
| YearsAtCompany | 0.0462 |
| DistanceFromHome | 0.0429 |
| HourlyRate | 0.0424 |
| MonthlyRate | 0.0419 |
| YearsWithCurrManager | 0.0378 |
| NumCompaniesWorked | 0.0374 |
| PercentSalaryHike | 0.0327 |
| OverTime_Yes | 0.0309 |
| StockOptionLevel | 0.0305 |
| YearsInCurrentRole | 0.0288 |
| OverTime_No | 0.0278 |

Estas variables sugieren que la rotacion laboral esta relacionada con factores economicos, edad, trayectoria laboral, antiguedad, distancia al trabajo y horas extra.

## 11. Conclusion

El trabajo permitio entrenar y comparar dos modelos supervisados para predecir rotacion laboral.

Random Forest fue el modelo con mayor accuracy, pero tuvo bajo rendimiento para detectar la clase minoritaria `Yes`. En cambio, Regresion Logistica tuvo menor accuracy general, pero fue mucho mejor para identificar empleados que abandonan la empresa.

Como el objetivo del problema es anticipar posibles renuncias, se recomienda priorizar la Regresion Logistica en esta primera version del analisis. El modelo no es perfecto, pero ofrece una deteccion mas util de los casos de rotacion.

Como mejora futura, se podria probar ajuste de hiperparametros, validacion cruzada y tecnicas especificas para datasets desbalanceados.
