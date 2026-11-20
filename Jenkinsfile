
pipeline {
    agent any

    stages {

        stage('Source Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully'
            }
        }

        stage('Build and Install Dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Automated Testing') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Deployment Packaging') {
            steps {
                bat 'if exist deployment rmdir /s /q deployment'
                bat 'mkdir deployment'
                bat 'copy app.py deployment\\app.py'
                bat 'copy requirements.txt deployment\\requirements.txt'

                archiveArtifacts artifacts: 'deployment/**',
                                 fingerprint: true

                echo 'Deployment package created successfully'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed! Check the stage logs.'
        }
    }
}
