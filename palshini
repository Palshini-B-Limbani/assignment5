pipeline {
    agent any

    environment {
        IMAGE = "yourdockerhubusername/assignment5"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE ."
            }
        }

        stage('Run Tests') {
            steps {
                sh "docker run -d --name test -p 5000:5000 $IMAGE"
                sh "sleep 5"
                sh "curl -f http://localhost:5000"
                sh "docker rm -f test"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push $IMAGE"
                }
            }
        }
    }
}
