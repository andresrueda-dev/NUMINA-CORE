from collections import Counter

def calculate_frequency(df):

    numbers = []

    for col in df.columns:
        if col.startswith("R"):
            numbers.extend(df[col].dropna().tolist())

    return Counter(numbers)
