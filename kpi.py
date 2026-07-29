def calculate_kpis(df):
    total = len(df)
    delivered = (df["status"]=="Delivered").sum()
    failed = (df["status"]=="Failed").sum()
    delivered_percentage = delivered / total
    failed_percentage = failed / total
    return {
        "total": total,
        "delivered" : delivered,
        "failed" : failed,
        "delivered_percentage" : delivered_percentage,
        "failed_percentage" : failed_percentage
    }
