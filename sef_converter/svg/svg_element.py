import matplotlib.patches as patches
import numpy as np
from matplotlib.transforms import Affine2D


class SvgRect(object):
    # x and y coordinate of rectangle
    _x, _y = None, None
    # width and height of rectangle
    _width, _height = None, None
    # rotation angle in rad
    _rot_angle = None

    def __init__(self, x: float, y: float, w: float, h: float, angle: float):
        self._x, self._y = x, y
        self._width, self._height = w, h
        self._rot_angle = angle

    def get_plt_object(self) -> patches.Rectangle:
        return patches.Rectangle((self._x, self._y), self._width, self._height,
                                 # transform=Affine2D().rotate_around(x=0, y=0, theta=self._rot_angle),
                                 linewidth=1, fill=False)


class SvgEllipse(object):
    # x and y coordinates of ellipse center
    _c_x, _c_y = None, None
    # radius in x and y direction of ellipse
    _r_x, _r_y = None, None
    # rotation angle in rad
    _rot_angle = None

    def __init__(self, c_x: float, c_y: float, r_x: float, r_y: float, angle: float):
        self._c_x, self._c_y = c_x, c_y
        self._r_x, self._r_y = r_x, r_y
        self._rot_angle = angle

    def get_plt_object(self) -> patches.Ellipse:
        return patches.Ellipse((self._c_x, self._c_y), 2 * self._r_x, 2 * self._r_y,
                               # transform=Affine2D().rotate_around(x=0, y=0, theta=self._rot_angle),
                               linewidth=1, fill=False)
