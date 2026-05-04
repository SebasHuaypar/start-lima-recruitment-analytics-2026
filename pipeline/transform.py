import pandas as pd

def transform_applications(df):

    parsed_rows = []

    for _, row in df.iterrows():

        answers = row["answers"]

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

    return clean_df