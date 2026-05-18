import pandas as pd

from normalize.helpers import (
    normalize_string,
    remove_other_prefix
)

UNIVERSITY_ALIASES = {

    "upc": "Universidad Peruana de Ciencias Aplicadas",

    "pucp": "Pontificia Universidad Católica del Perú",

    "utp": "Universidad Tecnológica del Perú",
    "universidad tecnologica del peru": "Universidad Tecnológica del Perú",
    "universidad tecnologia del peru": "Universidad Tecnológica del Perú",

    "unmsm": "Universidad Nacional Mayor de San Marcos",

    "uni": "Universidad Nacional de Ingeniería",
    "universidad nacional de ingenieria": "Universidad Nacional de Ingeniería",

    "udep": "Universidad de Piura",

    "utec": "Universidad de Ingeniería y Tecnología",

    "universidad de lima": "Universidad de Lima",

    "universidad del pacifico": "Universidad del Pacífico",

    "esan": "Universidad ESAN",

    "usil": "Universidad San Ignacio de Loyola",

    "upao": "Universidad Privada Antenor Orrego",
    "universidad privada antenor orrego": "Universidad Privada Antenor Orrego",
    "dnt upao": "Universidad Privada Antenor Orrego",

    "upn": "Universidad Privada del Norte",
    "universidad privada del norte": "Universidad Privada del Norte",

    "ucsur": "Universidad Científica del Sur",
    "universidad cientifica del sur": "Universidad Científica del Sur",

    "ucsp": "Universidad Católica San Pablo",
    "universidad catolica san pablo": "Universidad Católica San Pablo",

    "upch": "Universidad Peruana Cayetano Heredia",
    "upch cayetano heredia": "Universidad Peruana Cayetano Heredia",
    "upch (cayetano heredia)": "Universidad Peruana Cayetano Heredia",
    "universidad peruana cayetano heredia": "Universidad Peruana Cayetano Heredia",
    "universidad peruana cayetano heredia - ingenieria informatica": "Universidad Peruana Cayetano Heredia",

    "unsaac": "Universidad Nacional de San Antonio Abad del Cusco",
    "universidad nacional de san antonio abad del cusco": "Universidad Nacional de San Antonio Abad del Cusco",

    "unsa": "Universidad Nacional de San Agustín",
    "universidad nacional de san agustin": "Universidad Nacional de San Agustín",

    "usmp": "Universidad de San Martín de Porres",

    "unprg": "Universidad Nacional Pedro Ruiz Gallo",
    "universidad nacional pedro ruiz gallo": "Universidad Nacional Pedro Ruiz Gallo",

    "uct": "Universidad Católica de Trujillo",
    "universidad catolica de trujillo benedicto xvi": "Universidad Católica de Trujillo",
    "universidad catolica de trujillo": "Universidad Católica de Trujillo",

    "unaj": "Universidad Nacional de Juliaca",
    "universidad nacional de juliaca": "Universidad Nacional de Juliaca",

    "unt": "Universidad Nacional de Trujillo",

    "unfv": "Universidad Nacional Federico Villarreal",
    "universidad nacional federico villarreal": "Universidad Nacional Federico Villarreal",

    "urp": "Universidad Ricardo Palma",
    "universidad ricardo palma": "Universidad Ricardo Palma",

    "uarm": "Universidad Antonio Ruiz de Montoya",
    "universidad antonio ruiz de montoya": "Universidad Antonio Ruiz de Montoya",

    "uncp": "Universidad Nacional del Centro del Perú",
    "universidad nacional del centro del peru": "Universidad Nacional del Centro del Perú",

    "unsch": "Universidad Nacional de San Cristóbal de Huamanga",
    "universidad nacional de san cristobal de huamanga": "Universidad Nacional de San Cristóbal de Huamanga",

    "ucsm": "Universidad Católica de Santa María",

    "usat": "Universidad Católica Santo Toribio de Mogrovejo",
    "universidad catolica santo toribio de mogrovejo": "Universidad Católica Santo Toribio de Mogrovejo",

    "universidad continental": "Universidad Continental",
    "universidad continental ": "Universidad Continental",

    "universidad privada norbert wiener": "Universidad Norbert Wiener",
    "wiener": "Universidad Norbert Wiener",

    "universidad autonoma del peru": "Universidad Autónoma del Perú",

    "universidad nacional del santa": "Universidad Nacional del Santa",
    "universidad nacional del santa uns": "Universidad Nacional del Santa",
    "universidad nacional del santa (uns)": "Universidad Nacional del Santa",

    "universidad nacional de moquegua": "Universidad Nacional de Moquegua",

    "universidad nacional de jaen": "Universidad Nacional de Jaén",

    "universidad nacional san luis gonzaga de ica": "Universidad Nacional San Luis Gonzaga",

    "universidad nacional santiago antunez de mayolo": "Universidad Nacional Santiago Antúnez de Mayolo",
    "unasam": "Universidad Nacional Santiago Antúnez de Mayolo",

    "universidad nacional agraria la molina": "Universidad Nacional Agraria La Molina",
    "unalm": "Universidad Nacional Agraria La Molina",

    "universidad andina del cusco": "Universidad Andina del Cusco",

    "universidad tecnologica de los andes": "Universidad Tecnológica de los Andes",

    "universidad nacional del callao": "Universidad Nacional del Callao",

    "universidad nacional herminio valdizan": "Universidad Nacional Hermilio Valdizán",

    "universidad autonoma de nuevo leon": "Universidad Autónoma de Nuevo León",
    "uanl": "Universidad Autónoma de Nuevo León",

    "universidade federal do para": "Universidade Federal do Pará",

    "charles sturt university": "Charles Sturt University",
    "csu australia": "Charles Sturt University",

    "tecsup": "TECSUP",

    "isil": "Instituto San Ignacio de Loyola",
    "estudie escuela isil": "Instituto San Ignacio de Loyola",

    "cibertec": "Cibertec",

    "senati": "SENATI",

    "idat": "IDAT",

    "instituto politecnico nacional": "Instituto Politécnico Nacional",

    "toulouse lautrec": "Instituto Toulouse Lautrec",

    "instituto monserrat": "Instituto Monserrat",

    "recien egresada de certus": "Certus",

    "ninguna": "Self-Taught",
    "independiente": "Self-Taught",

    "abaco": "Other",
    "ja acabei": "Other",
    "5to secundaria": "Other",
    "tec de chucuito": "Other",
}
UNIVERSITY_SHORT_MAP = {

    "Universidad Peruana de Ciencias Aplicadas": "UPC",
    "Pontificia Universidad Católica del Perú": "PUCP",
    "Universidad Tecnológica del Perú": "UTP",
    "Universidad Nacional Mayor de San Marcos": "UNMSM",
    "Universidad Nacional de Ingeniería": "UNI",
    "Universidad de Ingeniería y Tecnología": "UTEC",
    "Universidad de Lima": "ULima",
    "Universidad de Piura": "UDEP",
    "Universidad del Pacífico": "UP",
    "Universidad ESAN": "ESAN",
    "Universidad San Ignacio de Loyola": "USIL",
    "Universidad Privada Antenor Orrego": "UPAO",
    "Universidad Privada del Norte": "UPN",
    "Universidad Científica del Sur": "UCSUR",
    "Universidad Católica San Pablo": "UCSP",
    "Universidad Peruana Cayetano Heredia": "UPCH",
    "Universidad Nacional de San Antonio Abad del Cusco": "UNSAAC",
    "Universidad Nacional de San Agustín": "UNSA",
    "Universidad de San Martín de Porres": "USMP",
    "Universidad Nacional de Trujillo": "UNT",
    "Universidad Nacional Federico Villarreal": "UNFV",
    "Universidad Ricardo Palma": "URP",
    "Universidad Antonio Ruiz de Montoya": "UARM",
    "Universidad Nacional del Centro del Perú": "UNCP",
    "Universidad Nacional de San Cristóbal de Huamanga": "UNSCH",
    "Universidad Católica de Santa María": "UCSM",
    "Universidad Católica Santo Toribio de Mogrovejo": "USAT",
    "Universidad Nacional Pedro Ruiz Gallo": "UNPRG",
    "Universidad Católica de Trujillo": "UCT",
    "Universidad Nacional de Juliaca": "UNAJ",

    "Universidad Continental": "UC",
    "Universidad Norbert Wiener": "Wiener",
    "Universidad Autónoma del Perú": "Autónoma",
    "Universidad Nacional del Santa": "UNS",
    "Universidad Nacional de Moquegua": "UNAM",
    "Universidad Nacional de Jaén": "UNJ",
    "Universidad Nacional San Luis Gonzaga": "UNICA",
    "Universidad Nacional Santiago Antúnez de Mayolo": "UNASAM",
    "Universidad Nacional Agraria La Molina": "UNALM",
    "Universidad Andina del Cusco": "UAC",
    "Universidad Tecnológica de los Andes": "UTEA",
    "Universidad Nacional del Callao": "UNAC",
    "Universidad Nacional Hermilio Valdizán": "UNHEVAL",
    "Universidad Autónoma de Nuevo León": "UANL",

    "TECSUP": "TECSUP",
    "Instituto San Ignacio de Loyola": "ISIL",
    "Cibertec": "CIBERTEC",
    "SENATI": "SENATI",
    "IDAT": "IDAT",
    "Instituto Toulouse Lautrec": "TLS",
    "Instituto Politécnico Nacional": "IPN",
    "Instituto Monserrat": "Monserrat",

    "Certus": "CERTUS",

    "Charles Sturt University": "CSU",
    "Universidade Federal do Pará": "UFPA",

    "Self-Taught": "Self-Taught",
}


def classify_education_type(university):

    if pd.isna(university):
        return None

    university_clean = normalize_string(university)

    if any(keyword in university_clean for keyword in [
        "instituto",
        "tecsup",
        "senati",
        "cibertec",
        "certus",
        "idat"
    ]):
        return "Institute"

    elif university == "Self-Taught":
        return "Self-Taught"

    elif any(keyword in university_clean for keyword in [
        "australia",
        "nuevo leon",
        "federal do para"
    ]):
        return "International"

    VALID_UNIVERSITIES = set(UNIVERSITY_SHORT_MAP.keys())

    if university in VALID_UNIVERSITIES:
        return "University"

    return "Other"


def normalize_university(university):

    if pd.isna(university):
        return None

    # Strip the 'Otro:' or 'Otra:' strings that usually prefix custom form answers
    university = remove_other_prefix(university)

    # Remove accents and set to lowercase to ensure matching ignores typing quirks
    university_clean = normalize_string(university)

    if (
        university_clean is None
        or university_clean == ""
    ):
        return None

    # Return canonical name if mapped, otherwise default to the cleaned original string:
    return UNIVERSITY_ALIASES.get(
        university_clean,
        university.strip()
    )


def normalize_universities(clean_df):

    # Resolve aliases to get a canonical full name for each university:
    clean_df["university_normalized"] = (
        clean_df["university"]
        .apply(normalize_university)
    )

    # Map the canonical name to a shorter BI-friendly acronym (e.g., 'PUCP'):
    clean_df["university_short"] = (
        clean_df["university_normalized"]
        .map(UNIVERSITY_SHORT_MAP)
    )

    clean_df["university_short"] = (
        clean_df["university_short"]
        .fillna(clean_df["university_normalized"])
    )

    clean_df["university_short"] = (
        clean_df["university_short"]
        .fillna("Unknown")
    )

    # Categorize the institution into broader buckets like 'University' or 'Institute':
    clean_df["education_type"] = (
        clean_df["university_normalized"]
        .apply(classify_education_type)
    )

    print("\nNORMALIZED UNIVERSITIES:\n")

    print(
        clean_df["university_normalized"]
        .value_counts(dropna=False)
    )

    print("\nUNIVERSITY SHORT:\n")

    print(
        clean_df["university_short"]
        .value_counts(dropna=False)
    )

    print("\nEDUCATION TYPES:\n")

    print(
        clean_df["education_type"]
        .value_counts(dropna=False)
    )

    return clean_df