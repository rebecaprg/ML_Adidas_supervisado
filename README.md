# **PREDICCIÓN DEL OPERATING PROFIT DE ADIDAS US SALES**

## **Descripción del proyecto**

Este proyecto implementa un flujo completo de Machine Learning para predecir el Operating Profit de las ventas de Adidas en Estados Unidos a partir de datos históricos de ventas, productos, precios, regiones y canales de venta.

El objetivo no es solo construir un modelo predictivo preciso, sino también generar insights de negocio accionables y desplegar el modelo en producción mediante una API con FastAPI.

## **Problema a resolver**

El beneficio operativo es un indicador clave de rentabilidad empresarial. En este proyecto se busca:

* Predecir el Operating Profit a partir de variables de ventas
* Identificar los factores que más influyen en la rentabilidad
* Evitar data leakage en variables relacionadas con el target
* Comparar modelos lineales y no lineales
* Traducir las predicciones en decisiones de negocio

## **Dataset**

El dataset contiene información de ventas de Adidas en EE. UU. e incluye:

* Retailer y ubicación (State, City, Region)
* Producto y categoría
* Precio por unidad y unidades vendidas
* Total Sales, Operating Profit, Operating Margin
* Método de venta (tienda física o online)

Se eliminaron variables que inducían data leakage, como Total Sales y Operating Margin, y se realizaron transformaciones para variables derivadas (log_units, sales_ratio) que facilitan la predicción sin filtrar información directa del target.

## Pipeline de Machine Learning

El proyecto sigue un pipeline estructurado en Scikit-Learn:

**Feature Engineering**
* Variables temporales (mes, año, día de la semana)
* Estacionalidad (temporada alta, fines de semana)
* Variables de interacción (precio × unidades)
* Transformaciones logarítmicas

**Modelos utilizados**
* Regresión Lineal
* Ridge / Lasso
* Random Forest Regressor (modelo final)

## **Resultados principales**

*Técnicos*

* Los modelos lineales explican un 93–94 % de la varianza, mostrando relaciones lineales claras.
* Random Forest alcanza R² ≈ 0.999, capturando relaciones no lineales e interacciones complejas.

Las variables más importantes son:
* Units Sold / log_units (volumen de ventas)
* Price per Unit (precio)
* sales_ratio (estructura del dataset)
* Variables geográficas y categóricas (ciudad, estado, tipo de producto y canal).

*De negocio* 

* El beneficio operativo depende principalmente de volumen y precio, permitiendo optimizar estrategias de ventas y precios.
* Diferencias por región y canal ofrecen oportunidades para ajustar estrategias locales.
* El modelo proporciona información confiable para planificación de stock, políticas de precios y detección de oportunidades o riesgos.

## **Conclusión**

Este proyecto combina rigor técnico y utilidad de negocio. Se demuestra que:

* Los modelos basados en árboles, especialmente Random Forest, ofrecen la mejor capacidad predictiva.
* El beneficio operativo está fuertemente determinado por un conjunto reducido de variables de alto impacto.
* La metodología desarrollada permite predecir el Operating Profit con alta precisión y generar insights estratégicos para la toma de decisiones.

## API de predicción (producción)

El modelo ha sido desplegado como una API REST usando:

* FastAPI
* Gunicorn
* Render

**URL base**
```
https://ml-adidas-supervisado.onrender.com
```

**Ejemplo de predicción**

Puedes probar la API directamente desde herramientas como Postman o curl enviando peticiones al endpoint `/predict`:

*Predicción de cliente*
```
POST /predict
```

*Ejemplo de entrada:*
```
{
  "Price per Unit": 50,
  "Units Sold": 10,
  "Retailer": "Walmart",
  "Region": "West",
  "State": "California",
  "City": "Los Angeles",
  "Product": "Shoes",
  "Sales Method": "Online",
  "Invoice Date": "2024-01-15"
}
```

*Salida:*
```
{
  "prediction_operating_profit": 3.52,
  "level": "bajo",
  "insight": "Rentabilidad baja",
  "recommendations": [
    "Revisar precio del producto",
    "Reducir costes o mejorar margen",
    "Analizar canal de venta"
  ]
}
```
La API devuelve tanto la predicción numérica del beneficio operativo como una interpretación de negocio (nivel de rentabilidad, insight y recomendaciones accionables), facilitando su uso por perfiles no técnicos.

## **Tecnologías utilizadas**

| Librería | Versión | Uso |
|---|---|---|
| `pandas` | 2.0+ | Manipulación y análisis de datos |
| `numpy` | 1.24+ | Operaciones numéricas |
| `matplotlib` | 3.7+ | Visualización |
| `seaborn` | 0.12+ | Visualización estadística |
| `scikit-learn` | 1.3+ | Preprocesado, modelos y métricas |
| `xgboost` | 2.0+ | Modelo principal |
| `joblib` | 1.3+ | Persistencia del modelo |

## **Estructura del proyecto**

```
├── data/
│   └── Adidas_US_Sales_Datasets.xlsx  
├── models/
│   └── adidas_pipeline.pkl                     
├── notebooks/
│   └── ML_Adidas  
├── src/
│   └── __init__.py 
│   └── pipeline.py 
├── .gitattributes
├── .gitignore
├── main.py
├── README.md                          
└── requirements.txt 
```

## **Instalación**

Clonar el repositorio:

```
git clone https://github.com/tu-usuario/tu-repo.git
```

Acceder al proyecto:
```
cd ML_Adidas
```

Instalar las dependencias:
```
pip install -r requirements.txt
```
## Autora
| Rebeca Prior | [@rebecaprg](https://github.com/rebecaprg) |




