pipeline {
    agent {
        docker {
            image 'python:3.8-slim-buster'
        }
    }
    stages {
        stage('Install requirements') {
            steps {
                dir('app_python'){
                    sh '''
                    pip install -r requirements.txt -r devrequirements.txt
                    '''
                }
            }
        }
        stage('Lint') {
            steps {
                dir('app_python'){
                    sh '''
                    pip3 install pylama
                    pylama ./app_python/src
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                dir('app_python'){
                    sh '''
                    pytest
                    '''
                }
            }
        }
    }
}