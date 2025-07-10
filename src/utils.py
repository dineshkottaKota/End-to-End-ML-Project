import os
import sys
import pandas as pd
import numpy as np
import dill

from src.exception import CustomException

def save_object(obj, file_path):
    """
    Save an object to a file using pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
    except Exception as e:
        raise CustomException(f"Error saving object to {file_path}: {str(e)}", sys) from e
