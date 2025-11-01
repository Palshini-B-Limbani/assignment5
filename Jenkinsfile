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

                // run container (host:5002 -> container:5000)
                sh "docker run -d --name test -p 5002:5000 $IMAGE"

                // wait for container to boot
                sh "sleep 5"

                // test endpoint on host:5002
                sh "curl -f http://localhost:5002"

                // cleanup container after testing
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
