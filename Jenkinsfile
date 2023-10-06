pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh 'docker build -t my-python-app:$JOB_BASE_NAME.$BUILD_ID .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
		sh 'docker tag my-python-app:$JOB_BASE_NAME.$BUILD_ID timilsinamadhav/my-python-app:$JOB_BASE_NAME.$BUILD_ID'
		sh 'docker push timilsinamadhav/my-python-app:$JOB_BASE_NAME.$BUILD_ID'
            }
        }
    }
}
