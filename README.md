# Customer Data Pipeline

## Sobre el proyecto

Este fue uno de mis primeros proyectos utilizando PySpark para construir un pipeline completo de procesamiento de datos.

La idea fue trabajar con un dataset de clientes bancarios y recorrer las etapas más habituales de un flujo de datos: validación, transformación y generación de una salida preparada para ser utilizada posteriormente en análisis o procesos de negocio.

Durante el desarrollo realicé controles básicos de calidad de datos, construí nuevas variables y generé un dataset final en formato Parquet.

---

## Dataset utilizado

Para este proyecto utilicé el dataset **Bank Customer Churn Prediction**.

El conjunto de datos contiene información de clientes bancarios e incluye variables relacionadas con edad, país, saldo, actividad, uso de productos y abandono de clientes.

---

## Tecnologías utilizadas

- Python
- PySpark
- Pandas
- PostgreSQL
- Parquet
- Git
- GitHub

---

## Validaciones realizadas

Antes de aplicar cualquier transformación revisé la calidad de los datos para asegurarme de que el dataset estuviera en condiciones de ser procesado.

Las comprobaciones realizadas fueron:

- Conteo total de registros.
- Conteo de columnas.
- Búsqueda de valores nulos.
- Búsqueda de registros duplicados.

Resultados obtenidos:

```text
Total de registros: 10.000
Total de columnas: 12
Valores nulos: 0
Registros duplicados: 0
```

### Evidencia

images/validation_results.png

images/null_check.png

---

## Transformaciones aplicadas

Una vez validada la información se crearon algunas variables adicionales para enriquecer el análisis.

### Clasificación de abandono de clientes

A partir de la variable original `churn` se creó una descripción más amigable.

| churn | churn_desc |
|--------|-------------|
| 0 | Activo |
| 1 | Abandono |

### Segmentación por rango de edad

También se añadió una clasificación sencilla para agrupar clientes por edad.

| Edad | Grupo |
|--------|--------|
| Menor a 30 años | Young |
| Entre 30 y 49 años | Adult |
| 50 años o más | Senior |

---

## Resultado obtenido

Después de aplicar las transformaciones se realizó una exploración básica del churn por grupo etario.

images/churn_by_age_group.png

---

## Salida generada

El resultado final del procesamiento se almacenó en formato Parquet.

```text
data/curated/customer_churn.parquet
```

---

## Organización del proyecto

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

---

## Qué me dejó esta práctica

Con este proyecto pude reforzar varios conceptos que aparecen frecuentemente en tareas de Data Engineering:

- Procesamiento de datos utilizando PySpark.
- Validaciones de calidad antes de transformar información.
- Creación de reglas de negocio sobre DataFrames.
- Generación de resultados en formato Parquet.
- Organización y documentación de proyectos utilizando Git y GitHub.

---

## Autor

Roger Antequera

Data Engineer

Python | SQL | PySpark | PostgreSQL