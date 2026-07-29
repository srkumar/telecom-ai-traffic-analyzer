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
