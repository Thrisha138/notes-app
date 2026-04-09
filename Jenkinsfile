pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "thrisha138/notes-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'v1', url: 'https://github.com/Thrisha138/notes-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t notes-app:v1 .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat 'echo %PASS% | docker login -u %USER% --password-stdin'
                }
            }
        }

        stage('Tag Image') {
            steps {
                bat 'docker tag notes-app:v1 %DOCKER_IMAGE%:v1'
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker push %DOCKER_IMAGE%:v1'
            }
        }
    }
}
