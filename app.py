from analysis.kpi import calculate_kpis
from analysis.country_analysis import country_analysis
from analysis.operator_analysis import operator_analysis
from analysis.error_analysis import (
    load_logs,
    load_error_master,
    top_errors,
    get_error_details,
)

from reports.report_builder import generate_report

from ai.vector_store import VectorStore
from ai.rag_engine import RAGEngine

from ai.prompt_builder import build_prompt
from ai.ai_engine import generate_summary


def main():

    print("=" * 70)
    print(" TELECOM AI TRAFFIC ANALYZER ")
    print("=" * 70)

    # ==================================================
    # Load Data
    # ==================================================

    logs_df = load_logs("data/logs.csv")

    error_df = load_error_master(
        "data/error_codes.csv"
    )

    print("\n✅ Logs Loaded Successfully")
    print(logs_df.head())

    print("\n✅ Error Master Loaded Successfully")
    print(error_df.head())

    # ==================================================
    # Build Knowledge Base
    # ==================================================

    print("\n" + "=" * 70)
    print("BUILDING TELECOM KNOWLEDGE BASE")
    print("=" * 70)

    vector_db = VectorStore()

    vector_db.build_vector_db(error_df)

    # ==================================================
    # KPI Analysis
    # ==================================================

    overall = calculate_kpis(logs_df)

    country = country_analysis(logs_df)

    operator = operator_analysis(logs_df)

    # ==================================================
    # Error Analysis
    # ==================================================

    print("\n" + "=" * 70)
    print("TOP ERROR CODES")
    print("=" * 70)

    error_summary = top_errors(logs_df)

    print(error_summary)

    # ==================================================
    # Error Details
    # ==================================================

    print("\n" + "=" * 70)
    print("DETAILS OF ERROR CODE : 005")
    print("=" * 70)

    details = get_error_details("005", error_df)

    if details is not None:
        print(details)
    else:
        print("Error Code Not Found")

    # ==================================================
    # Report Generation
    # ==================================================

    report = generate_report(
        overall,
        country,
        operator
    )

    print("\n" + "=" * 70)
    print("DAILY REPORT")
    print("=" * 70)

    print(report)

    with open(
        "daily_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print("\n✅ Report Saved Successfully")

    # ==================================================
    # AI Executive Summary
    # ==================================================

    print("\n" + "=" * 70)
    print("AI EXECUTIVE SUMMARY")
    print("=" * 70)

    try:

        summary_prompt = build_prompt(report)

        summary = generate_summary(summary_prompt)

        print(summary)

    except Exception:

        print("\nAI Summary could not be generated.")

    # ==================================================
    # Telecom Operations Copilot
    # ==================================================

    print("\n" + "=" * 70)
    print("TELECOM OPERATIONS COPILOT")
    print("=" * 70)

    question = input(
        "\nAsk your telecom question : "
    )

    rag = RAGEngine()

    # False = Offline SOP
    # True = AI Enhanced

    result = rag.answer_question(
        question,
        ai_enabled=False
    )

    print("\nMode :", result["mode"])

    if result["mode"] == "offline":

        print("\nRetrieved SOP\n")

        print(result["context"])

    else:

        print("\nAI Explanation\n")

        print(result["answer"])

        print("\nKnowledge Source\n")

        print(result["context"])


if __name__ == "__main__":
    main()