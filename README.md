<p align="center">
  <a href="https://github.com/AlexDemure/fastgenerator">
    <a href="https://ibb.co/23v8Qx04"><img src="https://i.ibb.co/fdk85fVw/Frame-1349.png" alt="Frame-1349" border="0" /></a>
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
fastgenerator -f {config.toml}
```


## Configuration File Guide

Fastgenerator uses a structured TOML configuration file to define the project structure, file contents, and commands to execute.

### General Structure

```toml
workdir = "myproject"

folders = []

exclude = []

[[files]]
path = "{{name}}.py"
content = """
def hello():
    print("Hello", {{name}})

if __name__ == '__main__':
    hello()
"""

[[scripts]]
command = "isort {{workdir}}"
check = true
```

### Sections Overview

| Section       | Format                          | Description                                                             |   |   |
|---------------|---------------------------------|-------------------------------------------------------------------------|---|---|
| `workdir`     | `""`                            | Uses the current directory                                              |   |   |
|               | `"myproject"`                   | Uses the current directory + `/myproject`                               |   |   |
|               | `"/home/myproject"`             | Uses an absolute path                                                   |   |   |
| `exclude`     | `["src/static/__init__.py"]`    | Uses a relative path to `workdir`. Excludes file creation.              |   |   |
| `folders`     | `["src/", "src/static"]`        | Uses a relative path to `workdir`. Describes directories to be created. |   |   |
| `[[files]]`   |                                 | Defines file creation rules                                             |   |   |
|               | `mode = "a"`                    | File writing mode: `"a"` (append), `"w"` (overwrite)                    |   |   |
|               | `path = "src/__init__.py"`      | Relative to workdir, specifies file location.                           |   |   |
|               | `""" ... """ / path / url`      | Raw content, local file path, or URL for remote content.                |   |   |
| `[[scripts]]` |                                 | Defines commands to be executed after generation.                       |   |   |
|               | `command = "isort {{workdir}}"` | Command to execute, supports dynamic variables.                         |   |   |
|               | `check = True\False"`           | If true, raises an error if the command fails, otherwise logs output.   |   |   |


## Using Dynamic Variables

Fastgenerator supports dynamic variables in both file paths, contents, and script commands.

```toml
[[files]]
path = "src/{{name}}.py"
content = """
def hello():
    print("Hello, {{name}}!")

if __name__ == '__main__':
    hello()
"""
```

### Supported Variable Formats

When running FastGenerator, it automatically detects placeholders (e.g., {{name}}) and prompts the user to enter values. These variables support multiple case formats:

| Variable Name | Format            | Example Value   |   |   |
|---------------|-------------------|-----------------|---|---|
| workdir       |                   | /home/myproject |   |   |
| `name`        | `{{name}}`        | user            |   |   |
|               | `{{name.lower}}`  | user            |   |   |
|               | `{{name.upper}}`  | USER            |   |   |
|               | `{{name.title}}`  | User            |   |   |
|               | `{{name.snake}}`  | user            |   |   |
|               | `{{name.kebab}}`  | user            |   |   |
|               | `{{name.pascal}}` | User            |   |   |

## Automating Post-Generation Tasks

FastGenerator allows you to execute scripts after generating files. These scripts can perform tasks such as formatting, linting, or additional file modifications.

#### Example
```
[[scripts]]
command = "isort {{workdir}}"
check = true

[[scripts]]
command = "ruff {{workdir}} --fix"
check = false
```

- Commands support dynamic variables.
- If check = true, the execution will fail if the command returns a non-zero exit code.
