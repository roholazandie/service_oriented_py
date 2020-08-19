from xmlrpc.client import ServerProxy

from configs import XMLRPCConfig


class XMLRPCClient:

    def __init__(self, config):
        self.config = config
        self.client = ServerProxy(f'http://{config.host}:{config.port}')

    def ask_sentiment(self, text):
        r = self.client.sentimentanalysis.get_sentiment(text)
        return r

    def ask_wikipedia(self, text):
        r = self.client.wikipedia.ask_wikipedia(text)
        return r

    def ask_gpt(self, text):
        r = self.client.gpt2.complete(text)
        return r

    def ask_weather(self, place):
        r = self.client.weather.get_temperature(place)
        return r


if __name__ == "__main__":
    config = XMLRPCConfig.from_yaml("services_config.yml")
    xmlrpcclinet = XMLRPCClient(config)
    print(xmlrpcclinet.ask_gpt("I am going to"))