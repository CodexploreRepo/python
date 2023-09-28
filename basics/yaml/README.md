# YAML

## Read YAML file
### PyYAML
- Install: `pip install pyyaml`

- `yaml.load_all(file, Loader=yaml.FullLoader)` load multiple yaml docs
- `yaml.safe_load(file)` load the yaml in a safe manner
### `ruamel.yaml`
- Install: `pip install ruamel.yaml`
- `typ='safe'` to achieve `safe_load()`
```Python
from ruamel.yaml import YAML

yaml=YAML(typ='safe')   # default, if not specfied, is 'rt' (round-trip)
yaml.load(doc)

# set identation
yaml = YAML()
yaml.indent(mapping=4, sequence=6, offset=3)
yaml.load(doc)
```

## Define YAML

- List:

```yaml
item:
  - apple
  - oragnge
  - banana
# {'item': ['apple', 'oragnge', 'banana']}
```

### Anchor & Alias

```yaml
age: &age 22
# Anchors (&) & Alias (*)
person_a: &person_a
  name: Harry Potter
  age: *age_anchor
  occupation: Software Engineer
person_a_copy: *person_a
person_b:
  <<: *person_a # <<: create merging of mapping (put whatever mapping on &person_a)
  name: Stacy # overwrite the mapping of &person_a
  age: 12 # overwrite the mapping of &person_a

```
