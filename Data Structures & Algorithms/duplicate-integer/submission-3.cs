public class Solution {
    public bool hasDuplicate(int[] nums) {
        var inSet = new HashSet<int>();
        for(int i = 0; i < nums.Length; i++)
        {
            if(inSet.Contains(nums[i]))
            {
                return true;
            }
            inSet.Add(nums[i]);
        }
        return false;
    }
}