import streamlit as st
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.evaluator import evaluate_idea
from agent.servicenow import create_ticket

st.set_page_config(page_title="ServiceNow AI Agent", page_icon="🤖")

st.title("🤖 ServiceNow AI Agent")
st.write("Submit an idea and let AI evaluate it and create a ServiceNow ticket automatically")

# idea input
idea = st.text_area("Enter your idea", height=150, placeholder="Example: Build a self service portal for employees to reset their own passwords without calling IT helpdesk")

if st.button("Evaluate Idea"):
    if idea:
        with st.spinner("AI is evaluating your idea..."):
            result = evaluate_idea(idea)

        try:
            # parse the json response
            data = json.loads(result)

            # show scores
            st.subheader("Evaluation Results")

            col1, col2, col3 = st.columns(3)
            col1.metric("Feasibility", f"{data['feasibility']}/10")
            col2.metric("Impact", f"{data['impact']}/10")
            col3.metric("Cost", f"{data['cost']}/10")

            # overall score
            overall = round((data['feasibility'] + data['impact'] + data['cost']) / 3, 1)
            st.metric("Overall Score", f"{overall}/10")

            # summary and recommendation
            st.write("**Summary:**", data['summary'])

            if data['recommendation'] == "Approve":
                st.success(f"✅ Recommendation: {data['recommendation']}")
            else:
                st.error(f"❌ Recommendation: {data['recommendation']}")

            st.write("**Reason:**", data['reason'])

            # create servicenow ticket
            st.subheader("ServiceNow Ticket")

            with st.spinner("Creating ServiceNow ticket..."):
                ticket = create_ticket(
                    idea=idea,
                    score=overall,
                    recommendation=data['recommendation'],
                    reason=data['reason']
                )

            if ticket['success']:
                st.success(f"✅ Ticket created: {ticket['ticket_number']}")
                st.write("**Ticket URL:**", ticket['url'])
            else:
                st.error(f"❌ Ticket creation failed: {ticket['error']}")

        except json.JSONDecodeError:
            st.error("AI returned invalid response. Please try again.")
    else:
        st.warning("Please enter an idea first!")