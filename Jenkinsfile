pipeline {
    agent any

    environment {
        IMAGE = "palshini/assignment5"
        TEST_PORT = "5010"  // new test port
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
                sh "docker rm -f test || true"

                // start container on bridge network
                sh """
                docker run -d --name test \
                -p ${TEST_PORT}:5000 \
                $IMAGE python app.py --host=0.0.0.0 --port=5000
                """

                sh "sleep 12"

                // test via mapped port
                sh "curl -f http://172.17.0.1:${TEST_PORT}/ || (docker logs test && exit 1)"

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
