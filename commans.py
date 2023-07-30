import subprocess


def execute_command_no_response(command):
    """
    Metodo para ejecutar un comando sin retornar la respuesta
    :param command: Comando a ser ejecutado
    :return:
    """
    subprocess.run(command, shell=True, capture_output=True, text=True)


def execute_command_with_response(command):
    """
    Metodo para ejecutar un comando imprimiendo y retornando la respuesta
    :param command: Comando a ser ejecutado
    :return:
    """
    result_command = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result_command.stdout)
    return result_command
