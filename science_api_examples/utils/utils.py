import os
import science_api_examples

def get_data_path(file_name=""):
    """

    Args:
        file_name: desired file inside data package

    Returns: string with absolute path to a file inside data package

    """
    parent_dir = os.path.abspath(os.path.dirname(science_api_examples.__file__)) + "/data"

    return os.path.join(parent_dir, file_name)
