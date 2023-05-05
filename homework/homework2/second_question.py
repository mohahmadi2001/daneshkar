"""
module providing celsius_to_fahrenheit function
"""
def celsius_to_fahrenheit(celsius) -> list:
    """
    This function converts Celsius to Fahrenheit
    """
    return (celsius * 9/5) + 32
thermometer = [0, 11, 23, 34, 100]

farenheit = list(map(celsius_to_fahrenheit,thermometer))

print(farenheit)

# def celsius_to_fahrenheit(degree: int | float) ->  float:
  
# deg = map(int,input().split())
