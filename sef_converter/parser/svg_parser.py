import untangle
import numpy as np
from sef_converter.svg.svg_element import SvgRect, SvgEllipse


class SvgParser(object):
    _svg_path = None

    def __init__(self, svg_path: str):
        self._svg_path = svg_path

    def generate_objects(self) -> list:
        object_list = []
        svg_object = untangle.parse(self._svg_path)
        svg_layers = svg_object.svg.g
        # loop over all layers
        for layer in svg_layers:
            for child in layer.children:
                if child._name == "rect":
                    x, y, w, h = float(child["x"]), float(child["x"]), float(child["width"]), float(child["height"])
                    angle = self.get_angle_from_str(param=child["transform"])
                    rect = SvgRect(x=x, y=y, w=w, h=h, angle=angle)
                    object_list.append(rect)
                elif child._name == "ellipse":
                    c_x, c_y, r_x, r_y = float(child["cx"]), float(child["cy"]), float(child["rx"]), float(child["ry"])
                    angle = self.get_angle_from_str(child["transform"])
                    ellipse = SvgEllipse(c_x=c_x, c_y=c_y, r_x=r_x, r_y=r_y, angle=angle)
                    object_list.append(ellipse)
        return object_list

    @staticmethod
    def get_angle_from_str(param) -> float:
        if param is None:
            return 0.0
        else:
            return float(param[param.find("rotate") + len("rotate") + 1:param.find(")")]) / 180.0 * np.pi
