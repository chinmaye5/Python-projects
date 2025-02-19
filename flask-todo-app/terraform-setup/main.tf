provider "aws" {
  region = "us-east-1"
}

resource "aws_dynamodb_table" "todo_tasks" {
  name           = "todo_tasks"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "task_id"

  attribute {
    name = "task_id"
    type = "S"
  }

  tags = {
    Name        = "dynamodb-table-1"
    Environment = "production"
  }
}

resource "aws_sns_topic" "todo_notifications" {
  name = "todo_notifications"
}

resource "aws_sns_topic_subscription" "user_updates_sqs_target" {
  topic_arn = aws_sns_topic.todo_notifications.arn
  protocol  = "email"
  endpoint  = "programmerpravesh@gmail.com"
}

output "sns_topic_arn" {
    value = aws_sns_topic.todo_notifications.arn
    description = "The ARN of the sns Topic"
}

