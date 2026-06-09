import re

# Limpieza de nombres conflictivos
def clean_column_name(value: str) -> str:
    return re.sub('[^A-Za-z0-9_]', '_', value)