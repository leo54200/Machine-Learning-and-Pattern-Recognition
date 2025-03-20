def removeMax(lst):
    maxVal = max(lst)
    lst.remove(maxVal)
    return lst
def removeMin(lst):
    minVal = min(lst)
    lst.remove(minVal)
    return lst

if __name__ == "__main__":
    with open("score.txt", "r") as f:
        rows = f.readlines()
    CountryScore = []
    podio = []
    for row in rows:
        row = row.strip()
        fields = row.split()
        if len(fields) >= 3:
            name = str(fields[0]) + ' ' + str(fields[1])
            country = str(fields[2])
            scores = []
            for field in fields[3:]:
                scores.append(float(field))
            scores = removeMax(scores)
            scores = removeMin(scores)
            totScore = sum(scores)
            if(len(CountryScore) == 0):
                CountryScore.append((country, totScore))
            else:
                found = False
                for i in range(len(CountryScore)):
                    if(CountryScore[i][0] == country):
                        CountryScore[i] = (country, CountryScore[i][1] + totScore)
                        found = True
                        break
                if(not found):
                    CountryScore.append((country, totScore))
            if(len(podio) < 3):
                podio.append((name, totScore))
            elif(totScore > podio[0][1]):
                podio[2] = podio[1]
                podio[1] = podio[0]
                podio[0] = (name, totScore)
            elif(totScore > podio[1][1]):
                podio[2] = podio[1]
                podio[1] = (name, totScore)
            elif(totScore > podio[2][1]):
                podio[2] = (name, totScore)
    print("First:", podio[0])
    print("Second:", podio[1])
    print("Third:", podio[2])
    maxScoreCountry = 0
    for c in CountryScore:
        if maxScoreCountry < float(c[1]):
            maxScoreCountry = float(c[1])
            maxC = str(c[0]) + ' ' + str(c[1])
    print("Country with the highest score: ", maxC)
    f.close()