from flask import Blueprint, request, redirect, url_for, render_template, flash
from utils import generate_task_id  # Assuming this function is defined in utils.py
import boto3
from config import Config

tasks = Blueprint('tasks', __name__)

# DynamoDB client to interact with the database
dynamodb = boto3.resource('dynamodb', region_name=Config.AWS_REGION)
tasks_table = dynamodb.Table(Config.DYNAMODB_TABLE)

@tasks.route('/')
def home():
    # Fetch tasks from DynamoDB
    response = tasks_table.scan()
    tasks_data = response.get('Items', [])
    return render_template('dashboard.html', tasks=tasks_data)

@tasks.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    if task_name:
        task_id = generate_task_id()
        tasks_table.put_item(
            Item={
                'task_id': task_id,
                'task_name': task_name,
                'completed': False,
            }
        )
        flash('Task added successfully!', 'success')
    return redirect(url_for('tasks.home'))

@tasks.route('/complete/<task_id>', methods=['POST'])
def complete_task(task_id):
    tasks_table.update_item(
        Key={'task_id': task_id},
        UpdateExpression="SET completed = :val",
        ExpressionAttributeValues={':val': True}
    )
    flash('Task marked as completed', 'success')
    return redirect(url_for('tasks.home'))

@tasks.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    tasks_table.delete_item(Key={'task_id': task_id})
    flash('Task deleted successfully!', 'danger')
    return redirect(url_for('tasks.home'))
