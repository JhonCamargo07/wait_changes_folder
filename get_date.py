import os
import sys
import time
import datetime


def get_last_modified_date(folder_path):
    last_modified_date_by_file = {}

    for file in os.listdir(folder_path):
        try:
            # Obtener la información del archivo
            file_stat = os.stat(os.path.join(folder_path, file))

            # Obtener el timestamp de la última modificación del archivo
            last_modified_timestamp = file_stat.st_mtime

            # Convertir el timestamp a una fecha legible
            last_modified_date = datetime.datetime.fromtimestamp(last_modified_timestamp)

            last_modified_date_by_file.setdefault(file, last_modified_date)

        except FileNotFoundError:

            print(f"El archivo '{folder_path}' no existe.")
            return None

        except Exception as e:

            print(f"Error al obtener la fecha de modificación: {str(e)}")
            return None

    return last_modified_date_by_file


try:
    print('Watching for changes. Press Ctrl + C to stop.')

    while True:
        folder_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

        # Obtener la última fecha de modificación
        first_last_modified_date_files = get_last_modified_date(folder_path)
        time.sleep(5)
        second_last_modified_date_file = get_last_modified_date(folder_path)

        for (key_first, value_first), (key_second, value_second) \
                in zip(first_last_modified_date_files.items(), second_last_modified_date_file.items()):
            if key_first != key_second:
                print(f'Cambió el archivo {key_first}')
                break
            if value_first != value_second:
                print(f'Cambió el archivo {key_first}')
                break

except KeyboardInterrupt as e:
    print("Gracias por utilizar este programa")
