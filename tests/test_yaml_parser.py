from unittest import TestCase
from sef_converter.parser.yaml_parser import YamlParser


class TestYamlParser(TestCase):
    def test__load(self):
        parser = YamlParser(yaml_file="examples/machine/machine-example.yaml")
        self.assertIsNotNone(parser._parameters, "parameters not correctly initialized")

    def test_get_parameter(self):
        parser = YamlParser(yaml_file="examples/machine/machine-example.yaml")
        value = parser.get_parameter("machine_name")
        self.assertIs(type(value), str)
