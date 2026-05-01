pipeline {
    agent any

    environment {
        PATH = "/Library/Frameworks/Python.framework/Versions/3.13/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                // This pulls your code from GitHub
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Uses your requirements.txt to install playwright, pytest, etc.
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Install Browsers') {
            steps {
                // Essential for Playwright: downloads the actual browser binaries
                sh 'playwright install --with-deps'
            }
        }

        stage('Run Tests') {
            steps {
                // Runs your Python tests
                sh 'pytest'
            }
        }
    }

    post {
        always {
            // This keeps your test results available in Jenkins after the run
            archiveArtifacts artifacts: '**/test-results/**', allowEmptyArchive: true
        }
    }
}
