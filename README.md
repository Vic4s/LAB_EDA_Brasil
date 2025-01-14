# 🔢 Análisis de los Ingresos Públicos en Brasil

Este proyecto realiza un análisis exploratorio de los ingresos públicos recaudados por el gobierno de Brasil entre 2013 y 2021. A través de una limpieza y consolidación de datos, junto con técnicas de visualización, se identifican tendencias, discrepancias y áreas de mejora en la gestión presupuestaria.

## 📂 Estructura del Proyecto

```plaintext
├── datos                      # Archivos de datos brutos (CSV por año)
├── src                        # Módulos de funciones de soporte para EDA
├── consolidacion_datos.ipynb       # Limpieza inicial y consolidación de datos
├── limpieza_datos.ipynb # Análisis Exploratorio de Datos (EDA)
├── visualizacion_datos.ipynb  # Visualización de datos y hallazgos clave
├── README.md                  # Descripción del proyecto
```

## 💻 Instalación y Requisitos

Este proyecto requiere las siguientes dependencias:
- **Python**: Versión 3.8 o superior
- **Librerías**: pandas, numpy, matplotlib, seaborn, Jupyter Notebook


## 📊 Principales Resultados y Conclusiones

1. **Análisis de Tendencias**:
   - La recaudación anual mostró un crecimiento constante a lo largo de los años, con un notable incremento entre 2020 y 2021.
   - Los ingresos mensuales tienen un comportamiento estacional, con un aumento significativo en diciembre, probablemente asociado a actividades económicas de fin de año.

2. **Análisis de Discrepancias**:
   - Las mayores discrepancias entre valores previstos y realizados se observan en la categoría **Receitas de Capital**, destacándose específicamente en fuentes como "Alienação de bens".
   - Las discrepancias son más pronunciadas en años como 2017, indicando posibles problemas de sobreestimación o factores externos que afectaron la recaudación.

3. **Hallazgos Adicionales**:
   - El **Ministerio de Economía** concentra más del 90% de los ingresos recaudados, lo que refleja su papel crítico en la gestión financiera.
   - La **Controladoria-geral da união** fue la entidad con mayores problemas para cumplir sus previsiones, indicando la necesidad de mejorar sus estrategias de gestión.

## 💡 Recomendaciones

- Mejorar la precisión de las previsiones de ingresos en categorías con alta discrepancia, como **Receitas de Capital**, implementando modelos predictivos más robustos.
- Realizar auditorías en entidades con bajos desempeños, como la **Controladoria-geral da união**, para identificar y mitigar problemas estructurales.
- Analizar las variaciones estacionales en los ingresos mensuales para optimizar estrategias de recaudación en períodos clave.

## 🤝 Contribuciones

Agradecemos cualquier contribución que mejore este análisis. Si tienes sugerencias, no dudes en contactarnos.

## 👤 Autor

- GitHub: [Victor Forés](https://github.com/Vic4s)
