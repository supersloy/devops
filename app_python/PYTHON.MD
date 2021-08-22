

## Best practices

#### Virtual environment

Virtual environment helps to keep dependencies required by different projects separate by creating isolated environments for them. As venv folder is not required for running the project it is added in `.gitignore` file

#### Requirements file

It helps with installing the project and tracking dependencies

#### Naming conventions

PEP8 standard was used in order to achieve consistency in naming and better code readability for experienced developers

#### Proper layout

Src layout with additional folders for static files and tests lead to better navigation inside the project

#### Utilization of suitable technologies

As the given application does not require connection with databases, high availability for multiple requests simultaneously or hard computation Flask framework is used as it is more suitable for tasks of that degree.