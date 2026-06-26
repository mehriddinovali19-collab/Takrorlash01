
def score_average(scores):
    result = []

    for name, score in scores.items(): 
        average = sum(score.values()) / len(score)
        result.append(f"{name}: {average}")
    
    return result

data = {"Ali": {"math":90,"fizika":80},
        "vali": {"math":90, "fizika": 85},
        "sali": {"math":60, "fizika": 75}}

print(score_average(data))