import os
import shutil

directorio = r'C:\especifica\tu\ruta'

extensiones = {

    '.txt': 'Textos',
    '.jpg': 'Imágenes',
    '.png': 'Imágenes',
    '.pdf': 'Documentos',
    '.docx': 'Documentos',
    '.xlsx': 'Documentos',
    '.mp3': 'Musica',
    '.mp4': 'Videos',
    '.zip': 'Comprimidos',
    '.rar': 'Comprimidos',
    '.exe': 'Ejecutables '
}

#Funcion para crear carpetas si no existen

def crear_carpetas(directorio, carpetas):
    for carpeta in carpetas.values():
        carpeta_path = os.path.join(directorio, carpeta)
        if not os.path.exists(carpeta_path):
            os.makedirs(carpeta_path)

#Funcion para mover archivos a sus respectivas carpetas 
def mover_archivos(directorio, extensiones):
    for archivo in os.listdir(directorio):
        if os.path.isfile(os.path.join(directorio, archivo)):
            extension = os.path.splitext(archivo)[1].lower()
            if extension in extensiones:
               carpeta_destino = extensiones[extension]
               carpeta_path = os.path.join(directorio, carpeta_destino)
               shutil.move(os.path.join(directorio, archivo), os.path.join(carpeta_path, archivo))

#Crear carpetas y mover archivos

crear_carpetas(directorio, extensiones)
mover_archivos(directorio, extensiones)

print("Archivos organizados con exito")