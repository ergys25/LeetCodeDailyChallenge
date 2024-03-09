import java.util.HashSet;
class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        HashSet<Integer> knownNumbers = new HashSet<Integer>();

        for(int i = 0; i < nums1.length; i++){
            knownNumbers.add(nums1[i]);
            
        }
        for(int i = 0; i < nums2.length; i++){
            if(knownNumbers.contains(nums2[i])){
                return nums2[i];

            }
            
        }
        return -1;
        
        
    }
}

// Complexity: O(n) where n is the length of the longest array
// Space: O(n) where n is the length of the longest array
