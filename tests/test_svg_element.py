from unittest import TestCase
from matplotlib.patches import Ellipse, Rectangle

from sef_converter.svg.svg_element import SvgRect, SvgEllipse


class TestSvgRect(TestCase):
    def test_get_plt_object(self):
        rect = SvgRect(x=0.0, y=0.0, w=1.0, h=1.0, angle=0.5)
        patch = rect.get_plt_object()
        self.assertIs(type(patch), Rectangle)

        ell = SvgEllipse(c_x=1.0, c_y=0.0, r_x=10.0, r_y=2.0, angle=0.0)
        patch = ell.get_plt_object()
        self.assertIs(type(patch), Ellipse)
