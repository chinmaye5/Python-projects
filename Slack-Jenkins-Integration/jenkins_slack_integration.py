import requests
import time
from slack_sdk import WebClient 
from slack_sdk.errors import SlackApiError

# ENV Vars

JENKINS_URL = "http://localhost:8080/job/<Your-Job-Name>/build"
JENKINS_USER = "admin"
JENKINS_API_TOKEN = "<Your-API-Token>"
BUILD_URL = "http://localhost:8080/job/<Your-Job-Name>/lastBuild/api/json"

SLACK_BOOT_TOKEN = "<Your-bot-token>"
SLACK_CHANNEL = "#devops-updates"

def trigger_pipeline():
    print("Triggering the pipeline...")
    response = requests.post(url=JENKINS_URL,
                             auth=(JENKINS_USER, JENKINS_API_TOKEN),
                             )
    if response.status_code == 201:
        print("Pipeline triggered Successfully.")
    else:
        print(f"Failed to trigger Pipeline!, Response's status code {response.status_code}")
        response.raise_for_status()


def get_build_status():
    while True:
        response = requests.get(url=BUILD_URL,
                            auth=(JENKINS_USER,
                            JENKINS_API_TOKEN),)
        if response.status_code == 200:
            build_info = response.json()
            status = build_info.get('result')
            if status:
                return status
            else:
                print("Pipeline is running....")
                time.sleep(10)

        else:
            print(f"Failed to get build info.. Response's status code: {response.status_code}")
            response.raise_for_status()


def send_slack_notification(status):
    client = WebClient(token=SLACK_BOOT_TOKEN)
    try:
        message = f"Pipeline Built Successfully with status: *{status}*"
        response = client.chat_postMessage(channel= SLACK_CHANNEL, text= message)
        print(f"Slack notification sent successfully. Status {response['message'] ['text']}")
    except Exception as e:
        print(f"Notification failed with error: {e}")



if __name__ == "__main__":
    trigger_pipeline()
    status = get_build_status()
    send_slack_notification(status)
