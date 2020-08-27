from xmlrpc.server import SimpleXMLRPCServer

from configs import XMLRPCConfig
from services.all_services import AllServices
import yaml

from loader import ClassLoader

class XMLRPCServer:
    def __init__(self, config):
        self.config = config
        self.server = SimpleXMLRPCServer((config.host, config.port), logRequests=True)
        self.prepare()

    def prepare(self):
        loader = ClassLoader()
        for service_name in self.config.services:
            service_config = self.config.services[service_name]
            meta_class = loader.instantiate_class(service_config['classname'])
            setattr(AllServices, service_name, meta_class)
            setattr(AllServices, service_name.lower(), meta_class(service_config))

        self.server.register_instance(AllServices, allow_dotted_names=True)

    def run(self):
        try:
            print("serving...")
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("Existing")


if __name__ == "__main__":
    config = XMLRPCConfig.from_yaml("services_config.yml")
    xmlrpc_server = XMLRPCServer(config)
    xmlrpc_server.run()
