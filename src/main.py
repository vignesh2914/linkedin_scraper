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
    

# this fun is responsible for creating url based on user input
def make_url():
    try:
        job_keyword = input("Enter the job keywords: ")
        location_keyword = input("Enter the location: ")
        date_posted = int(input("Enter the value (1-4): "))

        default_url = {
            1: 'https://www.linkedin.com/jobs/search/?keywords={}&location={}&origin=JOB_SEARCH_PAGE_LOCATION_HISTORY&refresh=true',
            2: 'https://www.linkedin.com/jobs/search/?f_TPR=r2592000&keywords={}&location={}&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true',
            3: 'https://www.linkedin.com/jobs/search/?f_TPR=r604800&keywords={}&location={}&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true',
            4: 'https://www.linkedin.com/jobs/search/?f_TPR=r86400&keywords={}&location={}&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'
        }

        if 1 <= date_posted <= 4:
            default_selected_filter = default_url[date_posted]
            logging.info(f"user selected default url collected - {default_selected_filter}")
            final_url = default_selected_filter.format(job_keyword, location_keyword)
            logging.info(f"final url collected with job and location - {final_url}")
            return final_url
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys)



# print(os.getcwd())

# create_folder()
    
print(make_url())