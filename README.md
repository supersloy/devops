# DevOps project: Clock application

The project itself is SPA(Single Page Application) that display current time in Moscow.

## List of main dependencies

- Python3
- flask
- pytest
- Gevent

## Installation

In order to install the project Python3 is required. Instructions how to install it on any OS(operating system) can be find [here](https://realpython.com/installing-python/).

After that clone the repository and navigate into the project folder: 

```shell
git clone https://github.com/supersloy/devops
cd devops
```

Requirements for the project can be installed via requirements file

```shell
cd app_python
pip install -r requirements.txt #Windows
pip3 install -r requirements.txt #Other OS
```

#### Start the project

Program can be easily executed after installation via the command

```shell
#From app_python folder
python app.py #Windows
python3 app.py #Other OS    
```

## Unit tests

#### Run tests

Tests can be executed via the command

```shell
    pytest
```

## Docker

#### Build

```shell
docker build --tag app --target build . #From app_python folder
```

#### Run

```shell
docker run -publish HOST_MACHINE_PORT:5000 app
```

#### Download and run container from dockerhub

```shell
docker pull supersloy/devops
docker run -publish HOST_MACHINE_PORT:5000 supersloy/devops
```

## Author

**Ruslan Muravev BS18SE02**

*mail: r.muravev@innopolis.university*

*telegram: @supersloy*