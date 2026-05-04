import pandas as pd

def transform_applications(df):

    parsed_rows = []

    for _, row in df.iterrows():

        answers = row["answers"]

        # Some applications might not have answers, so we need to handle that case:
        if answers is None:
            answers = {}

        # The answers are stored as a JSON string, so we need to parse it:
        if isinstance(answers, str):
            answers = pd.json.loads(answers)

        clean_row = {
            "id": row["id"],
            "email": row["email"],
            "status": row["status"],
            "current_stage": row["current_stage"],
            "created_at": row["created_at"],

            "first_name": answers.get("first_name"),
            "last_name": answers.get("last_name"),
            "university": answers.get("university"),
            "cycle": answers.get("ciclo"),
            "phone": answers.get("phone"),
            "linkedin": answers.get("linkedin"),
            "availability": answers.get("availability"),
            "goals": answers.get("goals"),
            "project": answers.get("project"),
            "activities": answers.get("activities"),
            "channel": answers.get("canal_adqui"),
        }

        parsed_rows.append(clean_row)

    clean_df = pd.DataFrame(parsed_rows)

    # Let's convert the created_at column to datetime and extract some date features:
    clean_df["created_at"] = pd.to_datetime(clean_df["created_at"])

    clean_df["application_date"] = clean_df["created_at"].dt.date
    clean_df["application_year"] = clean_df["created_at"].dt.year
    clean_df["application_month"] = clean_df["created_at"].dt.month_name()
    clean_df["application_week"] = clean_df["created_at"].dt.isocalendar().week
    clean_df["application_day"] = clean_df["created_at"].dt.day_name()

    # Now, we'll create a new column to indicate whether the application is submitted or not:
    clean_df["is_submitted"] = clean_df["status"] == "submitted"

    return clean_df