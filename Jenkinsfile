
pipeline {
    agent any

    stages {

        stage('Source Checkout') {
            steps {
                echo 'Source code checked out successfully'
            }
        }

        stage('Build and Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Automated Testing') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Deployment Packaging') {
            steps {
                sh 'rm -rf deployment'
                sh 'mkdir -p deployment'
                sh 'cp app.py requirements.txt deployment/'

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
