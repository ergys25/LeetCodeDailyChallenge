/**
 * This class represents a solution for finding the maximum depth of parentheses in a given string.
 */
class Solution {
    /**
     * Calculates the maximum depth of parentheses in the given string.
     *
     * @param s the input string
     * @return the maximum depth of parentheses
     */
    public int maxDepth(String s) {
        int result = 0;
        int depth = 0;
        
        if (s.length() == 0) {
            return 0;
        }
        
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                depth++;
            }
            if (ch == ')') {
                depth--;
            }
            result = Math.max(result, depth);
        }
        
        return result;
    }
}

// Space: O(1)
// Time: O(n)
