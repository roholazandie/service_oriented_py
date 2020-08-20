from services.service import Service
from pyowm import OWM

class WeatherService(Service):

    def __init__(self, config=None):
        super().__init__(config)
        api_key = config["api_key"]
        self.owm = OWM(api_key)

    def get_temperature(self, place):
        observation = self.owm.weather_at_place(place)
        print("observation: {}".format(observation))
        w = observation.get_weather()
        print("w: {}".format(w))
        return str(w.get_temperature(unit='fahrenheit')['temp'])

    def get_wind(self, place='London,GB'):
        mgr = self.owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        return str(w.wind())


if __name__ == "__main__":
    config = {"api_key": ""}
    ws = WeatherService(config)
    r = ws.get_temperature(place="London,GB")
    print(r)
    r = ws.get_wind()
    print(r)
