# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)
# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.
# Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)
#
# Steps
# 1. Use a 2D array to represent the glasses
# 2. Iterate through the rows and columns, if the glass is full, pour half of the champagne to the left and right glass
# 3. Return the amount of champagne in the glass
#
# Time: O(n^2)
# Space: O(n^2)
#
# Runtime: 32 ms, faster than 77.65% of Python3 online submissions for Champagne Tower.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Champagne Tower.
#
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * (query_row + 1) for _ in range(query_row + 1)] # O(n^2)
        glasses[0][0] = poured # O(1)

        
        for row in range(query_row + 1): # O(n^2)
            for col in range(row + 1): # O(n^2)
                if glasses[row][col] >= 1: # O(1)
                    half = (glasses[row][col] - 1) / 2 # O(1)
                    glasses[row][col] = 1 # O(1)
                    if row + 1 < query_row + 1: # O(1)
                        glasses[row + 1][col] += half # O(1)
                        glasses[row + 1][col + 1] += half # O(1)
        
                print(glasses)

        return glasses[query_row][query_glass] # O(1)
    
    print(champagneTower(None, 16, 4, 4)) 

 