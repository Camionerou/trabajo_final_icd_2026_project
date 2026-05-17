# Exploracion inicial del dataset

Archivo analizado:

- `IBM HR Analytics Employee_TF.csv`

## Tamano del dataset

El dataset tiene:

- 1470 filas.
- 35 columnas.

La variable objetivo es `Attrition`, que indica si el empleado abandono la empresa.

## Distribucion de la variable objetivo

| Attrition | Cantidad | Porcentaje aproximado |
| --- | ---: | ---: |
| No | 1233 | 83.88% |
| Yes | 237 | 16.12% |

Interpretacion inicial:

El dataset esta desbalanceado. La mayoria de los empleados no abandono la empresa. Por eso, al evaluar los modelos no alcanza con mirar solamente la exactitud (`accuracy`), porque un modelo podria acertar mucho prediciendo casi siempre `No`. Conviene mirar tambien metricas para la clase `Yes`, especialmente `recall` y `F1`.

## Valores faltantes

| Columna | Faltantes | Porcentaje aproximado |
| --- | ---: | ---: |
| DistanceFromHome | 147 | 10.00% |
| DailyRate | 73 | 4.97% |
| Age | 44 | 2.99% |

Decision propuesta:

Como son variables numericas, se imputaran con la mediana dentro del pipeline de preparacion. La mediana es una opcion razonable porque es menos sensible a valores extremos que el promedio.

## Columnas sin informacion util

Las siguientes columnas tienen un unico valor en todas las filas:

- `EmployeeCount = 1`
- `Over18 = Y`
- `StandardHours = 80`

Estas variables no ayudan a distinguir empleados que abandonan de empleados que no abandonan. Se eliminaran antes de entrenar los modelos.

Tambien se eliminara:

- `EmployeeNumber`

Motivo: es un identificador interno del empleado. No representa una caracteristica generalizable para predecir rotacion laboral.

## Resumen de variables numericas relevantes

| Variable | Minimo | Mediana | Promedio | Maximo |
| --- | ---: | ---: | ---: | ---: |
| Age | 18 | 36 | 36.91 | 60 |
| DailyRate | 102 | 802 | 803.88 | 1499 |
| DistanceFromHome | 1 | 7 | 9.16 | 29 |
| MonthlyIncome | 1009 | 4919 | 6502.93 | 19999 |
| TotalWorkingYears | 0 | 10 | 11.28 | 40 |
| YearsAtCompany | 0 | 5 | 7.01 | 40 |
| YearsInCurrentRole | 0 | 3 | 4.23 | 18 |
| YearsSinceLastPromotion | 0 | 1 | 2.19 | 15 |
| YearsWithCurrManager | 0 | 3 | 4.12 | 17 |

## Primeras relaciones observadas con Attrition

### Horas extra

| OverTime | Total | Attrition Yes | Tasa de rotacion |
| --- | ---: | ---: | ---: |
| No | 1054 | 110 | 10.4% |
| Yes | 416 | 127 | 30.5% |

Los empleados que hacen horas extra tienen una tasa de rotacion mucho mas alta.

### Viajes laborales

| BusinessTravel | Total | Attrition Yes | Tasa de rotacion |
| --- | ---: | ---: | ---: |
| Non-Travel | 150 | 12 | 8.0% |
| Travel_Frequently | 277 | 69 | 24.9% |
| Travel_Rarely | 1043 | 156 | 15.0% |

Los empleados que viajan frecuentemente muestran mayor rotacion.

### Rol laboral

| JobRole | Total | Attrition Yes | Tasa de rotacion |
| --- | ---: | ---: | ---: |
| Sales Representative | 83 | 33 | 39.8% |
| Laboratory Technician | 259 | 62 | 23.9% |
| Human Resources | 52 | 12 | 23.1% |
| Sales Executive | 326 | 57 | 17.5% |
| Research Scientist | 292 | 47 | 16.1% |
| Healthcare Representative | 131 | 9 | 6.9% |
| Manufacturing Director | 145 | 10 | 6.9% |
| Manager | 102 | 5 | 4.9% |
| Research Director | 80 | 2 | 2.5% |

El rol `Sales Representative` aparece como uno de los grupos con mayor proporcion de empleados que abandonan la empresa.

### Estado civil

| MaritalStatus | Total | Attrition Yes | Tasa de rotacion |
| --- | ---: | ---: | ---: |
| Single | 470 | 120 | 25.5% |
| Married | 673 | 84 | 12.5% |
| Divorced | 327 | 33 | 10.1% |

Los empleados solteros muestran una tasa de rotacion mayor que los casados y divorciados.

## Decisiones para el modelado

Se trabajara con dos modelos:

- Regresion Logistica.
- Random Forest.

Tambien se agregara un baseline simple que predice siempre la clase mayoritaria. No cuenta como modelo principal, pero sirve para comparar si el accuracy de los modelos realmente aporta algo.

La preparacion de datos se hara con pipelines:

- Imputacion de numericas con mediana.
- Imputacion de categoricas con moda.
- Escalado de numericas para Regresion Logistica.
- One-Hot Encoding para categoricas.
- Division train/test estratificada para respetar la proporcion de `Attrition`.

## Graficos que debe generar el notebook

El notebook queda preparado para generar:

- Distribucion de `Attrition`.
- Boxplot de `MonthlyIncome` segun `Attrition`.
- Violin plot de `Age` segun `Attrition`.
- Tasas de rotacion por `OverTime`.
- Tasas de rotacion por `JobRole`.
- Mapa de calor de correlaciones.
- Matriz de confusion de cada modelo.
- Comparacion de metricas entre modelos.
- Importancia de variables de Random Forest.
