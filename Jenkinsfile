pipeline {
    agent any

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
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
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
