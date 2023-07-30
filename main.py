from commans import *
from get_date import *
from read_config import *

wait_time_in_seg, command_to_execute, showResponseExecutedCommand = 5


try:
    print('Watching for changes. Press Ctrl + C to stop.')

    while True:
        folder_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

        one_last_modified_date_files = get_last_modified_date(folder_path)
        time.sleep(wait_time_in_seg)
        two_last_modified_date_files = get_last_modified_date(folder_path)

        print('Commando' + command_to_execute)

        for (key_first, value_first), (key_second, value_second) \
                in zip(one_last_modified_date_files.items(), two_last_modified_date_files.items()):
            if key_first != key_second:
                print(f'File {key_first} modified')
                execute_command_with_response(command_to_execute)
                print(f'Executed command')
                break
            if value_first != value_second:
                print(f'File {key_first} modified')
                execute_command_with_response(command_to_execute)
                print(f'Executed command')
                break

except KeyboardInterrupt as e:
    print("Thanks for using this app.")
