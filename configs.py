from dataclasses import dataclass, fields, field, asdict, is_dataclass
import json, yaml
import argparse

@dataclass
class XMLRPCConfig:
    host: str
    port: int
    services: dict

    @classmethod
    def from_json(cls, json_file):
        config_json = json.load(open(json_file))
        return cls(**config_json)

    @classmethod
    def from_yaml(cls, yaml_file):
        config_yaml = yaml.load(open(yaml_file), yaml.FullLoader)
        return cls(**config_yaml)

    def to_argparse(self, **kwargs):
        parser = argparse.ArgumentParser(description=self.__doc__)
        for attr, f in zip(self.__dict__, fields(self)):
            value = self.__dict__[attr]
            value_or_class = f.type
            if f.metadata:
                help = f.metadata['help']
                parser.add_argument("--" + str(attr.replace('_', '-')), default=value, type=value_or_class, help=help)
            else:
                parser.add_argument("--" + str(attr.replace('_', '-')), default=value, type=value_or_class)

        arg = parser.parse_args()
        return arg

    # def __post_init__(self):
    #     if type(self.services) is dict:
    #         self.services = ServicesConfig(**self.services)

    def help(self, f=None):
        if f:
            return {f.name: f.metadata['help'] for f in fields(self) if 'help' in f.metadata}[f]
        else:
            return {f.name: f.metadata['help'] for f in fields(self) if 'help' in f.metadata}


if __name__ == "__main__":
    config = XMLRPCConfig.from_yaml("services_config.yml")
    print(config.host)