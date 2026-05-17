# Resultados de modelos

Metricas sobre el conjunto de prueba:

| Modelo | Accuracy | Precision_Yes | Recall_Yes | F1_Yes |
| --- | --- | --- | --- | --- |
| Random Forest | 0.8401 | 0.5000 | 0.0638 | 0.1132 |
| Regresion Logistica | 0.7551 | 0.3529 | 0.6383 | 0.4545 |

## Reportes de clasificacion

### Regresion Logistica

```text
precision    recall  f1-score   support

          No       0.92      0.78      0.84       247
         Yes       0.35      0.64      0.45        47

    accuracy                           0.76       294
   macro avg       0.64      0.71      0.65       294
weighted avg       0.83      0.76      0.78       294
```

### Random Forest

```text
precision    recall  f1-score   support

          No       0.85      0.99      0.91       247
         Yes       0.50      0.06      0.11        47

    accuracy                           0.84       294
   macro avg       0.67      0.53      0.51       294
weighted avg       0.79      0.84      0.78       294
```

## Variables mas importantes segun Random Forest

| Variable | Importancia |
| --- | --- |
| num__MonthlyIncome | 0.0718 |
| num__Age | 0.0623 |
| num__TotalWorkingYears | 0.0528 |
| num__DailyRate | 0.0487 |
| num__YearsAtCompany | 0.0462 |
| num__DistanceFromHome | 0.0429 |
| num__HourlyRate | 0.0424 |
| num__MonthlyRate | 0.0419 |
| num__YearsWithCurrManager | 0.0378 |
| num__NumCompaniesWorked | 0.0374 |
| num__PercentSalaryHike | 0.0327 |
| cat__OverTime_Yes | 0.0309 |
| num__StockOptionLevel | 0.0305 |
| num__YearsInCurrentRole | 0.0288 |
| cat__OverTime_No | 0.0278 |
