def generate_report(overall, country, operator, report_type="Daily"):

    report = f"""
====================================================
{report_type.upper()} TELECOM REPORT
====================================================

OVERALL KPI
====================================================

Total Traffic           : {overall["total"]}
Delivered               : {overall["delivered"]}
Failed                  : {overall["failed"]}
Delivery Percentage     : {overall["delivered_percentage"]:.2%}

====================================================
COUNTRY SUMMARY
====================================================

{country["country_summary"].to_string(index=False)}

====================================================
DATE WISE COUNTRY REPORT
====================================================

{country["daily_country_report"].to_string(index=False)}

====================================================
Top 10 COUNTRY REPORT
====================================================


{country["top_traffic"]}


====================================================
Top 10 COUNTRY with high Failure
====================================================


{country["top_failure"]}


====================================================
OPERATOR SUMMARY
====================================================

{operator["operator_summary"].to_string(index=False)}

====================================================
DATE WISE OPERATOR REPORT
====================================================

{operator["daily_operator_report"].to_string(index=False)}

====================================================
END OF REPORT
====================================================
"""

    return report