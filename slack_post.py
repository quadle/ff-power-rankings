import os
import requests
from dotenv import load_dotenv

load_dotenv()


def post_to_slack(text: str):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        raise RuntimeError("SLACK_WEBHOOK_URL is not set in .env")
    resp = requests.post(webhook_url, json={"text": text})
    resp.raise_for_status()
    return resp
