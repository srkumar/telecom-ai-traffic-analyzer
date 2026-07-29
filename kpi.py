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
def country_analysis(df):
    country =df["country"].value_counts()
    total = (
    df.groupby(["date", "country"]).size().reset_index(name = "total_traffic"))
    delivered = (df[df["status"]=="Delivered"].groupby(["date", "country"]).size().reset_index(name = "delivered"))
    failed = (df[df["status"]=="Failed"].groupby(["date", "country"]).size().reset_index(name = "failed"))
    daily_country_report = total.merge(delivered,on = ["date", "country"],how = "left")
    daily_country_report = daily_country_report.merge(failed,on = ["date", "country"],how = "left")
    daily_country_report = daily_country_report.fillna(0)
    daily_country_report["delivery_percentage"] = (daily_country_report["delivered"]/daily_country_report["total_traffic"]) * 100
    daily_country_report["failed_percentage"] = (daily_country_report["failed"] /daily_country_report["total_traffic"]) * 100
    
    return {
        "country_summary": country,
        "daily_country_report" : daily_country_report
    }

def operator_analysis(df):
    operator = df["operator"].value_counts()
    total = (df.groupby(["date", "operator"]).size().reset_index(name = "total_traffic"))
    delivered = (df[df["status"]=="Delivered"].groupby(["date", "operator"]).size().reset_index(name = "delivered"))
    failed = (df[df["status"]=="Failed"].groupby(["date","operator"]).size().reset_index(name="failed"))
    daily_operator_report = total.merge(delivered, on =["date", "operator"],how = "left")
    daily_operator_report = daily_operator_report.merge(failed, on =["date", "operator"], how = "left")
    daily_operator_report = daily_operator_report.fillna(0)
    daily_operator_report ["delivery_percentage"] = (daily_operator_report["delivered"]/daily_operator_report["total_traffic"])*100
    daily_operator_report["failed_percentage"] = (daily_operator_report["failed"] /daily_operator_report["total_traffic"]) * 100
    
    return {
    "operator_summary" : operator,
    "daily_operator_report" : daily_operator_report
    }