def calculate_zones(freq):

    zones = {
        "1-10":0,
        "11-20":0,
        "21-30":0,
        "31-40":0,
        "41-50":0,
        "51-60":0
    }

    for num,count in freq.items():

        num = int(num)

        if num <= 10:
            zones["1-10"] += count

        elif num <= 20:
            zones["11-20"] += count

        elif num <= 30:
            zones["21-30"] += count

        elif num <= 40:
            zones["31-40"] += count

        elif num <= 50:
            zones["41-50"] += count

        else:
            zones["51-60"] += count

    return zones
