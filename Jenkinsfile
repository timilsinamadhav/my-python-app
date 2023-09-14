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
        stage('Tag and publish') {
            steps {
                echo 'Deploying....'
		sh 'docker tag my-python-app:$JOB_BASE_NAME.$BUILD_ID timilsinamadhav/my-python-app:$JOB_BASE_NAME.$BUILD_ID'
		sh 'docker push timilsinamadhav/my-python-app:$JOB_BASE_NAME.$BUILD_ID'
            }
        }
	stage('deploy') {
            steps {
                echo 'pulling image and deploying on production'
		sh 'ssh -i /var/lib/jenkins/id_rsa -P 2222 vagrant@10.10.14.41 "docker pull timilsinamadhav/my-python-app:$JOB_BASE_NAME.$BUILD_ID"'
		sh 'ssh -i /var/lib/jenkins/id_rsa -P 2222 vagrant@10.10.14.41 "docker run -d -p 1234:80 timilsinamadhav/my-python-app:$JOB_BASE_NAME.$BUILD_ID"'
            }
        }
    }
}
