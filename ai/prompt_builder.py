def build_prompt(report, report_type="Daily"):

    prompt = f"""
Below is the {report_type} Telecom Report.

{report}

Based on the above report, provide:

1. Executive Summary
2. Key Observations
3. Root Cause Analysis
4. Impacted Countries and Operators
5. Business Impact
6. Recommendations
7. Overall Health Status

Highlight countries or operators with low delivery percentage or high failure percentage.
If everything is normal, mention that the traffic is healthy.
Keep the report concise and suitable for customer communication.
"""

    return prompt


def build_rag_prompt(question, context):

    prompt = f"""
You are an experienced Telecom Technical Support Engineer.

Use ONLY the information provided below.

Context:

{context}

--------------------------------------

Question:

{question}

--------------------------------------

Instructions:

1. Answer in simple language.
2. Explain the issue.
3. Mention the possible cause.
4. Suggest the resolution.
5. Do not make up information.
"""

    return prompt