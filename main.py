import numpy as np
import pandas as pd
import yaml
import matplotlib.pyplot as plt
from sef_converter.parser.svg_parser import SvgParser

svg_parser = SvgParser(svg_path="examples/svg/2-layer.svg")
objects = svg_parser.generate_objects()

fig, ax = plt.subplots()
# ax.invert_yaxis()
for my_object in objects:
    patch = my_object.get_plt_object()
    ax.add_patch(patch)

plt.axis("equal")
# plt.tight_layout()
plt.show()
