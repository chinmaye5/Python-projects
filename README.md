# Python Projects to Kickstart Learning

Welcome to the repository for **3 Python projects** designed to help beginners kickstart their Python programming journey. Each project demonstrates Python's versatility and its application in real-world scenarios, especially for DevOps tasks. 🚀

## Projects Overview

### 1. **Weather App** 🌦️
A Python script that fetches and displays the current weather of a user-provided city using the [WeatherAPI](https://www.weatherapi.com/).

#### Features:
- Takes city name as input.
- Fetches weather details such as temperature, wind speed, and condition.
- Utilizes WeatherAPI to handle data in JSON format.

#### Files:
- `weather.py`

#### Setup:
1. Install the `requests` library:  
   ```bash
   pip install requests
   ```
2. Obtain a free API key from [WeatherAPI](https://www.weatherapi.com/).
3. Replace `<Your_API_KEY>` in the script with your API key.
4. Run the program:  
   ```bash
   python weather.py
   ```

---

### 2. **GitHub Pull Request Tracker** 🔄
A Python script that uses the GitHub API to track pull requests for the `argoproj/argo-cd` repository and displays the contributors.

#### Features:
- Fetches JSON data from GitHub API.
- Filters and displays pull request creators along with the number of PRs they made.
- Utilizes a dictionary to store contributor data.

#### Files:
- `github_pr_tracker.py`

#### Setup:
1. Install the `requests` library:  
   ```bash
   pip install requests
   ```
2. Run the program:  
   ```bash
   python github_pr_tracker.py
   ```

---

### 3. **SlackBot for Jenkins Pipeline** 🤖
A Python script that triggers a Jenkins pipeline and sends the build status to a Slack channel using a Slack bot.

#### Features:
- Triggers a Jenkins pipeline.
- Fetches build status using Jenkins API.
- Sends notifications to a Slack channel using Slack API.

#### Files:
- `jenkins_slack_integration.py`

#### Setup:
1. Install the required libraries:  
   ```bash
   pip install requests slack-sdk
   ```
2. Create a Jenkins pipeline and generate an API token for your Jenkins user.
3. Create a Slack bot, add it to a channel, and generate a bot token.
4. Replace placeholders (`<Your-API-Token>` and `<Your-Bot-Token>`) in the script with your credentials.
5. Run the program:  
   ```bash
   python jenkins_slack_integration.py
   ```

---

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of Python programming.
- API keys for WeatherAPI, GitHub, Jenkins, and Slack (as applicable).

## How to Clone This Repository
1. Clone the repository using Git:
   ```bash
   git clone https://github.com/Pravesh-Sudha/Python-projects.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Python-projects
   ```
3. Start exploring and running the scripts!

## Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy Coding! 🎉

