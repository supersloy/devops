# CI Best Practices

## General

- Utilize tracking and version control tools

- Utilize on-demand testing environments

- Automate the build and deployment

- Make the build self-testing

- Test in a clone of the production environment

## GitHub

- Keep actions minimal

- Never hardcode secret codes

  Utilize environments, environment protection rules and environment secrets features

- Tag commits

- Utilize pre-commit hooks

  Make linting and testing automated

- Utilize cache when appropriate

  Store dependencies/build cache

## Jenkins

- Utilize Jenkins credentials instead of hardcode secret codes

  Similiar to GitHub environment secrets

- Run unit tests and linters as part of pipeline

- Avoiding very large shared packages

  Use shared libraries in order to achieve that

- Use declarative syntax

- Avoid DiD (Docker in Docker)



