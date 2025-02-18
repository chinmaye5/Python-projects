from flask import Flask
from tasks import tasks  # Import the tasks Blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-unique-secret-key'
# Register the tasks Blueprint
app.register_blueprint(tasks, url_prefix='/')