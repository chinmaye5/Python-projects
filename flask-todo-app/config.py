import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'bhaiyokabhaipraveshbhai')
    AWS_REGION = 'us-east-1'
    DYNAMODB_TABLE = 'todo_tasks'
<<<<<<< HEAD
    SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:624448302051:task-notificatoin'
    EMAIL = "programmerpravesh@gmail.com"
=======
    SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:624448302051:task-notificatoin'   # Change which your ARN
>>>>>>> d7b1432eab3c17bd4d5776dfa921e557a2072fe1
