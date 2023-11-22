#PythonBorrarParcialidadesAsBuilt.py

import pandas as pd
import os

#*****
#***** Estructura completa
#*****
#├───ESTRUCTURA DE CARPETAS DE CADA PARCIALIDAD


#│   ├───DOCUMENTOS ASBUILT 

#       ├───01 PDF
#       │   ├───APROBADOS
#       │   └───OBSERVADOS
#       └───02 EDITABLE
#           ├───APROBADOS
#           └───OBSERVADOS


# Ruta base donde se deben verificar los subdirectorios
ruta_base = 'R:\\01 PARCIALIDADES\\'  

# Nombre del archivo de log
archivo_log = 'R:\\01 PARCIALIDADES\\0000-00 ADMINISTRACION\\LOG\\log_Borrar_DocumentosAsBuilt.txt'

# Planilla con la lista de parcialidades
archivo_excel = 'R:\\01 PARCIALIDADES\\Listado de Parcialidades_AsBuilt.xlsx'

# Lista de carpetas y subcarpetas
estructura = [
            'DOCUMENTOS ASBUILT\\01 PDF\\APROBADOS',
            'DOCUMENTOS ASBUILT\\01 PDF\\OBSERVADOS',
            'DOCUMENTOS ASBUILT\\02 EDITABLE\\APROBADOS',
            'DOCUMENTOS ASBUILT\\02 EDITABLE\\OBSERVADOS',
             ]

# Carga el archivo Excel en un DataFrame Hoja de Parcialidades.
df = pd.read_excel(archivo_excel, sheet_name='PARCIALIDADES')

# Filtra el DataFrame para considerar solo parcialidades a 'PROCESAR' igual a 'S'
df_parcialidades = df[df['PROCESAR'] == 'S']

# Abre el archivo de log en modo de escritura
with open(archivo_log, 'w') as log_file:
    # Itera a través de cada parcialidad y la procesa
    for parcialidad in df_parcialidades['PARCIALIDAD']:
        ruta_subdirectorio = os.path.join(ruta_base, parcialidad)
        log_file.write(f'Parcialidad AS BUILT: {parcialidad}\n')
        # Iterar a través de la estructura y crear carpetas si no existen
        for carpeta in estructura:
            ruta_carpeta = os.path.join(ruta_subdirectorio, carpeta)
            if os.path.exists(ruta_carpeta):
                for f in os.listdir(ruta_carpeta):
                    os.remove(os.path.join(ruta_carpeta, f))
                    log_file.write(f"Borrado AS BUILT: '{os.path.join(ruta_carpeta, f)}'\n")
                print(f"Los archivos de la carpeta AS BUILT '{ruta_carpeta}' han sido borrados.")
                log_file.write(f"Los archivos de la carpeta AS BUILT '{ruta_carpeta}' han sido borrados.\n")
            else:
                log_file.write(f"No existe la carpeta AS BUILT '{ruta_carpeta}'\n")

print("Proceso Borrado AS BUILT finalizado. Los resultados se han guardado en el archivo de log.")
