# Amazon Product Sales

Proyecto de análisis de datos de productos de Amazon. Su finalidad es construir un pipeline reproducible que normalice los datos de origen y genere métricas que permitan responder preguntas de negocio.

La primera pregunta analizada es:

> ¿Cuáles son los productos más demandados según las compras del último mes?

El análisis utiliza `bought_last_month` como indicador de demanda y lo complementa con calificación, número de reseñas, precio, cupones y patrocinio. La interpretación y las limitaciones del resultado están documentadas en el notebook de negocio.

## Flujo del proyecto

1. Extrae el archivo CSV sin procesar desde `data/raw/`.
2. Normaliza encabezados, campos de compras, calificaciones, precios, reseñas, cupones y variables booleanas.
3. Conserva las columnas analíticas y calcula el precio final disponible.
4. Genera el dataset limpio en `data/processed/clean_dataset.csv`.
5. Explora los datos y responde preguntas de negocio en los notebooks.

La ejecución del pipeline no requiere indicar rutas: el proyecto determina sus directorios de datos a partir de su propia estructura.

## Estructura

```text
.
├── data/
│   ├── raw/                 # Datos de entrada
│   └── processed/           # Dataset normalizado generado
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   └── 02_business_questions_boughts.ipynb
├── src/amazon_product_sales/
│   ├── extract/             # Lectura de datos
│   ├── transform/           # Limpieza y normalización
│   ├── load/                # Escritura del dataset procesado
│   └── utils/               # Resolución de rutas del proyecto
├── tests/                   # Pruebas automatizadas
├── main.py                  # Punto de entrada del pipeline
└── pyproject.toml           # Configuración y dependencias del proyecto
```

## Requisitos

- Python 3.10 o superior.
- `pip` actualizado.
- Git, si se clonará el repositorio.

Las dependencias y la configuración de desarrollo se declaran en `pyproject.toml`; no es necesario instalar paquetes desde rutas locales ni configurar rutas absolutas.

## Instalación

Desde la raíz del repositorio, crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

En Windows (PowerShell), actívalo con:

```powershell
.venv\Scripts\Activate.ps1
```

Instala el proyecto junto con las dependencias de desarrollo definidas en `pyproject.toml`:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Ejecutar el pipeline

Con el entorno virtual activo y desde la raíz del repositorio:

```bash
python -m main
```

El comando lee el CSV de entrada, aplica las transformaciones y escribe el resultado en `data/processed/clean_dataset.csv`.

## Ejecutar los notebooks

Inicia Jupyter desde la raíz del proyecto:

```bash
jupyter notebook
```

Después, ejecuta los notebooks en este orden:

1. `notebooks/01_exploratory_analysis.ipynb`
2. `notebooks/02_business_questions_boughts.ipynb`

El segundo notebook usa Plotly para las tarjetas y el ranking. Si el entorno no cuenta ya con esta librería, instálala antes de ejecutarlo:

```bash
python -m pip install plotly
```

## Pruebas

Ejecuta toda la suite de pruebas con:

```bash
python -m pytest
```

Las pruebas cubren la extracción del CSV, las transformaciones de limpieza y la generación del archivo procesado.

## Herramientas y librerías

| Herramienta o librería | Uso en el proyecto |
| --- | --- |
| Python | Lenguaje del pipeline y del análisis. |
| pandas | Lectura de CSV, limpieza, transformación y análisis tabular. |
| NumPy | Soporte para operaciones numéricas durante la transformación. |
| Jupyter | Ejecución y documentación del análisis exploratorio y de negocio. |
| Plotly | Visualizaciones interactivas del notebook de preguntas de negocio. |
| Matplotlib y Seaborn | Visualización exploratoria. |
| pytest | Pruebas automatizadas. |
| Ruff | Revisión estática y formato del código durante el desarrollo. |
| setuptools | Empaquetado e instalación editable definidos en `pyproject.toml`. |

## Consideraciones sobre las métricas

El dataset permite ordenar y comparar registros según las compras del último mes. Antes de convertir un agregado por título en una conclusión de demanda por producto, se debe validar la granularidad de los registros (por ejemplo, producto, variante o publicación) para no sumar métricas repetidas. Esta consideración se detalla en el notebook `02_business_questions_boughts.ipynb`.
