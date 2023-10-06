pipeline {
    environment {
        registry = "timilsinamadhav/my-python-app"
        registryCredentials = 'dockerhub_credentials'
        dockerImage = ''
    }
    agent any

    stages {
        stage('Building Image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$JOB_BASE_NAME.$BUILD_ID"
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry( '', registryCredentials ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning Up') {
            steps {
                echo 'Clearing'
                sh "docker rmi $registry:$JOB_BASE_NAME.$BUILD_ID"
            }
        }
    }
}
