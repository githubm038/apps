#!groovy

pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }
    stages {
        stage('Environment preparation')
            steps {
                echo "-=- preparing project environment -=-"
                // Python dependencies
                sh "python -m py_compile add2vals.py calc.py"
            }
        }
        stage('Compile') {
            steps {
                echo "-=- compiling project -=-"
            }
        }
    }
       
