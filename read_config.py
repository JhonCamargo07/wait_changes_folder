import json


wait_time_in_seg = 5
command_to_execute = 'echo "File modified"'
showResponseExecutedCommand: True


def read_config():
    path_config_file = './config.json'
    try:

        with open(path_config_file, 'r') as config:
            data = json.load(config)
            wait_time_in_seg = float(data['waitTimeInSeg'])
            command_to_execute = data['commandToExecute']
            showResponseExecutedCommand = data['showResponseExecutedCommand']

    except Exception as e:
        print(f'Error to read configuration file: {e}')
    return wait_time_in_seg, command_to_execute, showResponseExecutedCommand
