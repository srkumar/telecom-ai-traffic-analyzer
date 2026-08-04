import pandas as pd


def load_logs(file_path):
    """
    Load telecom logs.
    """
    return pd.read_csv(file_path, dtype={"error_code": str})


def load_error_master(file_path):
    """
    Load Error Code Master.
    """
    return pd.read_csv(file_path, dtype={"Error_Code": str})

def top_errors(log_df):
    """
    Return top occurring error codes.
    """

    return (
        log_df[log_df["status"] == "Failed"]
        .groupby("error_code")
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
    )

def get_error_details(error_code, error_df):
    """
    Return details of a single error code.
    """

    result = error_df[
        error_df["Error_Code"] == error_code
    ]

    if result.empty:
        return None

    return result.iloc[0]