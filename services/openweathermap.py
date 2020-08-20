from pyowm import OWM

try:
    from services.service import Service
except Exception:
    from service import Service

class WeatherService(Service):

    def __init__(self, config=None):
        super().__init__(config)
        api_key = config["api_key"]
        self.owm = OWM(api_key)

    def get_temperature(self, place):
        observation = self.owm.weather_at_place(place)
        w = observation.get_weather()
        return str(w.get_temperature(unit='fahrenheit')['temp'])

    def get_status(self, place="Denver, USA"):
        observation = self.owm.weather_at_place(place)
        weather = observation.get_weather()
        message = self.create_status_message(str(weather.get_status()))
        return message

    def create_status_message(self, weather, place):
        if weather == "Clouds":
            return "cloudy weather"
        elif weather == "Clear":
            return "clear skies are"
        else:
            return str(weather.get_status()) + " is"


if __name__ == "__main__":
    config = {"api_key": "b42dab02ba31304c08ae33bd9c63d0a4"}
    ws = WeatherService(config)
    london = "London, GB"
    denver = "Denver, USA"
    r = ws.get_temperature(place=denver)
    print("It is currently {} degrees fahrenheit in {}".format(r, denver))
    r = ws.get_status()
    print(r)