from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        defeats = defaultdict(int)
        not_lost = []
        one_loss = []


        for match in matches:
            wins[match[0]] += 1
            defeats[match[1]] += 1
        
        for key in wins.keys():
            if wins[key] > 0 and defeats[key] == 0:
                not_lost.append(key) 
        
        for key in defeats.keys():
            if defeats[key] == 1:
                one_loss.append(key)  

        return([sorted(not_lost), sorted(one_loss)])    
        
