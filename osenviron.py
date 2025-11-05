import os  # Module provides functions to handle file paths, directories, environment variables
import sys  # Module provides access to Python-specific system parameters and functions

def get_os_environ(os_environ_name, default_value):
    if not os_environ_name in os.environ:
        os.environ.setdefault(os_environ_name, default_value)
    return_value = os.environ[os_environ_name]
    if not os.path.exists(return_value):
        sys.exit("The path " + return_value + " does not exist.")
    print("The path ", return_value, " exists.")
    return return_value

def get_os_environ_path(os_environ_name, os_base_environ_name, default_value_concat):
    default_value = os.path.join(os.environ[os_base_environ_name], default_value_concat)
    return get_os_environ(os_environ_name, default_value)

def sys_path_append(path):
    sys.path.append(path)