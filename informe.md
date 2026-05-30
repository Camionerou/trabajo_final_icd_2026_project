# Informe — Trabajo Final ICD 2026 (IBM HR Analytics)

## Objetivo

La idea del trabajo es predecir si un empleado se va a ir de la empresa o no. Eso está en
la columna `Attrition`: `Yes` quiere decir que se fue y `No` que se quedó. Como tengo los
datos históricos junto con la respuesta, es un problema de **clasificación supervisada**.
Para resolverlo entrené y comparé dos modelos que vimos en la materia: **Regresión
Logística** y **Random Forest**.

Todo el código está en el notebook `trabajo_final_icd_2026.ipynb`. Acá explico lo que hice
y los resultados.

## Los datos

El dataset tiene **1470 filas y 35 columnas** con información de los empleados: edad,
sueldo, puesto, antigüedad, nivel de satisfacción, si hace horas extra, etc.

Lo primero que miré fue cómo está repartida la variable que quiero predecir:

![Distribución de Attrition](figuras/distribucion_attrition.png)

La mayoría de los empleados se queda: **1233 con `No` (≈83.9%)** y solo **237 con `Yes`
(≈16.1%)**. Esto es importante porque el dataset está **desbalanceado**, y un modelo podría
tener un accuracy alto simplemente diciendo casi siempre `No`. Por eso más adelante no miro
solo el accuracy.

## Exploración

Revisé los valores faltantes y encontré tres columnas con datos vacíos:

| Columna | Faltantes |
| --- | ---: |
| DistanceFromHome | 147 |
| DailyRate | 73 |
| Age | 44 |

También vi que hay columnas que tienen siempre el mismo valor (`EmployeeCount`,
`StandardHours`, `Over18`) y una que es solo un número de legajo (`EmployeeNumber`). Esas
no aportan nada para predecir, así que las saco después.

Después hice algunos gráficos para entender mejor los datos.

**Salario según si se fue o no (boxplot):**

![Boxplot del salario](figuras/boxplot_salario.png)

Los que se fueron suelen tener sueldos más bajos: su caja queda más abajo que la de los que
se quedaron.

**Edad según si se fue o no (violín):**

![Violín de la edad](figuras/violin_edad.png)

Los que se van tienden a ser más jóvenes, se concentran más cerca de los 30 años.

**Attrition según horas extra:**

![Attrition según horas extra](figuras/rotacion_overtime.png)

Los empleados que hacen horas extra se van bastante más seguido que los que no.

**Mapa de calor de correlaciones:**

![Mapa de calor](figuras/heatmap_correlaciones.png)

Sirve para ver qué variables se mueven juntas. Por ejemplo, las variables de antigüedad
(años en la empresa, en el puesto, con el jefe) están relacionadas entre ellas, y el sueldo
va de la mano de la experiencia total. Igual, que dos cosas vayan juntas no significa que
una cause la otra: es solo lo que muestran los datos.

## Preparación de los datos

Primero revisé que no hubiera errores de entrada: no hay filas duplicadas, las edades están
todas en un rango razonable (18 a 60 años) y `Attrition` solo tiene los valores `Yes`/`No`.
Así que los datos venían limpios y no hubo que corregir nada.

Después los preparé para el modelo:

- Saqué las columnas que no aportan (las constantes y el legajo).
- Pasé `Attrition` a número (`No = 0`, `Yes = 1`), porque los modelos trabajan con números.
- Convertí las columnas de texto en columnas 0/1 con `get_dummies(drop_first=True)`
  (one-hot encoding). Quedaron **44 columnas**.
- Dividí en entrenamiento (80%) y prueba (20%) usando `stratify` para mantener la misma
  proporción de `Yes`/`No` en las dos partes. Quedaron **1176 filas de entrenamiento y 294
  de prueba**.
- Recién ahí rellené los faltantes con la **mediana del conjunto de entrenamiento**: la
  calculo solo con `train` para no filtrar información del `test`. Uso la mediana porque es
  robusta y no se deja arrastrar por valores extremos.
- Escalé las variables con `StandardScaler`. La Regresión Logística lo necesita porque es
  sensible a la escala; al Random Forest no le afecta.

## Modelos y resultados

Entrené los dos modelos y los evalué sobre el conjunto de prueba (294 empleados, de los
cuales 47 eran `Yes`). Estas fueron las métricas:

| Métrica | Regresión Logística | Random Forest |
| --- | ---: | ---: |
| Accuracy | 0.8605 | 0.8401 |
| Precision (Yes) | 0.6154 | 0.5000 |
| Recall (Yes) | 0.3404 | 0.1064 |
| F1 (Yes) | 0.4384 | 0.1754 |

![Comparación de modelos](figuras/comparacion_modelos.png)

Las matrices de confusión muestran en qué se equivoca cada modelo (las filas son el valor
real y las columnas lo que predijo):

![Matriz de confusión - Regresión Logística](figuras/matriz_confusion_logistica.png)

La Regresión Logística acertó **253 de los 294** casos. De los 47 empleados que realmente
se fueron, detectó **16**. No es mucho, pero es el modelo que más encontró.

![Matriz de confusión - Random Forest](figuras/matriz_confusion_random_forest.png)

El Random Forest acertó **247 de 294**, pero de los 47 que se fueron solo detectó **5**.
Casi siempre predice `No`.

Lo interesante es que los dos modelos tienen un accuracy parecido y bastante alto (84–86%),
pero eso es en gran parte porque la mayoría de los empleados son `No`. Cuando miro el
**recall de la clase `Yes`** (cuántos de los que se fueron logré encontrar), se nota que a
los dos les cuesta, y que la Regresión Logística anda mejor (34% contra 11%).

## Variables más importantes

El Random Forest deja ver qué variables pesan más para decidir:

![Importancia de variables](figuras/importancia_variables.png)

Las que más influyen son el sueldo (`MonthlyIncome`), la edad (`Age`), los años trabajados
(`TotalWorkingYears`), algunas tarifas (`DailyRate`, `HourlyRate`, `MonthlyRate`) y la
distancia al trabajo (`DistanceFromHome`). También aparece `OverTime_Yes`, que coincide con
lo que ya había visto en los gráficos.

## Conclusión

Entrené y comparé dos modelos para predecir la rotación de empleados. La **Regresión
Logística** fue mejor en todas las métricas: más accuracy y, sobre todo, mejor recall y F1
para la clase `Yes`, que es la que importa si la idea es anticipar renuncias.

De todas formas, ningún modelo detecta del todo bien a los que se van. Eso pasa porque hay
pocos casos `Yes` (el dataset está desbalanceado), así que a los modelos les cuesta aprender
ese grupo.
