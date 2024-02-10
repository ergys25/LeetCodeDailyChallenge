
// Time Complexity: O(n^3)
// Space Complexity: O(1)

// Approach: Brute Force
// 1. We can generate all possible substrings and check if they are palindrome or not.
// 2. If a substring is palindrome, we increment the count.


class Solution {

    public boolean isPalindrome(String s, int left, int right) {
        while(left < right) {
            if(s.charAt(left++) != s.charAt(right--)) return false;
        } 
        return true;
    }
    
    public int countSubstrings(String s) {
        int ans = 0;
        int n = s.length();
        for(int i=0;i<n;i++) {
            for(int j=i;j<n;j++) {
                if(isPalindrome(s, i, j)) ans++;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "abc";
        System.out.println(sol.countSubstrings(s));
    }


    
}