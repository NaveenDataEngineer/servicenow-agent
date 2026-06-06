import os
import requests
from dotenv import load_dotenv

load_dotenv()

INSTANCE = os.getenv("SNOW_INSTANCE")
USERNAME = os.getenv("SNOW_USERNAME")
PASSWORD = os.getenv("SNOW_PASSWORD")

# create a ticket in servicenow
def create_ticket(idea, score, recommendation, reason):
    url = f"{INSTANCE}/api/now/table/incident"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # build the ticket data
    data = {
        "short_description": f"AI Idea Evaluation: {idea[:80]}",
        "description": f"""
Idea: {idea}

AI Evaluation Results:
- Recommendation: {recommendation}
- Overall Score: {score}/10
- Reason: {reason}

This ticket was created automatically by the ServiceNow AI Agent.
        """,
        "category": "inquiry",
        "urgency": "3",
        "impact": "3",
        "caller_id": USERNAME
    }

    response = requests.post(
        url,
        auth=(USERNAME, PASSWORD),
        headers=headers,
        json=data
    )

    if response.status_code == 201:
        ticket = response.json()["result"]
        return {
            "success": True,
            "ticket_number": ticket["number"],
            "ticket_id": ticket["sys_id"],
            "url": f"{INSTANCE}/incident.do?sys_id={ticket['sys_id']}"
        }
    else:
        return {
            "success": False,
            "error": response.text
        }