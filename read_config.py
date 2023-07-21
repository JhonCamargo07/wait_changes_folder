import os
import json
import sys


def read_config():
    wait_time_in_seg = 5
    command_to_execute = 'echo "Hola mundo"'
    show_response_executed_command: True
    default_folder = os.getcwd()
    try:

        with open('./config.json', 'r') as config:
            data = json.load(config)
            wait_time_in_seg = get_value_true(
                float(data['waitTimeInSeg']), wait_time_in_seg)
            command_to_execute = get_value_true(
                data['commandToExecute'], command_to_execute)
            show_response_executed_command = bool(
                data['showResponseExecutedCommand'])
            default_folder = get_value_true(
                data['defaultFolder'], default_folder)

    except Exception as e:

        print(f'Error to read configuration file: {e}')
        sys.exit()
    print(wait_time_in_seg, command_to_execute,
          show_response_executed_command, default_folder)
    return wait_time_in_seg, command_to_execute, show_response_executed_command, default_folder


def get_value_true(value_to_validate, default_value):

    try:
        value_type = type(value_to_validate)
        if value_type.__name__ == 'int' or value_type.__name__ == 'float':
            return value_to_validate if 0 < value_to_validate <= 43200 else default_value

        if value_to_validate != '' and len(value_to_validate) > 5:
            return value_to_validate

        return default_value

    except Exception as e:
        print('Validacion error', e)

    return default_value
