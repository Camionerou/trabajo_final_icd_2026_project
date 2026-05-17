from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "IBM HR Analytics Employee_TF.csv"
FIGURES_DIR = ROOT / "figuras"
REPORTS_DIR = ROOT / "informes"


def save_current_figure(filename: str) -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / filename, dpi=150, bbox_inches="tight")


def plot_attrition_rate(df: pd.DataFrame, column: str, filename: str) -> pd.DataFrame:
    rate = (
        df.groupby(column)["Attrition"]
        .apply(lambda values: (values == "Yes").mean() * 100)
        .sort_values(ascending=False)
        .reset_index(name="Porcentaje_Attrition_Yes")
    )

    plt.figure(figsize=(10, 5))
    sns.barplot(data=rate, x=column, y="Porcentaje_Attrition_Yes", color="#4C78A8")
    plt.title(f"Porcentaje de rotacion segun {column}")
    plt.xlabel(column)
    plt.ylabel("Rotacion Yes (%)")
    plt.xticks(rotation=35, ha="right")
    save_current_figure(filename)
    plt.close()

    return rate


def dataframe_to_markdown(df: pd.DataFrame, float_digits: int = 4) -> str:
    formatted = df.copy()
    for column in formatted.columns:
        if pd.api.types.is_float_dtype(formatted[column]):
            formatted[column] = formatted[column].map(lambda value: f"{value:.{float_digits}f}")

    columns = formatted.columns.tolist()
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]

    for _, row in formatted.iterrows():
        lines.append("| " + " | ".join(str(row[column]) for column in columns) + " |")

    return "\n".join(lines)


def main() -> None:
    sns.set_theme(style="darkgrid")
    plt.rcParams["figure.dpi"] = 120
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH, sep=";")

    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="Attrition", color="#4C78A8")
    plt.title("Distribucion de la variable objetivo")
    plt.xlabel("Rotacion laboral")
    plt.ylabel("Cantidad de empleados")
    save_current_figure("01_distribucion_attrition.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="Attrition", y="MonthlyIncome")
    plt.title("Boxplot de salario mensual segun rotacion")
    plt.xlabel("Rotacion laboral")
    plt.ylabel("Ingreso mensual")
    save_current_figure("02_boxplot_monthly_income_attrition.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.violinplot(data=df, x="Attrition", y="Age")
    plt.title("Violin plot de edad segun rotacion")
    plt.xlabel("Rotacion laboral")
    plt.ylabel("Edad")
    save_current_figure("03_violin_age_attrition.png")
    plt.close()

    plot_attrition_rate(df, "OverTime", "04_rotacion_por_overtime.png")
    plot_attrition_rate(df, "JobRole", "05_rotacion_por_jobrole.png")

    numeric_df = df.select_dtypes(include=["int64", "float64"])
    plt.figure(figsize=(14, 10))
    sns.heatmap(numeric_df.corr(), cmap="coolwarm", center=0)
    plt.title("Mapa de calor de correlaciones numericas")
    save_current_figure("06_heatmap_correlaciones.png")
    plt.close()

    target = "Attrition"
    columns_to_drop = ["EmployeeCount", "EmployeeNumber", "Over18", "StandardHours"]

    X = df.drop(columns=[target] + columns_to_drop)
    y = df[target].map({"No": 0, "Yes": 1})

    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(include=["object", "string"]).columns.tolist()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    models = {
        "Regresion Logistica": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                (
                    "model",
                    LogisticRegression(
                        max_iter=1000,
                        class_weight="balanced",
                        random_state=42,
                    ),
                ),
            ]
        ),
        "Random Forest": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                (
                    "model",
                    RandomForestClassifier(
                        n_estimators=200,
                        class_weight="balanced",
                        random_state=42,
                    ),
                ),
            ]
        ),
    }

    results = []
    reports = []

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        train_acc = accuracy_score(y_train, model.predict(X_train))
        acc = accuracy_score(y_test, y_pred)
        precision_yes = precision_score(y_test, y_pred, zero_division=0)
        recall_yes = recall_score(y_test, y_pred, zero_division=0)
        f1_yes = f1_score(y_test, y_pred, zero_division=0)

        results.append(
            {
                "Modelo": name,
                "Train_Accuracy": train_acc,
                "Accuracy": acc,
                "Precision_Yes": precision_yes,
                "Recall_Yes": recall_yes,
                "F1_Yes": f1_yes,
            }
        )

        reports.append(
            {
                "Modelo": name,
                "Reporte": classification_report(
                    y_test,
                    y_pred,
                    target_names=["No", "Yes"],
                    zero_division=0,
                ),
            }
        )

        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(5, 4))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=["No", "Yes"],
            yticklabels=["No", "Yes"],
        )
        plt.title(f"Matriz de confusion - {name}")
        plt.xlabel("Prediccion")
        plt.ylabel("Valor real")
        save_current_figure(f"07_matriz_confusion_{name.lower().replace(' ', '_')}.png")
        plt.close()

    results_df = pd.DataFrame(results).sort_values("Accuracy", ascending=False)
    results_df.to_csv(REPORTS_DIR / "resultados_modelos.csv", index=False)

    results_long = results_df.melt(id_vars="Modelo", var_name="Metrica", value_name="Valor")
    plt.figure(figsize=(10, 5))
    sns.barplot(data=results_long, x="Metrica", y="Valor", hue="Modelo")
    plt.title("Comparacion de metricas entre modelos")
    plt.xlabel("Metrica")
    plt.ylabel("Valor")
    plt.ylim(0, 1)
    plt.xticks(rotation=20, ha="right")
    save_current_figure("08_comparacion_modelos.png")
    plt.close()

    random_forest_model = models["Random Forest"]
    feature_names = random_forest_model.named_steps["preprocessor"].get_feature_names_out()
    importances = random_forest_model.named_steps["model"].feature_importances_
    feature_importance = (
        pd.DataFrame({"Variable": feature_names, "Importancia": importances})
        .sort_values("Importancia", ascending=False)
        .head(15)
    )
    feature_importance.to_csv(REPORTS_DIR / "importancia_variables_random_forest.csv", index=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=feature_importance, y="Variable", x="Importancia", color="#4C78A8")
    plt.title("Variables mas importantes segun Random Forest")
    plt.xlabel("Importancia")
    plt.ylabel("Variable")
    save_current_figure("09_importancia_variables_random_forest.png")
    plt.close()

    report_lines = [
        "# Resultados de modelos",
        "",
        "Metricas sobre el conjunto de prueba:",
        "",
        dataframe_to_markdown(results_df),
        "",
        "## Reportes de clasificacion",
        "",
    ]

    for item in reports:
        report_lines.extend(
            [
                f"### {item['Modelo']}",
                "",
                "```text",
                item["Reporte"].strip(),
                "```",
                "",
            ]
        )

    report_lines.extend(
        [
            "## Variables mas importantes segun Random Forest",
            "",
            dataframe_to_markdown(feature_importance),
            "",
        ]
    )

    (REPORTS_DIR / "resultados_modelos.md").write_text("\n".join(report_lines), encoding="utf-8")

    print(results_df.to_string(index=False))


if __name__ == "__main__":
    main()
