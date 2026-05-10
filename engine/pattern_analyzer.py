from engine.frequency_engine import calculate_frequency

def analyze_patterns(df):

    frequency = calculate_frequency(df)

    sorted_freq = sorted(
        frequency.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_freq
