import pandas as pd


def operator_analysis(df):

    # Total Traffic
    total = (
        df.groupby(["date", "operator"])
        .size()
        .reset_index(name="total_traffic")
    )

    # Delivered Traffic
    delivered = (
        df[df["status"] == "Delivered"]
        .groupby(["date", "operator"])
        .size()
        .reset_index(name="delivered")
    )

    # Failed Traffic
    failed = (
        df[df["status"] == "Failed"]
        .groupby(["date", "operator"])
        .size()
        .reset_index(name="failed")
    )

    # Merge Reports
    daily_operator_report = total.merge(
        delivered,
        on=["date", "operator"],
        how="left"
    )

    daily_operator_report = daily_operator_report.merge(
        failed,
        on=["date", "operator"],
        how="left"
    )

    # Replace NaN with 0
    daily_operator_report = daily_operator_report.fillna(0)

    # Percentages
    daily_operator_report["delivery_percentage"] = (
        daily_operator_report["delivered"]
        / daily_operator_report["total_traffic"]
    ) * 100

    daily_operator_report["failed_percentage"] = (
        daily_operator_report["failed"]
        / daily_operator_report["total_traffic"]
    ) * 100

    # Operator Summary (All Dates Combined)
    operator_summary = (
        daily_operator_report
        .groupby("operator", as_index=False)
        .agg(
            {
                "total_traffic": "sum",
                "delivered": "sum",
                "failed": "sum"
            }
        )
    )

    operator_summary["delivery_percentage"] = (
        operator_summary["delivered"]
        / operator_summary["total_traffic"]
    ) * 100

    operator_summary["failed_percentage"] = (
        operator_summary["failed"]
        / operator_summary["total_traffic"]
    ) * 100


    return {
        "operator_summary": operator_summary,
        "daily_operator_report": daily_operator_report
    }