**PREDICCIÓN DEL OPERATING PROFIT DE ADIDAS US SALES**

**Descripción del proyecto**

Este proyecto tiene como objetivo desarrollar un workflow completo de Machine Learning para predecir el Operating Profit de las ventas de Adidas en Estados Unidos a partir de datos históricos de ventas, productos, precios, unidades vendidas, región y canal de venta.

Se implementó un flujo estructurado que abarca: limpieza de datos, feature engineering, selección de modelos, optimización de hiperparámetros y evaluación final. El proyecto no solo busca precisión técnica, sino también generar insights de negocio accionables.

**Problema a resolver**

El beneficio operativo es un indicador clave para la rentabilidad de la empresa. El problema consiste en:

* Construir un modelo que prediga el Operating Profit basado en variables históricas de ventas y características de productos.
* Identificar las variables que más impactan en la rentabilidad.
* Garantizar que el modelo no dependa de información derivada del target (evitar data leakage).
* Evaluar modelos lineales y no lineales para seleccionar la mejor estrategia de predicción.
* Generar insights útiles para decisiones comerciales y estratégicas.

**Dataset**

El dataset contiene información de ventas de Adidas en EE. UU. y incluye:

* Retailer y ubicación (State, City, Region)
* Producto y categoría
* Precio por unidad y unidades vendidas
* Total Sales, Operating Profit, Operating Margin
* Método de venta (tienda física o online)

Se eliminaron variables que inducían data leakage, como Total Sales y Operating Margin, y se realizaron transformaciones para variables derivadas (log_units, sales_ratio) que facilitan la predicción sin filtrar información directa del target.


**Resultados principales**

*Técnicos*

Los modelos lineales explican un 93–94 % de la varianza, mostrando relaciones lineales claras.
Random Forest alcanza R² ≈ 0.999, capturando relaciones no lineales e interacciones complejas.
Las variables más importantes son:
Units Sold / log_units (volumen de ventas)
Price per Unit (precio)
sales_ratio (estructura del dataset)
Variables geográficas y categóricas (ciudad, estado, tipo de producto y canal).

*De negocio* 

El beneficio operativo depende principalmente de volumen y precio, permitiendo optimizar estrategias de ventas y precios.
Diferencias por región y canal ofrecen oportunidades para ajustar estrategias locales.
El modelo proporciona información confiable para planificación de stock, políticas de precios y detección de oportunidades o riesgos.

**Conclusión**

Este proyecto combina rigor técnico y utilidad de negocio. Se demuestra que:

* Los modelos basados en árboles, especialmente Random Forest, ofrecen la mejor capacidad predictiva.
* El beneficio operativo está fuertemente determinado por un conjunto reducido de variables de alto impacto.
* La metodología desarrollada permite predecir el Operating Profit con alta precisión y generar insights estratégicos para la toma de decisiones.

**Tecnologías utilizadas**

Python 3
Pandas, NumPy
Scikit-learn
XGBoost
Matplotlib, Seaborn

**Estructura del proyecto**

├── data/
│   └── Adidas_US_Sales_Datasets.xlsx
├── notebooks/
│   └── adidas_sales_analysis.ipynb
├── README.md
└── requirements.txt

