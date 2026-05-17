# Resultados de modelos

Metricas sobre el conjunto de prueba:

| Modelo | Train_Accuracy | Accuracy | Precision_Yes | Recall_Yes | F1_Yes |
| --- | --- | --- | --- | --- | --- |
| Random Forest | 1.0000 | 0.8401 | 0.5000 | 0.0638 | 0.1132 |
| Baseline mayoria | 0.8384 | 0.8401 | 0.0000 | 0.0000 | 0.0000 |
| Regresion Logistica | 0.7815 | 0.7551 | 0.3529 | 0.6383 | 0.4545 |

## Reportes de clasificacion

### Baseline mayoria

```text
precision    recall  f1-score   support

          No       0.84      1.00      0.91       247
         Yes       0.00      0.00      0.00        47

    accuracy                           0.84       294
   macro avg       0.42      0.50      0.46       294
weighted avg       0.71      0.84      0.77       294
```

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
| OverTime = Yes | 0.0309 |
| StockOptionLevel | 0.0305 |
| YearsInCurrentRole | 0.0288 |
| OverTime = No | 0.0278 |
