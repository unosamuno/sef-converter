[![test and lint](https://gitlab.switch.ch/rehrler/sef-converter/badges/master/pipeline.svg)](https://gitlab.switch.ch/rehrler/sef-converter/-/commits/master)

# SEF Converter

sandbox for SEF project at HSLU

[[_TOC_]]

## Documentation

see [docs](docs/)

## Installation

1. Clone project to your git folder \
   `git clone https://gitlab.switch.ch/rehrler/sef-converter.git`
2. Install python3-venv \
   `sudo apt-get update && sudo apt-get install python3-venv`
3. Create venv based on [requirements](requirements.txt) \
   `cd sef-converter/` \
   `python3 -m venv env` \
   `source env/bin/activate`
   `pip3 install -r requirements`
4. Run your desired script

## Conventions

### Axis

- `z` axis points in the direction of gravity (towards floor)
- `x` and `y` axis are inline with `x` and `y` axis of machine (see [machine parameters](examples/machine/machine-example.yaml))

### General rules
- Test your code before pushing it to the repository
- Never push directly to the master branch
- Commit frequently your code to your branch
- Create merge requests

### Tests
- Use [unittest](https://docs.python.org/3/library/unittest.html) to test your code

### Formatting
- Use the [editorconfig](.editorconfig) file for formatting the code

