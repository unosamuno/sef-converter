# Description of tool format

A SEF tool consists of the following parameters and definitions:

| variable | type | description | example values |
| ---      | ---  | :---         | :--- |
| _tool_name_ | `string` | name of tool | `"tool1"` |
| _tool_id_ | `int` | unique identifier integer | `0`, `1` |
| _target_offset_ <br> - _translation_ <br> - _rotation_ | `float vectors` [m], [rad] | tool offset to machine flange/mounting point | `[0.05, 0.05, 0.0], [0.0, 0.0, 0.0]` |
| _material_ | `string` | type of ennoblement material | `silk`, `wool` |