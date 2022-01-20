from json.tool import main


def getWrongAnswers(a,b):
    final = []
    for x in b:
        if(x == "A"):
            final.append("B")
        elif(x == "B"):
            final.append("A")
    return ("".join(final))


print(getWrongAnswers(3,"BBBABBB"))