# YAML

## Read YAML file

- `yaml.load_all(file, Loader=yaml.FullLoader)` load multiple yaml docs
- `yaml.safe_load(file)` load the yaml in a safe manner

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
