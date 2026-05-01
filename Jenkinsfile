// --- THE BEGINNING (Setup) ---
pipeline {
    agent any 

    stages {
        // --- THE MIDDLE (The actual work) ---
        stage('Install Python Packages') {
            steps {
                // This is like typing in your command prompt
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                // Playwright needs to download Chromium/Firefox to run
                sh 'playwright install --with-deps'
            }
        }

        stage('Run My Tests') {
            steps {
                // This runs your python tests
                sh 'pytest'
            }
        }
    }

    // --- THE END (Cleanup/Results) ---
    post {
        always {
            echo 'The build has finished!'
            // You can add code here to save your test reports later
        }
    }
}
