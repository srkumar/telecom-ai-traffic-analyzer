import pandas as pd

from kpi import calculate_kpis
from country_analysis import country_analysis
from operator_analysis import operator_analysis
from report_builder import generate_report
from prompt_builder import build_prompt
from ai_engine import generate_summary

def main():

    # Load CSV
    df = pd.read_csv("logs.csv")

    # Analysis
    overall = calculate_kpis(df)
    country = country_analysis(df)
    operator = operator_analysis(df)

    # Build Text Report
    report = generate_report(
        overall,
        country,
        operator
    )

    print(report)

    # Save Report
    with open("daily_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    # ---------- AI (Optional) ----------
    prompt = build_prompt(report)
    ai_report = generate_summary(prompt)
    print(ai_report)


if __name__ == "__main__":
    main()