import pandas as pd


def country_analysis(df):

    # Total traffic
    total = (
        df.groupby(["date", "country"])
        .size()
        .reset_index(name="total_traffic")
    )

    # Delivered traffic
    delivered = (
        df[df["status"] == "Delivered"]
        .groupby(["date", "country"])
        .size()
        .reset_index(name="delivered")
    )

    # Failed traffic
    failed = (
        df[df["status"] == "Failed"]
        .groupby(["date", "country"])
        .size()
        .reset_index(name="failed")
    )

    # Merge reports
    daily_country_report = total.merge(
        delivered,
        on=["date", "country"],
        how="left"
    )

    daily_country_report = daily_country_report.merge(
        failed,
        on=["date", "country"],
        how="left"
    )

    # Replace NaN with 0
    daily_country_report = daily_country_report.fillna(0)

    # Percentages
    daily_country_report["delivery_percentage"] = (
        daily_country_report["delivered"]
        / daily_country_report["total_traffic"]
    ) * 100

    daily_country_report["failed_percentage"] = (
        daily_country_report["failed"]
        / daily_country_report["total_traffic"]
    ) * 100

    # Country Summary (All Dates Combined)
    country_summary = (
        daily_country_report
        .groupby("country", as_index=False)
        .agg(
            {
                "total_traffic": "sum",
                "delivered": "sum",
                "failed": "sum"
            }
        )
    )

    country_summary["delivery_percentage"] = (
        country_summary["delivered"]
        / country_summary["total_traffic"]
    ) * 100

    country_summary["failed_percentage"] = (
        country_summary["failed"]
        / country_summary["total_traffic"]
    ) * 100

    top_traffic = (
    country_summary
    .sort_values("total_traffic", ascending=False)
    .head(10)
    )

    top_failure = (
        country_summary
        .sort_values("failed", ascending =False)
        .head(10)
    )

    
    return {
        "country_summary": country_summary,
        "daily_country_report": daily_country_report,
        "top_traffic" : top_traffic,
        "top_failure" : top_failure        
    }