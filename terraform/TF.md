# Terraform best practices

## Code structure

- Minimize number of resources
- Start project using remote state
- Try to practise a consistent structure and naming convention
- Keep resource modules as plain as possible
- Use shared modules
- Don't hardcode values which can be passed as variables or discovered using data sources
- Use locals to specify explicit dependencies between resources

## Naming conventions

- Use snake case : use underscores and lowercase letters and numbers
- Do not repeat resource type in resource name
- Always use singular nouns for names

Source: https://www.terraform-best-practices.com/