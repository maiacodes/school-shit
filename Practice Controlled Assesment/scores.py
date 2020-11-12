import json
import os

scorefile = open('scores.json', 'r+')
scoredata = json.load(scorefile)

def storeScore(name: str, score: int):
    scoredata.append({
        "name": name,
        "score": score
    })
    os.remove('scores.json')
    f = open("scores.json", "w") 
    json.dump(scoredata, f)
    

def showTop():
    sortedScores = sorted(scoredata, key=lambda data: data["score"], reverse=True)
    print("--- TOP SCORES ---")
    i = 0
    for score in sortedScores:
        i = i+1
        if i > 5:
            quit()
        print(f"{i}) {score['name']}: {score['score']} points")
