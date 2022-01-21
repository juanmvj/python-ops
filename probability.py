from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    
    counter = 0
    for i in range(len(G)):
        for j in range(len(G)):
            if (G[i][j] == 1):
                counter = counter + 1

    return 0.0


getHitProbability(2,3,[[0,0,1],[1,0,1]])


test = [[0,0,1],[1,0,1]]

print(test[0][2])