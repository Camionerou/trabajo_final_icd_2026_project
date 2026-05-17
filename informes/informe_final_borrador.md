# Informe final - IBM HR Analytics

## 1. Introduccion

Este trabajo analiza un dataset de empleados de IBM con el objetivo de predecir si un empleado abandona la empresa voluntariamente. La variable a predecir es `Attrition`, que puede tomar los valores `Yes` o `No`.

El problema se plantea como una tarea de clasificacion supervisada, porque se cuenta con ejemplos historicos donde ya se conoce si el empleado abandono o no la empresa.

## 2. Descripcion del dataset

El dataset contiene 1470 registros y 35 columnas. Incluye informacion demografica, laboral y de satisfaccion de los empleados.

La variable objetivo esta desbalanceada:

- 1233 empleados no abandonaron la empresa.
- 237 empleados si abandonaron la empresa.

Esto significa que aproximadamente el 16% de los registros corresponde a empleados con rotacion laboral.

## 3. Exploracion inicial

Durante la exploracion se revisaron:

- Tipos de datos.
- Valores faltantes.
- Distribucion de la variable objetivo.
- Variables numericas.
- Variables categoricas.
- Relaciones iniciales entre algunas variables y `Attrition`.

Se detectaron valores faltantes en:

- `Age`
- `DailyRate`
- `DistanceFromHome`

Tambien se detectaron columnas que no aportan informacion porque tienen un unico valor:

- `EmployeeCount`
- `Over18`
- `StandardHours`

Ademas, se decidio eliminar `EmployeeNumber`, ya que es un identificador interno del empleado.

## 4. Visualizaciones exploratorias

El notebook genera los graficos pedidos por la consigna:

- Boxplot de `MonthlyIncome` segun `Attrition`.
- Violin plot de `Age` segun `Attrition`.
- Mapa de calor de correlaciones.

Tambien genera visualizaciones adicionales:

- Distribucion de `Attrition`.
- Tasa de rotacion segun `OverTime`.
- Tasa de rotacion segun `JobRole`.

Primeras observaciones:

- Los empleados con horas extra (`OverTime = Yes`) muestran mayor proporcion de rotacion.
- Los empleados que viajan frecuentemente tambien muestran mayor rotacion.
- El rol `Sales Representative` aparece con una tasa alta de abandono.
- Los empleados solteros presentan una tasa de rotacion mayor que otros estados civiles.

## 5. Preparacion de datos

Antes de entrenar los modelos se realiza:

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

## 7. Evaluacion

Los modelos se evaluaron con:

- Accuracy.
- Precision para la clase `Yes`.
- Recall para la clase `Yes`.
- F1 para la clase `Yes`.
- Matriz de confusion de cada modelo.

La matriz de confusion es obligatoria segun la consigna y permite ver cuantos empleados fueron clasificados correctamente e incorrectamente en cada clase.

## 8. Comparacion de modelos

Se agrego tambien un baseline que predice siempre la clase mayoritaria (`No`). Esto ayuda a interpretar el accuracy, porque el dataset esta desbalanceado.

| Modelo | Accuracy | Precision Yes | Recall Yes | F1 Yes |
| --- | ---: | ---: | ---: | ---: |
| Random Forest | 0.8401 | 0.5000 | 0.0638 | 0.1132 |
| Baseline mayoria | 0.8401 | 0.0000 | 0.0000 | 0.0000 |
| Regresion Logistica | 0.7551 | 0.3529 | 0.6383 | 0.4545 |

Random Forest tuvo mejor accuracy que Regresion Logistica, pero casi no detecto casos `Yes`. La Regresion Logistica tuvo menor accuracy general, pero encontro muchos mas empleados que efectivamente abandonaron la empresa.

## 9. Conclusion

El modelo mas util para este objetivo es la Regresion Logistica, porque el problema principal no es solo acertar muchos casos `No`, sino detectar empleados con `Attrition = Yes`.

Limitaciones:

- No se puede afirmar causalidad.
- Es una primera version del analisis.
- No se hizo ajuste profundo de parametros.
- Las metricas pueden cambiar con otra division de datos.
