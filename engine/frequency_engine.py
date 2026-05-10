from collections import Counter

def calculate_frequency(df):

    numbers = []

    for col in df.columns:

        if col.startswith("r"):

            numbers.extend(
                df[col].dropna().tolist()
            )

    frequency = Counter(numbers)

    return frequency
