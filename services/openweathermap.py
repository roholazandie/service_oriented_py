from services.service import Service
from pyowm import OWM

class WeatherService(Service):

    def __init__(self, config=None):
        super().__init__(config)
        api_key = config["api_key"]
        self.owm = OWM(api_key)

    def get_temperature(self, place):
        mgr = self.owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        return str(w.temperature('celsius'))

    def get_wind(self, place='London,GB'):
        mgr = self.owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        return str(w.wind())


if __name__ == "__main__":
    config = {"api_key": "0bfe2759bd3ccd504ed0bcacc31a06d8"}
    ws = WeatherService(config)
    r = ws.get_temperature(place="London,GB")
    print(r)
    r = ws.get_wind()
    print(r)
