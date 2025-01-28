# Weather Data Analysis

A Python-based weather data analysis tool that processes historical weather data and provides statistical insights. This project demonstrates file handling, data processing, and statistical analysis in Python.

## Features

- Read and parse weather data from CSV files
- Calculate average temperature
- Track total rainfall
- Identify temperature extremes (highest/lowest)
- Find days with maximum rainfall
- Formatted JSON output for easy data consumption

## Project Structure

```
Weather-Data-Analysis/
│
├── weather_analysis.py   # Core analysis functions
├── main.py              # Main program interface
├── weather_data.txt     # Sample weather data
└── README.md           # Project documentation
```

## Usage

1. Ensure your weather data file follows this format:
```
Date,Temperature,Rainfall
2025-01-01,32,0.1
2025-01-02,30,0.0
...
```

2. Run the analysis:
```python
python main.py
```

3. Example output:
```json
{
  "average_temperature": 31.0,
  "total_rainfall": 0.9,
  "highest_temperature": {
    "date": "2025-01-03",
    "temperature": 35.0
  },
  "lowest_temperature": {
    "date": "2025-01-04",
    "temperature": 28.0
  },
  "most_rainfall": {
    "date": "2025-01-06",
    "rainfall": 0.4
  }
}
```

## Functions

### weather_analysis.py
- `read_weather_data(file_path)`: Reads and parses weather data
- `calculate_average_temperature(data)`: Computes mean temperature
- `calculate_total_rainfall(data)`: Sums total rainfall
- `find_highest_temperature(data)`: Locates highest temperature record
- `find_lowest_temperature(data)`: Locates lowest temperature record
- `find_day_with_most_rainfall(data)`: Identifies day with maximum rainfall

### main.py
- `weather_analyzer(file_path)`: Primary interface for weather analysis

## Technical Details

- Written in Python 3
- Uses only standard library modules
- Implements error handling for file operations
- Includes type hints for better code readability
- Follows PEP 8 style guidelines

## Error Handling

The program includes robust error handling for:
- File not found errors
- Invalid data format
- Type mismatches
- Empty data sets

## Future Improvements

Potential enhancements could include:
- Support for different data formats
- Additional statistical analyses
- Data visualization capabilities
- Command-line interface
- Real-time weather data integration

## Author

Juve Perez

## License

This project is open source and available under the MIT License.
