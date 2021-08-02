# Description of machine format

A SEF machine consists of the following parameters and definitions:

| variable | type | description | example values |
| ---      | ---  | :---         | :--- |
| _machine_name_ | `string` | name of machine | `"sef_machine"` |
| _machine_id_ | `int` | unique identifier integer | `0`, `1` |
| _i_axis_ <br>- _limits_: _min_val_, _max_val_ <br>- _velocities_: _min_vel_, _max_vel_ | `float` [m], [m/s] | information about axis `i` in terms of minimum and maximum distance to travel with minimum and maximum velocity. Standard values for `i={x,y,z}` with the `xy`-plane parallel to ground. | `0.0, 1.0, 0.01, 0.5` with distance in meters and velocity in meters per second.