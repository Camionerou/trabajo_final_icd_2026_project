# Trabajo Final ICD 2026 - IBM HR Analytics

Trabajo final de Introduccion a Ciencia de Datos.

El objetivo es predecir si un empleado se va de la empresa (`Attrition = Yes`) o no
(`Attrition = No`) a partir del dataset de IBM HR Analytics. Es un problema de
clasificacion y uso dos modelos: **Regresion Logistica** y **Random Forest**.

## Archivos

- `trabajo_final_icd_2026.ipynb` - notebook con todo el analisis (exploracion, limpieza, modelos y evaluacion).
- `informe.md` - informe con los resultados y los graficos explicados.
- `IBM HR Analytics Employee_TF.csv` - dataset (separado por `;`).
- `figuras/` - graficos que genera el notebook.
- `requirements.txt` - librerias que uso.

## Como correrlo

En Google Colab:

1. Abrir el notebook: https://colab.research.google.com/github/Camionerou/trabajo_final_icd_2026_project/blob/main/trabajo_final_icd_2026.ipynb
2. Subir el archivo `IBM HR Analytics Employee_TF.csv` (boton de la carpeta, a la izquierda).
3. Ejecutar las celdas en orden.

En la compu:

```bash
pip install -r requirements.txt
jupyter notebook trabajo_final_icd_2026.ipynb
```
