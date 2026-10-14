public class Solution {
    public int Search(int[] nums, int target) {
        return BinarySearch(nums, indexStart:0, indexEnd:nums.Length-1, target);
    }

    public static int BinarySearch(int[] nums, int indexStart, int indexEnd, int target)
    {
        if(indexStart > indexEnd)
        {
            return -1;
        }
        int indexMid  = indexStart + (indexEnd - indexStart) / 2;
        if(nums[indexMid] == target)
        {
            return indexMid;
        }
        else if(nums[indexMid] > target)
        {
           return BinarySearch(nums, indexStart, indexMid - 1, target);
        }
        else
        {
           return BinarySearch(nums, indexMid + 1, indexEnd, target);
        }
    }
}
