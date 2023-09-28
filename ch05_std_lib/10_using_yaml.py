"""
    10_using_yaml.py
    To work with the pyyaml module, it must first be installed.
    Typically, this involves a statement such as pip install pyyaml.

"""
from pathlib import Path
import yaml

yaml_source = Path('./sample.yaml').read_text(encoding='utf-8')
config = yaml.load(yaml_source, Loader=yaml.SafeLoader)          # can also use yaml.safe_load(source)
print(config)

yaml_out = yaml.dump(config)
Path('./yaml_out.yaml').write_text(yaml_out, encoding='utf-8')
print(yaml_out)
