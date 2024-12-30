from main import get_nasa_data


if get_nasa_data():
    print("Data fetched and saved successfully!")
else:
    print("Failed to fetch data.")