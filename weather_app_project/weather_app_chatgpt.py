import tkinter as tk
import requests

class WeatherApp(tk.Tk):
    def __init__(self, api_key):
        super().__init__()
        self.title("Weather App")
        self.columnconfigure(0, weight=1, minsize=600)
        self.rowconfigure(1, minsize=600, weight=1)

        self.api_key = api_key

        self.setup_ui()

    def setup_ui(self):
        frm_search = tk.Frame(self, border=1, relief="raised")
        frm_search.grid(column=0, row=0, sticky="nesw")
        frm_search.columnconfigure(1, pad=10, weight=1, minsize=400)
        frm_search.rowconfigure(0, weight=1, pad=10)

        lbl_location = tk.Label(frm_search, text="Location:", font=("Arial", 18))
        self.ent_search = tk.Entry(frm_search, width=20, justify="center", font=("Arial", 25))
        btn_search = tk.Button(frm_search, text="Search", font=("Arial", 18), command=self.get_weather)
        
        lbl_location.grid(column=0, row=0, padx=10, pady=10)
        self.ent_search.grid(column=1, sticky="ew", row=0, padx=10, pady=10)
        btn_search.grid(column=2, row=0, padx=10, pady=10)

        self.frm_measurements = tk.Frame(self, relief="flat")
        self.frm_measurements.grid(column=0, row=1, sticky="ew", pady=10)

    def get_weather(self):
        city = self.ent_search.get()
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
        }

        response = requests.get(base_url, params=params)
        weather_data = response.json()

        self.frm_measurements.destroy()
        self.frm_measurements = tk.Frame(self, relief="flat")
        self.frm_measurements.grid(column=0, row=1, sticky="ew", pady=10)

        if response.status_code == 200:
            self.display_weather_info(weather_data)
        else:
            self.display_error()

    def display_weather_info(self, weather_data):
        labels_info = [
            ("Temperature", "main", "temp", "°C"),
            ("Humidity", "main", "humidity", "%"),
            ("Wind Speed", "wind", "speed", "m/s"),
            ("Pressure", "main", "pressure", "hPa"),
            ("Precipitation (last hour)", "rain", "1h", "%"),
        ]

        for label, category, attribute, unit in labels_info:
            value = weather_data.get(category, {}).get(attribute, 0)
            self.create_label(f"{label}: {value} {unit}")

    def create_label(self, text):
        label = tk.Label(master=self.frm_measurements, text=text, font=("Arial", 25))
        label.pack(fill="both", expand=2)

    def display_error(self):
        self.create_label("Error: Unable to fetch weather data")

if __name__ == "__main__":
    api_key = "391967c5fd16faf45cf5335badcc3452"
    app = WeatherApp(api_key)
    app.mainloop()
