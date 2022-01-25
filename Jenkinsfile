#!groovy

pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }
    stages {
        stage('Environment preparation') {stash(name: 'compiled-results', includes: '*.py*')
            steps {
                echo "-=- preparing project environment -=-"
                // Python dependencies
                sh "python -m py_compile add2vals.py calc.py"
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Compile') {
            steps {
                echo "-=- compiling project -=-"
            }
        }
    }      
       
