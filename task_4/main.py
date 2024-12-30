import requests
import json
import time
from config.config_files import APIkeys
from check_update import is_data_outdated
import json_parcer


MARS_WEATHER_URL = f'https://api.nasa.gov/insight_weather/?api_key={APIkeys.APIkey}&feedtype=json&ver=1.0'
DATA_FILE_PATH = 'data.json'
LAST_UPDATE_FILE = 'last_update.txt'

def get_nasa_data():
    """
    Fetches data from the NASA Mars Weather API and writes it to a JSON file.

    Returns:
        True if data was fetched and written successfully, False otherwise.
    """
    try:
        response = requests.get(MARS_WEATHER_URL)
        response.raise_for_status() 
        data_json = response.json()
        sol_keys = data_json["sol_keys"] 
        parsed_data = {}

        for sol_key in sol_keys:
            if sol_key in data_json:
                parsed_data[sol_key] = data_json[sol_key]

        json_parcer.write_file(DATA_FILE_PATH, parsed_data)
        
        # Update the timestamp of the last fetch
        with open(LAST_UPDATE_FILE, 'w') as f:
            f.write(str(time.time()))

        return True

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from NASA API: {e}")
        return False

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return False

    except (KeyError, TypeError) as e:
        print(f"Error accessing or processing data: {e}")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


def transform_data(file_name, data_type):
    """
    Transforms data from a JSON file containing a dictionary of dictionaries.

    Args:
        file_name: Path to the JSON file.
        data_type: The type of data to extract (e.g., "temperature", "pressure", "season", "all").

    Returns:
        A dictionary containing the extracted data, where keys are from the original data
        and values are the transformed data for each key (or None if missing data).
    """
    try:
        data = json_parcer.load_data(file_name)
        
        transformed_data = {}
        data_mapping = {
            "temperature": {"min_temp": "AT.mn", "max_temp": "AT.mx", "season": "Season"},
            "pressure": {"min_pressure": "PRE.mn", "max_pressure": "PRE.mx", "season": "Season"},
            "all": {"min_temp": "AT.mn", "max_temp": "AT.mx",
                   "min_pressure": "PRE.mn", "max_pressure": "PRE.mx",
                   "season": "Season"}
        }

        if data_type not in data_mapping:
            print(f"Invalid data_type: {data_type}. Supported types: {list(data_mapping.keys())}")
            return None

        for key, item in data.items():
            try:
                transformed_data[f'{key}-{data_type}'] = {
                    k: item.get(
                        v.split(".")[0], None) 
                    if len(v.split(".")) == 1 else item.get(v.split(".")[0], {}).get(v.split(".")[1], None) 
                    for k, v in data_mapping[data_type].items()
                }
            except (KeyError, IndexError):
                print(f"Error processing item: {item}")
        return transformed_data

    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


def filter_data(data, key, sort_order):
    """
    Filters a dictionary of dictionaries based on a key and value.

    Args:
        data: The dictionary of dictionaries to filter.
        key: The key to filter by.
        value: The value to match for the given key.

    Returns:
        A new dictionary containing only the items that match the filter.
    """
    if sort_order == 'asc':
        sorted_data = dict(sorted(data.items(), key=lambda item: item[1][key]))
    elif sort_order == 'desc':
        sorted_data = dict(sorted(data.items(), key=lambda item: item[1][key], reverse=True))
    else:
        raise ValueError("Invalid sort_order. Supported values: 'asc', 'desc'")

    return sorted_data


def print_mars_data(data, data_type):
    """
    Prints Martian weather data to the console.

    Args:
        data: A dictionary where keys represent Sol numbers and values are dictionaries 
              containing weather data (min_temp, max_temp, min_pressure, max_pressure, season).
        data_type: The type of data to print: 
                   'temperature' for temperature range, 
                   'pressure' for pressure range, 
                   or 'all' for both temperature and pressure.

    Prints the weather data for each Sol, including season, temperature range, 
    and/or pressure range, depending on the specified data_type.
    """
    for key, value in data.items():
        print(f'On Sol {key} is {value["season"]}') 
        if data_type == 'temperature' or data_type == 'all':
            print(f'The temperature ranged from {value["min_temp"]}C to {value["max_temp"]}C')
        if data_type == 'pressure' or data_type == 'all':
            print(f'An atmospheric pressure of {value["min_pressure"]}C to {value["max_pressure"]}C')
        print()


def main():
    if is_data_outdated():
        print("Data is outdated. Fetching new data...")
        if not get_nasa_data():
            print("Failed to fetch new data.")
            return
    data = transform_data(DATA_FILE_PATH, 'temperature')
    if data:
        filtered_data = filter_data(data, 'max_temp', 'asc')
        print_mars_data(filtered_data, 'temperature')
    else:
        print("Failed to fetch or process data.")


if __name__ == "__main__":
    main()