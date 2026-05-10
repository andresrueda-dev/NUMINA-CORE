
def calculate_score(
    frequency,
    resonance
):

    score = (
        frequency * 0.7 +
        resonance * 0.3
    )

    return round(score,2)
