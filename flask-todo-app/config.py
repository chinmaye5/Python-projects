import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'bhaiyokabhaipraveshbhai')
    AWS_REGION = 'us-east-1'
    DYNAMODB_TABLE = 'todo_tasks'
    SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:624448302051:task-notificatoin'
    EMAIL = "programmerpravesh@gmail.com"