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