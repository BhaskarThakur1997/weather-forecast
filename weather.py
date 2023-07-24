import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

def get_temperature_by_date(data, target_date):
    for entry in data["list"]:
        if target_date in entry["dt_txt"]:
            return entry["main"]["temp"]
    return None

def get_wind_speed_by_date(data, target_date):
    for entry in data["list"]:
        if target_date in entry["dt_txt"]:
            return entry["wind"]["speed"]
    return None

def get_pressure_by_date(data, target_date):
    for entry in data["list"]:
        if target_date in entry["dt_txt"]:
            return entry["main"]["pressure"]
    return None

def main():
    data = get_weather_data()
    if not data:
        return

    while True:
        print("\nChoose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            target_date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_temperature_by_date(data, target_date)
            if temperature:
                print(f"Temperature on {target_date}: {temperature} K")
            else:
                print("No data found for the given date.")

        elif choice == '2':
            target_date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed_by_date(data, target_date)
            if wind_speed:
                print(f"Wind Speed on {target_date}: {wind_speed} m/s")
            else:
                print("No data found for the given date.")

        elif choice == '3':
            target_date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure_by_date(data, target_date)
            if pressure:
                print(f"Pressure on {target_date}: {pressure} hPa")
            else:
                print("No data found for the given date.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()