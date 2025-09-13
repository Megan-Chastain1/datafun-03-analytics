<<<<<<< HEAD
=======
# datafun-03-analytics
Creating a GitHub account and repository, and setting up a local project to sync with it, is a standard workflow for developers. Here's a step-by-step guide based on your request.

## 1\. GitHub Account and Repository

  * **Create a GitHub Account:** Go to [github.com](https://github.com) and sign up with your email. Follow the on-screen instructions to create your account.
  * **Create a New Repository:** On your GitHub home page, click the **New** button to create a new repository. Name it **`datafun-01-utils`**. You can add an optional description and choose to make it public or private.
  * **Initialize with a README:** It's a good practice to check the "Add a README file" box. This creates an initial file in your repository, which makes cloning easier.

-----

## 2\. Local Setup and Cloning

  * **Create Your Project Folder:** On your computer, open a file explorer and navigate to your `C:` drive. Create a new folder named `Repos`. The full path will be `C:\Repos`.
  * **Clone the Repository:**
      * Open Visual Studio Code.
      * Go to **Terminal** \> **New Terminal** in the top menu.
      * In the terminal, navigate to your new folder by typing `cd C:\Repos`.
      * Now, clone your repository. **Replace** `youraccount` and `yourrepo` with your actual GitHub username and repository name.
        ```
        git clone https://github.com/youraccount/datafun-01-utils.git
        ```
      * After this command, a new folder named **`datafun-01-utils`** will appear inside your `C:\Repos` folder.

-----

## 3\. Adding and Syncing Files

  * **Add `.gitignore` and `requirements.txt`:**
      * In the VS Code file explorer, open the newly created `datafun-01-utils` folder.
      * Create a new file named **`.gitignore`** (make sure there's a dot at the beginning). This file tells Git to ignore certain files and folders, like your virtual environment.
      * Create another new file named **`requirements.txt`**. This file will list all the Python packages your project depends on.
  * **Sync and Save Changes:** In the VS Code terminal, make sure you are in the `datafun-01-utils` folder (`cd C:\Repos\datafun-01-utils`). Then run the following commands in order:
    ```
    git add .
    git commit -m "Add .gitignore and requirements.txt files"
    git push -u origin main
    ```
      * The `git add .` command stages all your changes.
      * The `git commit` command saves a snapshot of your changes with a descriptive message.
      * The `git push` command uploads your changes from your local repository to the remote one on GitHub.

-----

## 4\. Create a Virtual Environment

  * With your terminal still open and your current directory set to `C:\Repos\datafun-01-utils`, run the following command to create a virtual environment:
    ```
    py -m venv .venv
    ```
  * This command creates a new folder named **`.venv`** in your project directory. This folder contains a local, isolated Python environment where you can install packages for this specific project without affecting your system's global Python installation.

Follow the code below to import different file types from the web

>>>>>>> d9eef215f656214ebfd41e115d684bcca7136a2a
import requests
import pathlib
import json
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define a constant for the fetched data directory
FETCHED_DATA_DIR = "fetched_data"

#####################################
# CSV File Handlers
#####################################

def fetch_csv_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch CSV data from the given URL and write it to a file.
    
    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the CSV file to fetch.
    
    Returns:
        None
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return
    
    try:
        logger.info(f"Fetching CSV data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: CSV file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_csv_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write CSV data to a file.
    
    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): CSV content as a string.
    
    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing CSV data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        logger.info(f"SUCCESS: CSV data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing CSV data to {file_path}: {io_err}")

#####################################
# Excel File Handlers
#####################################

def fetch_excel_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch Excel data from the given URL and write it to a file.
    
    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the Excel file to fetch.
    
    Returns:
        None
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return
    
    try:
        logger.info(f"Fetching Excel data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
        logger.info(f"SUCCESS: Excel file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_excel_file(folder_name: str, filename: str, binary_data: bytes) -> None:
    """
    Write Excel binary data to a file.
    
    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        binary_data (bytes): Binary content of the Excel file.
    
    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing Excel data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            file.write(binary_data)
        logger.info(f"SUCCESS: Excel data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing Excel data to {file_path}: {io_err}")

#####################################
# JSON File Handlers
#####################################

def fetch_json_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch JSON data from the given URL and write it to a file.
    
    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the JSON file to fetch.
    
    Returns:
        None
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return
    
    try:
        logger.info(f"Fetching JSON data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
        logger.info(f"SUCCESS: JSON file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")
    except Exception as e:
        logger.error(f"Error parsing JSON: {e}")

def write_json_file(folder_name: str, filename: str, json_data: dict) -> None:
    """
    Write JSON data to a file.
    
    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        json_data (dict): JSON data to write to the file.
    
    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing JSON data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            json.dump(json_data, file, indent=4)
        logger.info(f"SUCCESS: JSON data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing JSON data to {file_path}: {io_err}")

#####################################
# Text File Handlers
#####################################

def fetch_txt_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch text data from the given URL and write it to a file.
    
    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the text file to fetch.
    
    Returns:
        None
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return
    
    try:
        logger.info(f"Fetching text data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: Text file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_txt_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write text data to a file.
    
    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): Text content to write to the file.
    
    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        logger.info(f"SUCCESS: Data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing to file {file_path}: {io_err}")


#####################################
# Main function to demonstrate fetches
#####################################

def main():
    """ Main function to demonstrate fetching various data files. """
    logger.info("Starting data fetch demonstration...")
    
    # CSV Data
    csv_url = 'example.csv'
    fetch_csv_file(FETCHED_DATA_DIR, "exp.csv", csv_url)
    
    # Excel Data
    excel_url = 'example.xlsx'
    fetch_excel_file(FETCHED_DATA_DIR, "exp.xlsx", excel_url)
    
    # JSON Data
    json_url = 'eample.json'
    fetch_json_file(FETCHED_DATA_DIR, "exp.json", json_url)
    
    # Text Data
    # Replace these with your desired URL and filename.
    generic_txt_url = 'example.txt'
    fetch_txt_file(FETCHED_DATA_DIR, "your_file_name.txt", generic_txt_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
