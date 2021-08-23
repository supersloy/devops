# Docker best practices

#### Dockerignore file

Dockerignore helps reduce the image size and works similarly to the gitignore file

#### Don’t install unnecessary packages / removing unnecessary dependencies

In order to remove unnecessary packages file with python requirements file was split into requirements.txt file for production build and devrequirements.txt for production

#### Using minified base images

Docker python slim image requires much less space than regular version while providing most of the functionality of the original python image.

#### Minimize the number of layers

Minimizing the number of layers lead to reduction of required instructions and build time in general