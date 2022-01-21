from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    
    counter = 0
    for i in range(R):
        for j in range(C):
            if(G[i][j] == 1):
                counter = counter + 1
            
            
        

    return (counter/(R*C))


print(getHitProbability(2,2,[[1,1],[1,1]]))

