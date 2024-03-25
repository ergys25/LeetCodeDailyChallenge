class Solution {
  public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans;

        for (int i = 0; i < nums.size(); i++)
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[j] == nums[i]) {
                    ans.push_back(nums[i]);
                    break;
                }
            }

        return ans;
    }
};