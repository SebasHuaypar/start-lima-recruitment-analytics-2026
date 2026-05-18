import pandas as pd

from normalize.channels import normalize_channels
from normalize.universities import normalize_universities


def classify_engagement(score):

    if score >= 4:
        return "High"

    elif score >= 2:
        return "Medium"

    else:
        return "Low"


def normalize_data(clean_df):

    # Delegate channel and university normalization to their respective helper functions:
    clean_df = normalize_channels(clean_df)

    clean_df = normalize_universities(clean_df)

    # Convert the cycle text into a numeric format to allow for proper sorting:
    clean_df["cycle_numeric"] = (
        clean_df["cycle"]
        .replace({
            "Egresado(a)": 11
        })
    )

    clean_df["cycle_numeric"] = pd.to_numeric(
        clean_df["cycle_numeric"],
        errors="coerce"
    ).astype("Int64")

    # Boolean flag indicating whether the candidate provided a LinkedIn profile:
    clean_df["has_linkedin"] = (
        clean_df["linkedin"]
        .notna()
    )

    # Measure the length of written responses to assess candidate effort:
    clean_df["goals_length"] = (
        clean_df["goals"]
        .fillna("")
        .str.len()
    )

    clean_df["project_length"] = (
        clean_df["project"]
        .fillna("")
        .str.len()
    )

    clean_df["activities_length"] = (
        clean_df["activities"]
        .fillna("")
        .str.len()
    )

    # Create a more human-readable submission status text for the dashboard:
    clean_df["submission_status"] = (
        clean_df["is_submitted"]
        .map({
            True: "Submitted",
            False: "Incomplete"
        })
    )

    # A friendly text version for the LinkedIn flag:
    clean_df["linkedin_status"] = (
        clean_df["has_linkedin"]
        .map({
            True: "Has LinkedIn",
            False: "No LinkedIn"
        })
    )

    # Engagement score awards points based on LinkedIn profile and essay lengths:
    clean_df["engagement_score"] = (
        clean_df["has_linkedin"].astype(int)
        + (clean_df["goals_length"] > 300).astype(int)
        + (clean_df["project_length"] > 300).astype(int)
        + (clean_df["activities_length"] > 150).astype(int)
    )

    # Classify the numeric score into High, Medium, or Low tiers for easier analysis:
    clean_df["engagement_level"] = (
        clean_df["engagement_score"]
        .apply(classify_engagement)
    )

    # Build an application period string (e.g., "2026-W16") to group applications by week:
    clean_df["application_period"] = (
        clean_df["application_year"].astype(str)
        + "-W"
        + clean_df["application_week"].astype(str).str.zfill(2)
    )

    # Identify the top 10 most frequent universities and group the rest under 'Other':
    top_universities = (
        clean_df["university_normalized"]
        .fillna("Unknown")
        .value_counts()
        .head(10)
        .index
    )

    clean_df["university_group"] = (
        clean_df["university_normalized"]
        .apply(
            lambda x: x if x in top_universities else "Other"
        )
    )

    return clean_df