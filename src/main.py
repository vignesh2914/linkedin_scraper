import os
import sys
from exception import CustomException
from logger import logging


# this fun responsible for creating folder
def create_folder(folder_name):
    try:
        current_dir = os.getcwd()
        new_folder_path = os.path.join(current_dir, folder_name)
        os.makedirs(new_folder_path, exist_ok=True)
        logging.info("Creating folder done")
        return new_folder_path
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys)



# print(os.getcwd())

# create_folder()