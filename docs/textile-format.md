# Description of textile format

A SEF textile/substrate consists of the following parameters and definitions:

| variable | type | description | example values |
| ---      | ---  | :---         | :--- |
| _textile_name_ | `string` | name of textile | `my_textile_1` |
| _textile_id_ | `int` | unique identifier integer | `0`, `1` |
| _type_ | `string` | type of textile | `silk`, `wool`, `cotton` |
| _size_ <br>- width (x) _w_ <br>- height (y) _h_ <br>- thickness _t_ | `float` [m] | dimensions of textile | `[0.2, 0.4, 0.1]` |