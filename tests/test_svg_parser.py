from unittest import TestCase

from sef_converter.parser.svg_parser import SvgParser


class TestSvgParser(TestCase):
    def test_generate_objects(self):
        parser = SvgParser(svg_path="examples/svg/2-layer.svg")
        objects = parser.generate_objects()
        self.assertTrue(len(objects) != 0)
