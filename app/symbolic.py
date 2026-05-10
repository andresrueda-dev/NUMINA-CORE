MASTER_CODE = "7122"

def resonance_score(number):

    score = 0

    for digit in str(number):

        if digit in MASTER_CODE:
            score += 1

    return score
