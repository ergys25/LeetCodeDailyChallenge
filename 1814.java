class Solution {
    private int rev(int n) {
      var rev = 0;
  
      while (n > 0) {
        rev = (rev * 10) + (n % 10);
        n /= 10;
      }
      return rev;
    }
  
    public int countNicePairs(int[] nums) {
      var map = new HashMap<Integer, Integer>();
      var ans = 0;
  
      for (var n : nums) {
        var a = map.getOrDefault(n - rev(n), 0);
        ans = (ans + a) % 1000000007;
        map.put(n - rev(n), a+1);
      }
      return ans;
    }
  }