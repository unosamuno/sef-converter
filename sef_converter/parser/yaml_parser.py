import yaml


class YamlParser(object):
    _yaml_file, _parameters = None, None

    def __init__(self, yaml_file: str):
        self._yaml_file = yaml_file
        self._load()

    def _load(self) -> None:
        with open(self._yaml_file) as file:
            self._parameters = yaml.load(file, Loader=yaml.FullLoader)

    def get_parameter(self, key: str):
        if key not in self._parameters.keys():
            raise KeyError(key + " is not a correct key")
        else:
            return self._parameters.get(key)
