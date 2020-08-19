from xmlrpc.server import SimpleXMLRPCServer
from services.all_services import AllServices
import yaml

from loader import ClassLoader

server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)

if __name__ == "__main__":
    try:
        with open('services_config.yml') as file_reader:
            config = yaml.full_load(file_reader)

        loader = ClassLoader()
        for service_name in config['services']:
            service_config = config['services'][service_name]
            meta_class = loader.instantiate_class(service_config['classname'])
            setattr(AllServices, service_name, meta_class)
            setattr(AllServices, service_name.lower(), meta_class(service_config))


        print('Serving...')
        server.register_instance(AllServices, allow_dotted_names=True)

        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")
