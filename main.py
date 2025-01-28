# main.py

from weather_analysis import (
    read_weather_data,
    calculate_average_temperature,
    calculate_total_rainfall,
    find_highest_temperature,
    find_lowest_temperature,
    find_day_with_most_rainfall
)

def weather_analyzer(file_path: str) -> dict:
    """
    Analyzes the weather data and returns a dictionary with nice statistics.

    Parameters:
        file_path (str): The path to the weather data file.
    
    Returns:
        dict: A dictionary containing the calculated statistics includes:
            - average_temperature: float
            - total_rainfall: float
            - highest_temperature: dict with date and temperature
            - lowest_temperature: dict with date and temperature
            - most_rainfall: dict with date and rainfall
    """
    # Read the weather data
    weather_data = read_weather_data(file_path)
    
    # Calculate all statistics
    highest_temp_date, highest_temp = find_highest_temperature(weather_data)
    lowest_temp_date, lowest_temp = find_lowest_temperature(weather_data)
    most_rainfall_date, most_rainfall = find_day_with_most_rainfall(weather_data)
    
    # Return formatted results
    return {
        'average_temperature': round(calculate_average_temperature(weather_data), 2),
        'total_rainfall': round(calculate_total_rainfall(weather_data), 2),
        'highest_temperature': {
            'date': highest_temp_date,
            'temperature': highest_temp
        },
        'lowest_temperature': {
            'date': lowest_temp_date,
            'temperature': lowest_temp
        },
        'most_rainfall': {
            'date': most_rainfall_date,
            'rainfall': most_rainfall
        }
    }

if __name__ == "__main__":
    try:
        file_path = "weather_data.txt"
        results = weather_analyzer(file_path)
        print(results)
    except Exception as e:
        print(f"Error analyzing weather data: {str(e)}")