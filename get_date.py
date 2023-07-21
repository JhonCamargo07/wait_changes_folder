import os
import sys
import datetime


def get_last_modified_date(folder_path):
    last_modified_date_by_file = {}

    try:
        for file in os.listdir(folder_path):
            # Obtener la información del archivo
            file_stat = os.stat(os.path.join(folder_path, file))

            # Obtener el timestamp de la última modificación del archivo
            last_modified_timestamp = file_stat.st_mtime

            # Convertir el timestamp a una fecha legible
            last_modified_date = datetime.datetime.fromtimestamp(last_modified_timestamp)

            last_modified_date_by_file.setdefault(file, last_modified_date)

    except FileNotFoundError as e:

        print(f'File or folder not found: {e}')
        sys.exit()

    except Exception as e:

        print(f"Error getting modified date: {e}")
        sys.exit()

    return last_modified_date_by_file

