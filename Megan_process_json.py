

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################


FETCHED_DATA_DIR: str = "Megan_data"
PROCESSED_DIR: str = "Megan_json_processed"

#####################################
# Define Functions
#####################################


def count_laureates_by_category(file_path: pathlib.Path) -> dict:
    """Count the number of laureates per category from a JSON file."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r') as file:

            # Use the json module load() function 
            # to read data file into a Python dictionary
            laureates_dictionary = json.load(file)  
            category_dictionary =  json.load(file)

            # initialize an empty dictionary to store the counts
            category_counts_dictionary = {}

            # people is a list of dictionaries in the JSON file
            # We can get it using the get() method and pass in the key "people"
            prizes_list: list = laureates_dictionary.get("laureates", [])
            prizes_list: list = category_dictionary.get("category", [])

            # For each person in the list, get the craft and count them
            for person_dictionary in prizes_list:  

                # Get the craft from the person dictionary
                # If the key "craft" is not found, default to "Unknown"
                category = category_dictionary.get("category", "Unknown")

                # Update the craft counts dictionary for that craft
                # If the craft is not in the dictionary, initialize it to 0
                # Add 1 to the count for the current craft
                category_counts_dictionary[category] = category_counts_dictionary.get(category, 0) + 1

            # Return the dictionary with counts of astronauts by spacecraft    
            return category_counts_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {} # return an empty dictionary in case of error

def process_json_file():
    """Read a JSON file, count laureates by category, and save the result."""

   
    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "Nobel.json")

    
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "json_laureates_by_category.txt")
    
 
    category_count = count_laureates_by_category(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        
        file.write("Laureates by Category:\n")
        for category, count in category_count.items():
            file.write(f"{category}: {count}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")