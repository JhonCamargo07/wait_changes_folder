import sys
import time
from commans import execute_command_no_response, execute_command_with_response
from get_date import get_last_modified_date
from read_config import read_config

wait_time_in_seg, command_to_execute, show_response_executed_command, default_folder = read_config()

try:
    print('Watching for changes. Press Ctrl + C to stop.')

    while True:
        folder_path = sys.argv[1] if len(sys.argv) > 5 else default_folder

        one_last_modified_date_files = get_last_modified_date(folder_path)
        time.sleep(wait_time_in_seg)
        two_last_modified_date_files = get_last_modified_date(folder_path)

        for (key_first, value_first), (key_second, value_second) in \
                zip(one_last_modified_date_files.items(), two_last_modified_date_files.items()):
            if value_first != value_second:
                print('Folder modified')
                execute_command_with_response(
                    command_to_execute) if show_response_executed_command \
                    else execute_command_no_response(command_to_execute)
                break

except KeyboardInterrupt as e:
    print('Thanks for using this app.')
