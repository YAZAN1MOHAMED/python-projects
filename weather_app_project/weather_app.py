import tkinter as tk
import requests


api_key = "391967c5fd16faf45cf5335badcc3452"

window = tk.Tk()
window.title("Weather app")
window.columnconfigure(0, weight=1, minsize=600)
window.rowconfigure(1, minsize=600, weight=1)


def get_weather(api_key, city):
    city = city.get()
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    frm_measurements = tk.Frame(window, relief="flat")
    frm_measurements.grid(column=0, row=1, sticky="ew", pady=10)

    if response.status_code == 200:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]
        wind_speed = weather_data["wind"]["speed"]
        precipitation = weather_data.get("rain", {}).get("1h", 0)

        lbl_temp = tk.Label(
            master=frm_measurements,
            text=f"Temperature: {temperature}°C",
            font=("Arial", 25),
        )
        lbl_temp.pack()
        lbl_humidity = tk.Label(
            master=frm_measurements, text=f"Humidity: {humidity}%", font=("Arial", 25)
        )
        lbl_humidity.pack()
        lbl_wind = tk.Label(
            master=frm_measurements,
            text=f"Wind Speed: {wind_speed} m/s",
            font=("Arial", 25),
        )
        lbl_wind.pack()
        lbl_pressure = tk.Label(
            master=frm_measurements,
            text=f"pressure: {pressure} hPa",
            font=("Arial", 25),
        )
        lbl_pressure.pack(fill="both", expand=2)
        lbl_precipitation = tk.Label(
            master=frm_measurements,
            text=f"Precipitation (last hour): {precipitation} %",
            font=("Arial", 25),
        )
        lbl_precipitation.pack()
    else:
        print(f"Error: {response.status_code}")
        lbl_temp = tk.Label(master=frm_measurements, text="failed", font=("Arial", 25))
        lbl_temp.pack()


frm_search = tk.Frame(
    window,
    border=1,
    relief="raised",
)
frm_search.grid(column=0, row=0, sticky="nesw")
frm_search.columnconfigure(1, pad=10, weight=1, minsize=400)
frm_search.rowconfigure(0, weight=1, pad=10)


lbl_location = tk.Label(frm_search, text="Location:", font=("Arial", 18))
ent_search = tk.Entry(frm_search, width=20, justify="center", font=("Arial", 25))
btn_search = tk.Button(
    frm_search,
    text="search",
    font=("Arial", 18),
    command=lambda: get_weather(api_key, ent_search),
)
lbl_location.grid(column=0, row=0, padx=10, pady=10)
ent_search.grid(column=1, sticky="ew", row=0, padx=10, pady=10)
btn_search.grid(column=2, row=0, padx=10, pady=10)


window.mainloop()
