import pandas as pd

UNIVERSITY_MAP = {
    "UPC": "Universidad Peruana de Ciencias Aplicadas",
    "PUCP": "Pontificia Universidad Católica del Perú",
    "UTP": "Universidad Tecnológica del Perú",
    "UNMSM": "Universidad Nacional Mayor de San Marcos",
    "UDEP": "Universidad de Piura",
    "UCSP": "Universidad Católica San Pablo",
    "USIL": "Universidad San Ignacio de Loyola",
    "Usil": "Universidad San Ignacio de Loyola",
    "URP": "Universidad Ricardo Palma",
    "UPCH": "Universidad Peruana Cayetano Heredia",
    "UPN": "Universidad Privada del Norte",
    "UNFV": "Universidad Nacional Federico Villarreal",
    "UNSA": "Universidad Nacional de San Agustín",
    "UCSUR": "Universidad Científica del Sur",
    "UNT": "Universidad Nacional de Trujillo",
    "ESAN": "Universidad ESAN",
    "UTEC": "Universidad de Ingeniería y Tecnología",
    "UPAO": "Universidad Privada Antenor Orrego",
    "Recién egresada de Certus": "Certus",
    "UNIVERSIDAD RICARDO PALMA": "Universidad Ricardo Palma",
    "UNIVERSIDAD CONTINENTAL": "Universidad Continental",
    "Universidad nacional del callao": "Universidad Nacional del Callao",
    "Universidad Nacional de San Agustin": "Universidad Nacional de San Agustín",
    "USMP": "Universidad de San Martín de Porres",
    "ISIL": "Instituto San Ignacio de Loyola",
    "UARM": "Universidad Antonio Ruiz de Montoya",
    "INSTITUTO POLITECNICO NACIONAL": "Instituto Politécnico Nacional",
    "UNIVERSIDAD NACIONAL DEL SANTA": "Universidad Nacional del Santa",
    "UNPRG": "Universidad Nacional Pedro Ruiz Gallo",
    "UNSAAC": "Universidad Nacional de San Antonio Abad del Cusco",
    "Tecsup": "TECSUP",
    "Unalm": "Universidad Nacional Agraria La Molina",
    "DNT UPAO": "Universidad Privada Antenor Orrego",
    "IDAT": "IDAT",
    "Wiener": "Universidad Norbert Wiener",
    "Universidad continental": "Universidad Continental",
    "UNIVERSIDAD NACIONAL DE MOQUEGUA": "Universidad Nacional de Moquegua",
    "Senati": "SENATI",
    "Estudié Escuela ISIL": "Instituto San Ignacio de Loyola",
    "USAT": "Universidad Católica Santo Toribio de Mogrovejo",
    "Ucsur": "Universidad Científica del Sur",
    "Toulouse Lautrec": "Instituto Toulouse Lautrec",
    "CIBERTEC": "Cibertec",
    "UNIVERSIDAD CATOLICA SANTO TORIBIO DE MOGROVEJO": "Universidad Católica Santo Toribio de Mogrovejo",
    "UNI": "Universidad Nacional de Ingeniería",
    "UNCP": "Universidad Nacional del Centro del Perú",
    "UCSM": "Universidad Católica de Santa María",
    "UNSCH": "Universidad Nacional de San Cristóbal de Huamanga",
    "upn": "Universidad Privada del Norte",
    "Universidad Nacional de San Cristóbal de Huamanga": "Universidad Nacional de San Cristóbal de Huamanga",
}

def classify_education_type(university):

    if pd.isna(university):
        return None

    university = str(university).lower()

    if any(keyword in university for keyword in [
        "instituto",
        "isil",
        "senati",
        "cibertec",
        "certus",
        "idat",
        "tecsup",
        "toulouse"
    ]):
        return "Institute"

    elif any(keyword in university for keyword in [
        "independiente",
        "no estudio",
        "ninguna"
    ]):
        return "Self-Taught"

    elif any(keyword in university for keyword in [
        "australia",
        "uanl",
        "federal do pará"
    ]):
        return "International"

    else:
        return "University"
    
def classify_engagement(score):

    if score >= 4:
        return "High"

    elif score >= 2:
        return "Medium"

    else:
        return "Low"


def normalize_data(clean_df):

    # Let's explore the university, channel, and cycle distributions before normalization:
    print("\nUNIVERSITIES:\n")
    print(clean_df["university"].value_counts(dropna=False))

    print("\nCHANNELS:\n")
    print(clean_df["channel"].value_counts(dropna=False))

    print("\nCYCLES:\n")
    print(clean_df["cycle"].value_counts(dropna=False))

    # Now, let's clean and normalize the university names:
    # Remove "Otra (Especificar):"
    clean_df["university"] = (
        clean_df["university"]
        .str.replace(r"Otra\s*\(Especificar\):", "", regex=True)
        .str.strip()
    )

    # Remove parentheses
    clean_df["university"] = (
        clean_df["university"]
        .str.replace(r"\s*\(.*?\)", "", regex=True)
        .str.strip()
    )

    # Normalize university names
    clean_df["university_normalized"] = (
        clean_df["university"]
        .replace(UNIVERSITY_MAP)
    )

    # Education type classification
    clean_df["education_type"] = (
        clean_df["university_normalized"]
        .apply(classify_education_type)
    )

    # Create numeric cycle feature
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

    # Feature engineering
    clean_df["has_linkedin"] = (
        clean_df["linkedin"]
        .notna()
    )

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

    # Submission status
    clean_df["submission_status"] = (
        clean_df["is_submitted"]
        .map({
            True: "Submitted",
            False: "Incomplete"
        })
    )

    # LinkedIn status
    clean_df["linkedin_status"] = (
        clean_df["has_linkedin"]
        .map({
            True: "Has LinkedIn",
            False: "No LinkedIn"
        })
    )

    # Engagement score
    clean_df["engagement_score"] = (
        clean_df["has_linkedin"].astype(int)
        + (clean_df["goals_length"] > 300).astype(int)
        + (clean_df["project_length"] > 300).astype(int)
        + (clean_df["activities_length"] > 150).astype(int)
    )

    # Engagement level
    clean_df["engagement_level"] = (
        clean_df["engagement_score"]
        .apply(classify_engagement)
    )

    # Application period
    clean_df["application_period"] = (
        clean_df["application_year"].astype(str)
        + "-W"
        + clean_df["application_week"].astype(str).str.zfill(2)
    )

    # Top universities grouping
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

    # Final validation outputs
    print("\nNORMALIZED UNIVERSITIES:\n")

    print(
        clean_df["university_normalized"]
        .value_counts(dropna=False)
    )

    print("\nEDUCATION TYPES:\n")

    print(
        clean_df["education_type"]
        .value_counts(dropna=False)
    )

    return clean_df