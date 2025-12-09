🚗 **AutoInsights Dashboard**

Dashboard interactivo para el análisis de ventas de  vehículos en EE.UU. , desarrollado con Python + Streamlit y desplegado en la nube usando Render.

**Aplicación desplegada:**

👉 https://autoinsights-dashboard-1.onrender.com


📌 **Descripción del proyecto**

AutoInsights Dashboard es una aplicación web desarrollada para analizar información de  venta de vehículos de manera dinámica e interactiva.
Permite visualizar:

- 📊 Histogramas de distribución

- 📈 Gráficos de dispersión

- 🔍 Exploración interactiva del dataset

El objetivo es demostrar la capacidad de integrar análisis de datos con el desarrollo web, aplicando:

- Creación y gestión de entornos virtuales

- Uso profesional de Streamlit

- Preparación y limpieza de datos

- Despliegue en un servicio cloud (Render)

- Buenas prácticas de documentación

📁 **Estructura del repositorio**


```
AutoInsights_Dashboard/
│
├── app.py
│   Archivo principal de la aplicación Streamlit.  
│
├── data/
│   └── vehicles_us.csv
│       Dataset utilizado por la aplicación.
│
├── notebooks/
│   └── EDA.ipynb
│       Notebook de análisis exploratorio de datos.
│
├── README.md
│   Documentación del proyecto.
│
└── requirements.txt
    Lista de dependencias necesarias para ejecutar la aplicación.
```


⚙️ **Cómo ejecutar el proyecto localmente**

 1️⃣ *Clona el repositorio*

``git clone https://github.com/code-ALX79/AutoInsights_Dashboard.git``
``cd AutoInsights_Dashboard ``


2️⃣ *Crea un entorno virtual*

``python -m venv .venv``

3️⃣ *Activa el entorno virtual*

Windows:

``. ./.venv/Scripts/activate``

Mac/Linux:

``source .venv/bin/activate``


4️⃣ *Instala las dependencias*

``pip install -r requirements.txt``

5️⃣ *Ejecuta la app*

``streamlit run app.py``



🌐 **Despliegue en la nube (Render)**

El proyecto fue desplegado utilizando **Render**, un servicio que permite ejecutar apps de Streamlit directamente desde GitHub.

Pasos clave del despliegue:

**1.** Subir el proyecto a GitHub

**2.** Crear un nuevo *Web Service* en Render

**3.** Configurar:

     - Runtime: Python 3

     - Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

**4.** Agregar archivo ``config.toml`` para desactivar CORS y XSRF

**5.** Conectar el repositorio y desplegar automáticamente


🚀 **Demo del Dashboard**

🔗 **Accede aquí:** https://autoinsights-dashboard-1.onrender.com


🔧 **Tecnologías utilizadas**

**Tecnología**	            **Uso**

*Python 3*	             Procesamiento y análisis de datos

*Pandas*	             Manipulación del dataset

*Streamlit*	             Creación del dashboard interactivo

*Matplotlib*	       Visualizaciones gráficas

*Render*	             Despliegue en producción

*Git + GitHub*	       Control de versiones
 

 💡 **Oportunidades de mejora**

Para quienes quieran ampliar este proyecto, aquí algunas ideas:

🔹 Agregar filtros avanzados por precio, marca o año

🔹 Incorporar modelos de predicción (ej. precio estimado del vehículo)

🔹 Crear un mapa interactivo con ubicación geográfica

🔹 Añadir análisis de correlaciones

🔹 Implementar autenticación para usuarios

🔹 Conectar el dashboard a una API real

🤝 **Contribuciones**

Este proyecto está abierto a la comunidad analítica.
Si quieres mejorarlo:

**1.** Haz un fork

**2.** Crea una nueva rama

**3.** Implementa tus mejoras

**4.** Envía un Pull Request

**5.** Toda contribución es bienvenida 🚀.


🧑‍💻 **Autor**

**Alexander Herrera**

Analista de Datos | Desarrollo Web | Automatización
