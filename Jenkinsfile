pipeline {

    agent any

    stages {

        stage('Checkout') {

            steps {

                git branch: 'main',
                    url: 'https://github.com/Amarbiradar107/seleniumEndtoEnd.git'

            }

        }

        stage('Build Docker') {

            steps {

                    sh 'docker compose build'

            }

        }
        stage('Run Tests') {

            steps {

                sh 'docker compose up -d'

            }

        }
        stage('Generate Allure') {

        steps {

            sh '''
            allure generate reports/allure-results \
            -o reports/allure-report \
            --clean
            '''

           }

        }
        stage('Cleanup') {

            steps {

                sh 'docker compose down'

            }

        }
    }
}