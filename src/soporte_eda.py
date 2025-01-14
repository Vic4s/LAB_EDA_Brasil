# soporte_eda.py
# Este archivo contiene funciones de soporte para el análisis exploratorio de datos.

import pandas as pd

# Función 1: Renombrar columnas para facilitar el análisis
def traducir_columnas(dataframe, traducciones):
    """Traduce las columnas de un DataFrame según un diccionario de traducciones.

    Args:
        dataframe (pd.DataFrame): El DataFrame que se va a modificar.
        traducciones (dict): Diccionario con traducciones {nombre_original: nombre_traducido}.

    Returns:
        pd.DataFrame: DataFrame con las columnas traducidas.
    """
    return dataframe.rename(columns=traducciones)

# Función 2: Resumen de valores nulos y tipos de datos
def generar_reporte_nulos(dataframe):
    """Genera un informe sobre los valores nulos y tipos de datos en un DataFrame.

    Args:
        dataframe (pd.DataFrame): El DataFrame a analizar.

    Returns:
        pd.DataFrame: DataFrame con el número de valores nulos, porcentaje de nulos y tipo de dato.
    """
    reporte = pd.DataFrame({
        "Numero_nulos": dataframe.isnull().sum(),
        "Porcentaje_nulos": (dataframe.isnull().sum() / len(dataframe) * 100).round(2),
        "Tipo_dato": dataframe.dtypes
    })
    return reporte

# Función 3: Verificar columnas con valores únicos y su distribución
def valores_unicos(dataframe, columna):
    """Devuelve los valores únicos y su frecuencia en una columna específica.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        columna (str): Nombre de la columna a analizar.

    Returns:
        pd.DataFrame: DataFrame con los valores únicos y su porcentaje.
    """
    conteo = dataframe[columna].value_counts()
    return pd.DataFrame({
        "Frecuencia": conteo,
        "% Total": (conteo / len(dataframe) * 100).round(2)
    })

# Función 4: Conversión de valores monetarios a tipo numérico
def convertir_valores_monetarios(dataframe, columnas):
    """Convierte columnas de valores monetarios (en texto) a formato numérico eliminando caracteres no deseados.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene las columnas a convertir.
        columnas (list): Lista de nombres de columnas a procesar.

    Returns:
        pd.DataFrame: DataFrame con las columnas convertidas a formato numérico.
    """
    for columna in columnas:
        dataframe[columna] = (dataframe[columna]
                               .str.replace('.', '', regex=False)
                               .str.replace(',', '.', regex=False)
                               .astype(float))
    return dataframe

# Función 5: Generar informe de rango de fechas
def rango_fechas(dataframe, columna):
    """Genera un rango completo de fechas y verifica cuáles están ausentes en la columna.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        columna (str): Nombre de la columna de fechas.

    Returns:
        pd.DatetimeIndex: Fechas ausentes en el rango completo.
    """
    rango_completo = pd.date_range(dataframe[columna].min(), dataframe[columna].max())
    fechas_presentes = pd.to_datetime(dataframe[columna]).dropna().unique()
    return rango_completo.difference(fechas_presentes)
