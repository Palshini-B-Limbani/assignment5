pipeline {
    agent any

    environment {
        IMAGE = "palshini/assignment5"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE ./app"
            }
        }

        stage('Run Tests') {
            steps {
                // remove old test container if exists
                sh "docker rm -f test || true"

                // run container WITHOUT using external DB
                sh """
                docker run -d --name test \
                -e DB_HOST=localhost \
                -p 5002:5000 $IMAGE
                """

                // wait for Flask to boot
                sh "sleep 8"

                // call Flask endpoint
                sh "curl -f http://127.0.0.1:5002/ || (docker logs test && exit 1)"

                // cleanup container
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
