pipeline {
  agent any
  environment {
  # ubah 'youruser/simple-app' dengan nama kamu dan repo proyek kamu
    IMAGE_NAME = 'youruser/simple-app'
    REGISTRY = 'https://index.docker.io/v1/'
  # ubah 'dockerhub-credentials' dengan credential yang sudah kamu buat 
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        sh 'echo "Mulai build aplikasi"'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          docker.build("${env.IMAGE_NAME}:${env.BUILD_NUMBER}")
        }
      }
    }
    stage('Push Docker Image') {
      steps {
        script {
          docker.withRegistry(env.REGISTRY, env.REGISTRY_CREDENTIALS) {
            def tag = "${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
            docker.image(tag).push()
            docker.image(tag).tag('latest')
            docker.image("${env.IMAGE_NAME}:latest").push()
          }
        }
      }
    }
  }
  post {
    always {
      echo 'Selesai build'
    }
  }
}

pipeline {
  agent any
  environment {
  // ubah 'youruser/simple-app' dengan nama kamu dan repo proyek kamu
    IMAGE_NAME = 'irpan011204/simple-app'
  // ubah 'dockerhub-credentials' dengan credential yang sudah kamu buat 
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        bat 'echo "Build di Windows"'
      }
    }
    stage('Build Docker Image') {
      steps {
        bat """docker build -t ${env.IMAGE_NAME}:${env.BUILD_NUMBER} ."""
      }
    }
    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: env.REGISTRY_CREDENTIALS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          bat """docker login -u %USER% -p %PASS%"""
          bat """docker push ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"""
          bat """docker tag ${env.IMAGE_NAME}:${env.BUILD_NUMBER} ${env.IMAGE_NAME}:latest"""
          bat """docker push ${env.IMAGE_NAME}:latest"""
        }
      }
    }
  }
}