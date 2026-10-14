import sys
import os
import io
import pandas as pd

# 1. Agregar la carpeta 'datos-de-entrada-ml-1472' al path de Python
dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_datos = os.path.abspath(os.path.join(dir_actual, '..', 'datos-de-entrada-ml-1472'))
sys.path.append(dir_datos)

# 2. Importar el archivo dicc_1472.py
import dicc_1472

print("jose solis Machine Learning pandas, NC 1472")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "jose solis Machine Learning pandas, NC 1472"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_1472.datos_panaderias)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Kg_pan_dia)
registrar("3. Estadísticas Generales de la Columna 'Kg_pan_dia'", df['Kg_pan_dia'].describe())

# 4. Ordenar Ascendente por Kg_pan_dia
df_asc_kg = df.sort_values(by="Kg_pan_dia", ascending=True)
registrar("4. Ordenar Ascendente por Kg_pan_dia", df_asc_kg)

# 5. Ordenar Descendente por Variedades
df_desc_variedades = df.sort_values(by="Variedades", ascending=False)
registrar("5. Ordenar Descendente por Variedades", df_desc_variedades)

# 6. Guardar el archivo resultados-ml-1472.md dentro de resultados-1472
carpeta_resultados = os.path.abspath(os.path.join(dir_actual, '..', 'resultados-1472'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-1472.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("jose solis Machine Learning pandas, NC 1472")