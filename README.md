<p align="center">
  <a href="https://github.com/AlexDemure/fastgenerator">
    <a href="https://ibb.co/23v8Qx04"><img src="https://i.ibb.co/23v8Qx04/Frame-1349.png" alt="FastGenerator Logo" border="0"></a>
  </a>
</p>

<p align="center">
  CLI utility for code generation based on a TOML configuration file.
</p>

---

## Installation

```sh
pip install fastgenerator
```

## Usage

Run the code generation process:

```sh
fastgenerator -f {config-file.toml}
```

---

## Configuration File Guide

| Section   | Format                      | Description                                                                |
|-----------|-----------------------------|----------------------------------------------------------------------------|
| `workdir` | `""`                        | Uses the current directory                                                |
|           | `"myproject"`                | Uses the current directory + `/myproject`                                 |
|           | `"/home/myproject"`          | Uses an absolute path                                                     |
| `exclude` | `["src/static/__init__.py"]` | Uses a relative path to `workdir`. Excludes file creation.                 |
| `folders` | `["src/", "src/static"]`     | Uses a relative path to `workdir`. Describes directories to be created.   |
| `[[files]]` |                             | Defines file creation rules                                               |
|           | `mode = "a"`                 | File writing mode: `"a"` (append), `"w"` (overwrite)                      |
|           | `path = "src/__init__.py"`   | Uses a relative path to `workdir`. File location                          |
|           | `content = """ ... """`      | File content                                                              |

---

## Using Dynamic Variables in the Configuration File

Example configuration file:

```toml
[[files]]
path = "src/endpoints/http/openapi/{{name.snake}}/__init__.py"
content = """
print("Hello, {{name}}!")
"""
```

When the generator runs, it will automatically detect all variables (e.g., `{{name}}`) and prompt the user to input values.

Each variable, such as `{{name}}`, supports multiple case formats:

| Variable Name | Format          | Example Value |
|--------------|-----------------|---------------|
| `name`       | `{{name}}`       | user          |
|              | `{{name.lower}}` | user          |
|              | `{{name.upper}}` | USER          |
|              | `{{name.title}}` | User          |
|              | `{{name.snake}}` | user          |
|              | `{{name.kebab}}` | user          |
|              | `{{name.pascal}}`| User          |

The tool automatically substitutes values for the specified placeholders in the generated files.