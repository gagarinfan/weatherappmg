pipeline {
  agent {
    label 'master'
  }
  stages {
    stage('checkout SCM') {
      steps {
        checkout scm
      }
    }
    stage('Build image') {
      steps {
        script {
          image = docker.build("weatherappmg:${env.BUILD_NUMBER}")
        }

      }
    }
    stage('Test image') {
      steps {
        script {
          image.inside {
            sh 'echo Passed'
          }
        }

      }
    }
    stage('Kill older one') {
      steps {
        script {
          sh 'check=$(docker ps -q); if [[ $check ]]; then docker kill $check; echo Deleted; exit 0; else exit 0; fi'
        }
      }
    }
    stage('Run image') {
      steps {
        script {
          docker.image("weatherappmg:${env.BUILD_NUMBER}").run()
        }

      }
    }
    stage('Email notification') {
      steps {
        emailext(subject: 'WeatherAppMG Notification', body: 'The newest app version: weatherappmg:$BUILD_NUMBER has just been released!\n\nBest regards, Jenkins', from: 'FROM', to: 'TO')
      }
    }
  }
}