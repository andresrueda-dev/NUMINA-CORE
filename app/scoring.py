def pattern_score(
    frequency,
    resonance,
    repetition
):

    score = (
        frequency * 0.5 +
        resonance * 0.3 +
        repetition * 0.2
    )

    return round(score,2)
