ServiceNow AI Agent
An intelligent agent that evaluates ideas using Groq LLM, scores them automatically, and creates ServiceNow tickets.
What it does
Submit an idea → AI evaluates and scores it → ServiceNow ticket created automatically.
Tech Stack

Python - Core language
Groq LLM - Fast LLM inference for idea evaluation
ServiceNow REST API - Automatic ticket creation
Streamlit - Frontend dashboard

How it works

User submits an idea
Groq LLM evaluates the idea on feasibility, impact and cost
Each criteria is scored from 1 to 10
Overall score is calculated
Recommendation is generated - Approve or Reject
ServiceNow incident ticket is created automatically

Project Structure
servicenow-agent/
agent/
evaluator.py - Groq LLM idea evaluation and scoring
servicenow.py - ServiceNow REST API ticket creation
frontend/
app.py - Streamlit dashboard
.env - API keys not included in repo
requirements.txt
README.md
Setup
git clone https://github.com/NaveenDataEngineer/servicenow-agent.git
cd servicenow-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Create a .env file:
GROQ_API_KEY=your_groq_api_key
SNOW_INSTANCE=https://your-instance.service-now.com
SNOW_USERNAME=admin
SNOW_PASSWORD=your_password
Run
streamlit run frontend/app.py
Open http://localhost:8501 in your browser
Use Cases

Evaluate new product ideas automatically
Score innovation proposals before review meetings
Auto create IT tickets from AI recommendations
Streamline idea management workflows

What I learned

Building AI agents with Groq LLM
Integrating ServiceNow REST API for automatic ticket creation
Scoring and evaluating ideas using LLM structured outputs
Building interactive dashboards with Streamlit