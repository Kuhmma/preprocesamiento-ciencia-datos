import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def cargar_dataset(ruta):
    """
    Carga un dataset CSV desde la ruta indicada.
    """
    return pd.read_csv(ruta)

def manejar_nulos(df):
    """
    Rellena valores nulos numéricos con la media y categóricos con la moda.
    """
    for columna in df.columns:
        if df[columna].dtype in ['float64', 'int64']:
            df[columna].fillna(df[columna].mean(), inplace=True)
        else:
            df[columna].fillna(df[columna].mode()[0], inplace=True)
    return df

def eliminar_duplicados(df):
    """
    Elimina filas duplicadas del DataFrame.
    """
    return df.drop_duplicates()

def normalizar_numericas(df):
    """
    Normaliza columnas numéricas al rango [0, 1] usando MinMaxScaler.
    """
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = MinMaxScaler()
    df[columnas_numericas] = scaler.fit_transform(df[columnas_numericas])
    return df

def codificar_categoricas(df):
    """
    Convierte variables categóricas en numéricas con LabelEncoder.
    """
    columnas_categoricas = df.select_dtypes(include=['object']).columns
    le = LabelEncoder()
    for col in columnas_categoricas:
        df[col] = le.fit_transform(df[col])
    return df

def preprocesar_dataset(ruta):
    """
    Aplica todo el preprocesamiento al dataset.
    """
    df = cargar_dataset(ruta)
    df = manejar_nulos(df)
    df = eliminar_duplicados(df)
    df = normalizar_numericas(df)
    df = codificar_categoricas(df)
    return df

if __name__ == "__main__":
    # Ejemplo de uso (puedes cambiar "dataset.csv" por el tuyo)
    ruta = "dataset.csv"
    try:
        df_final = preprocesar_dataset(ruta)
        print("Preprocesamiento completado. Vista previa:")
        print(df_final.head())
    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta}.")
