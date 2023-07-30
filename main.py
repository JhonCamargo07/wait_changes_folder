import os
import time

def watch_folder(folder_path):
    # Obtener los archivos actuales en la carpeta
    current_files = set(os.listdir(folder_path))

    while True:
        # Obtener los archivos actuales nuevamente
        updated_files = set(os.listdir(folder_path))

        # Comparar si hay cambios en los archivos
        diff = updated_files - current_files

        if diff:
            print("La carpeta {} ha sido modificada.".format(folder_path))
            # Coloca aquí las acciones que deseas realizar cuando detecte un cambio en la carpeta.
            print("Ejecutando comando")

        current_files = updated_files
        time.sleep(1)


if __name__ == "__main__":
    import sys
    folder_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    watch_folder(folder_path)
