# Customer Data Pipeline

Proyecto de Ingeniería de Datos desarrollado con PySpark.

## Descripción General

Este proyecto simula un pipeline completo de procesamiento de datos:

CSV
→ Validación de Datos
→ Transformaciones de Negocio
→ Parquet

## Dataset

Bank Customer Churn Prediction Dataset

## Tecnologías Utilizadas

- Python
- PySpark
- Pandas
- PostgreSQL
- Parquet

## Validación de Datos

Antes de realizar las transformaciones se ejecutaron controles de calidad sobre el dataset.

### Conteo de Registros

Se verificó la cantidad total de registros.

- Total de registros: 10.000

### Conteo de Columnas

Se validó la estructura del dataset.

- Total de columnas: 12

### Validación de Nulos

Se verificó la existencia de valores nulos en todas las columnas.

- No se detectaron valores nulos.

### Validación de Duplicados

Se verificó la existencia de registros duplicados.

- No se detectaron registros duplicados.

## Evidencia de Validaciones

images/validation_results.png

## Validación de Valores Nulos

images/null_check.png

## Transformaciones de Negocio

### churn_desc

Se creó una descripción amigable para el indicador de abandono de clientes.

| churn | churn_desc |
|--------|-------------|
| 0 | Activo |
| 1 | Abandono |

### age_group

Se realizó una segmentación de clientes por grupo etario.

| Edad | Grupo |
|-------|--------|
| < 30 | Young |
| 30 - 49 | Adult |
| >= 50 | Senior |

## Análisis de Negocio

images/churn_by_age_group.png

## Resultado

El resultado final del procesamiento se almacena en formato Parquet:

```text
data/curated/customer_churn.parquet
```

## Estructura del Proyecto

images/project_structure.png

## Estructura del Repositorio

```text
customer-data-pipeline
│
├── data
│   ├── raw
│   │   └── customer_churn.csv
│   │
│   └── curated
│       └── customer_churn.parquet
│
├── images
│   ├── validation_results.png
│   ├── null_check.png
│   ├── churn_by_age_group.png
│   └── project_structure.png
│
├── src
│   └── pipeline.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Resultados Obtenidos

- Ingesta de datos mediante PySpark.
- Validación de registros, columnas, nulos y duplicados.
- Aplicación de reglas de negocio.
- Generación de salida optimizada en formato Parquet.
- Simulación de un flujo real de Ingeniería de Datos.