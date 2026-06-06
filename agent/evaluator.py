import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# evaluate the idea and return scores
def evaluate_idea(idea: str):
    prompt = f"""You are an expert business analyst. Evaluate the following idea and return a JSON response only.

Idea: {idea}

Rate the idea on these 3 criteria from 1 to 10:
- feasibility: how easy is it to implement
- impact: how much business value it creates
- cost: how affordable it is (10 = very cheap, 1 = very expensive)

Also provide:
- summary: one sentence summary of the idea
- recommendation: either "Approve" or "Reject"
- reason: one sentence explaining the recommendation

Return only valid JSON like this:
{{
    "feasibility": 8,
    "impact": 7,
    "cost": 6,
    "summary": "...",
    "recommendation": "Approve",
    "reason": "..."
}}"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content