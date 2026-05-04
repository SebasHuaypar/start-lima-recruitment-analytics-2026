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
}

def normalize_data(clean_df):

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

    print("\nNORMALIZED UNIVERSITIES:\n")

    print(
        clean_df["university_normalized"]
        .value_counts()
    )

    return clean_df