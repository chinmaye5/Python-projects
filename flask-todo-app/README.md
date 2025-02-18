# Flask To-Do List App

This is a simple Flask-based To-Do List application that allows users to add, complete, and delete tasks. The tasks are stored in AWS DynamoDB, and flash messages are displayed for task actions.

## Features

- Add new tasks
- Mark tasks as completed
- Delete tasks
- Flash messages for task actions

## Prerequisites

1. **AWS Account**: You’ll need an AWS account to set up DynamoDB and configure the AWS CLI.
2. **Python 3.10+**: This project uses Python for its backend logic.
3. **Flask**: A lightweight web framework to create the app.
4. **Boto3**: AWS SDK for Python to interact with DynamoDB.
5. **AWS CLI**: Command line tool for configuring AWS services.

---

## Table of Contents

1. [Installation](#installation)
2. [Setting up DynamoDB](#setting-up-dynamodb)
3. [Configuring AWS CLI](#configuring-aws-cli)
4. [Running the Application](#running-the-application)
5. [File Structure](#file-structure)
6. [Contributing](#contributing)

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Pravesh-Sudha/Python-projects/flask-todo-app.git
   cd flask-todo-app
   ```

2. **Create a Python virtual environment**:

   ```bash
   python3 -m venv flask-env
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     flask-env\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source flask-env/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## Setting up DynamoDB

1. **Create a DynamoDB table named `todo_tasks`**:
   
   To create the DynamoDB table, follow these steps:
   
   - Open the [AWS DynamoDB Console](https://console.aws.amazon.com/dynamodb/).
   - Click on **Create Table**.
   - In the **Table name** field, enter `todo_tasks`.
   - Set **Partition key** as `task_id` with type **String**.
   - Leave the default settings for the rest of the options and click on **Create**.

2. **DynamoDB Table Schema**:
   
   The table schema should have at least the following attributes:
   
   - `task_id` (String) - Partition Key
   - `task_name` (String)
   - `completed` (Boolean)

---

## Configuring AWS CLI

1. **Install AWS CLI** (if not already installed):

   Follow the instructions from the [AWS CLI Documentation](https://aws.amazon.com/cli/).

2. **Configure AWS CLI**:

   Run the following command to configure your AWS CLI:

   ```bash
   aws configure
   ```

   You'll need to provide your:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region name (e.g., `us-east-1`)
   - Default output format (e.g., `json`)

3. **Ensure that DynamoDB permissions are enabled** for the IAM user whose credentials you are using.

---

## Configuring the Application

1. **Update `config.py`**:

   In the `config.py` file, update the following values:

   ```python
   class Config:
       # AWS DynamoDB Configuration
       AWS_REGION = 'us-east-1'  # Set to your AWS region
       DYNAMODB_TABLE = 'todo_tasks'  # Name of your DynamoDB table
   ```

---

## Running the Application

1. **Run the Flask app**:

   Start the Flask development server:

   ```bash
   flask run
   ```

   The application will run on `http://127.0.0.1:5000/`.

2. **Access the To-Do List App**:

   Open your browser and navigate to `http://127.0.0.1:5000/`. You should be able to see the app's user interface, where you can add, complete, and delete tasks.

---

## File Structure

```
flask-todo-app/
│
├── app.py               # Flask app entry point
├── db.py                # DynamoDB connection setup
├── routes.py            # Main routes for task management
├── static/
│   └── style.css        # CSS for styling the UI
├── templates/
│   ├── dashboard.html   # Dashboard (Task Management) page
├── config.py            # Configuration for AWS and app settings
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation (this file)
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Make changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request to the main repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By following this README, you should be able to set up the application, configure DynamoDB, run the Flask app, and use the To-Do List application with the DynamoDB backend.
