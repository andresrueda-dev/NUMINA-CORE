import re
from collections import Counter

def scan_ticket(text):
    tokens = re.findall(r'[A-Z]+|\d+', text.upper())
    letters = [t for t in tokens if t.isalpha()]
    numbers = [t for t in tokens if t.isdigit()]

    return {
        "raw": text,
        "tokens": tokens,
        "letters": letters,
        "numbers": numbers,
        "length": len(text)
    }

def detect_anomalies(scan):
    anomalies = []
    score = 0

    # Longitud rara
    if scan["length"] < 6:
        anomalies.append("Too short")
        score += 20

    if scan["length"] > 18:
        anomalies.append("Too long")
        score += 20

    # Repeticiones tipo 11111
    for num in scan["numbers"]:
        if len(set(num)) == 1:
            anomalies.append(f"Repeated: {num}")
            score += 25

    # Secuencias tipo 12345
    for num in scan["numbers"]:
        if num in "0123456789":
            anomalies.append(f"Sequential: {num}")
            score += 15

    return anomalies, min(score, 100)

def analyze_patterns(scan):
    digits = ''.join(scan["numbers"])
    freq = Counter(digits)

    return {
        "digit_frequency": dict(freq),
        "unique_digits": len(freq)
    }
