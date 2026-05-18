import pandas as pd
import unicodedata
import re


def normalize_string(text):

    if pd.isna(text):
        return None

    text = str(text).strip().lower()

    # Safely strip away accents and special characters to ensure robust matching:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")

    return text


def remove_other_prefix(text):

    if pd.isna(text):
        return None

    text = str(text).strip()

    # Clean out the 'Otro:' or 'Otra (Especificar):' prefixes from custom form answers:
    text = re.sub(
        r"^(otro|otra)\s*(\(.*?\))?\s*:\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Catch and clear exact "Otra(Especificar)" selections that contain no other text:
    text = re.sub(
        r"^(otro|otra)\s*(\(.*?\))$",
        "",
        text,
        flags=re.IGNORECASE
    )

    return text.strip()