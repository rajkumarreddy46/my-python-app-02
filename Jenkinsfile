pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
       
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover'
            }
        }
    }
    post {
        success {
            script {
                def comment = 'Your pull request is successfully accepted.'
                addGitHubComment(comment)
            }
        }
        failure {
            script {
                def comment = 'Your build has failed. Please check the issues below and update your code.'
                addGitHubComment(comment)
            }
        }
    }
}

def addGitHubComment(String comment) {
    def gitHubToken = credentials('GITHUB_TOKEN')
    def repo = 'rajkumarreddy46/my-python-app-02'
    def pullRequestId = env.CHANGE_ID

    sh """
        curl -H "Authorization: token ${gitHubToken}" \
        -X POST \
        -d "{\\"body\\":\\"${comment}\\"}" \
        https://api.github.com/repos/${repo}/issues/${pullRequestId}/comments
    """
}

