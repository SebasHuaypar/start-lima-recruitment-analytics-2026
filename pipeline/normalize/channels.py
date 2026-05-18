from normalize.helpers import (
    normalize_string,
    remove_other_prefix
)

CHANNEL_MAP = {
    "linkedin": "LinkedIn",
    "email": "Email",
    "instagram": "Instagram",
    "tiktok": "TikTok",
    "facebook": "Facebook",
    "whatsapp": "WhatsApp",

    "referido de un amigo": "Referral",
    "referido de un profesor o mentor": "Referral",

    "evento de start lima": "START Lima Event",

    "incubadora o centro de emprendimiento": "Incubator",
}


def normalize_channel(channel):

    # Early exit for empty channels to prevent errors during string manipulation:
    if channel is None:
        return None

    # Strip the 'Otro:' or 'Otra:' strings that usually prefix custom form answers:
    channel = remove_other_prefix(channel)

    # Convert to lowercase and remove any tricky accents or special characters:
    channel_clean = normalize_string(channel)

    # If the text was only spaces or became empty after normalization, return None:
    if channel_clean is None:
        return None

    # Apply smart inference for common misspellings or abbreviations like 'wssp':
    if (
        "wssp" in channel_clean
        or "whatsapp" in channel_clean
        or "wsp" in channel_clean
    ):
        return "WhatsApp"

    if (
        "gmail" in channel_clean
        or "correo" in channel_clean
        or "mail" in channel_clean
    ):
        return "Email"

    # Return the canonical name if mapped, otherwise default to 'Other':
    return CHANNEL_MAP.get(channel_clean, "Other")


def normalize_channels(clean_df):

    clean_df["channel_normalized"] = (
        clean_df["channel"]
        .apply(normalize_channel)
    )

    print("\nNORMALIZED CHANNELS:\n")

    print(
        clean_df["channel_normalized"]
        .value_counts(dropna=False)
    )

    return clean_df