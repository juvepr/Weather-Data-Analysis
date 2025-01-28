# weather_analysis.py

def read_weather_data(file_path: str) -> list:
    """
    Reads weather data from the provided text file and returns it as a list of tuples.
    
    Parameters:
        file_path (str): The path to the weather data file.
    
    Returns:
        List[Tuple(str, float, float)]: A list of tuples where each tuple contains
        the date (str), temperature (float), and rainfall (float).
    """
    weather_data = []
    try:
        with open(file_path, 'r') as file:
            # Skip header line
            next(file)
            # Process each line
            for line in file:
                date, temp, rainfall = line.strip().split(',')
                weather_data.append((date, float(temp), float(rainfall)))
        return weather_data
    except FileNotFoundError:
        raise FileNotFoundError(f"Weather data file not found at {file_path}")
    except ValueError:
        raise ValueError("Invalid data format in weather file")

def calculate_average_temperature(data: list) -> float:
    """
    Calculates and returns the average temperature.
    
    Parameters:
        data (List[Tuple(str, float, float)]): The weather data.
    
    Returns:
        float: The average temperature.
    """
    if not data:
        return 0.0
    temperatures = [temp for _, temp, _ in data]
    return sum(temperatures) / len(temperatures)

def calculate_total_rainfall(data: list) -> float:
    """
    Calculates and returns the total rainfall.
    
    Parameters:
        data (List[Tuple(str, float, float)]): The weather data.
    
    Returns:
        float: The total rainfall.
    """
    if not data:
        return 0.0
    rainfall_values = [rain for _, _, rain in data]
    return sum(rainfall_values)

def find_highest_temperature(data: list) -> tuple:
    """
    Finds the highest temperature and its date.
    
    Parameters:
        data (List[Tuple(str, float, float)]): The weather data.
    
    Returns:
        Tuple[str, float]: A tuple containing the date and temperature.
    """
    if not data:
        return ('', 0.0)
    return max(data, key=lambda x: x[1])[:2]

def find_lowest_temperature(data: list) -> tuple:
    """
    Finds the lowest temperature and its date.
    
    Parameters:
        data (List[Tuple(str, float, float)]): The weather data.
    
    Returns:
        Tuple[str, float]: A tuple containing the date and temperature.
    """
    if not data:
        return ('', 0.0)
    return min(data, key=lambda x: x[1])[:2]

def find_day_with_most_rainfall(data: list) -> tuple:
    """
    Finds the day with the most rainfall and its value.
    
    Parameters:
        data (List[Tuple(str, float, float)]): The weather data.
    
    Returns:
        Tuple[str, float]: A tuple containing the date and rainfall.
    """
    if not data:
        return ('', 0.0)
    date, _, rainfall = max(data, key=lambda x: x[2])
    return (date, rainfall)