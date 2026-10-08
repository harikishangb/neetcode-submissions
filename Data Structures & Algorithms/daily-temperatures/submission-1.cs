public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        Stack<int> stack = new Stack<int>();
        int[] result = new int[temperatures.Length];
        for(int j = 0; j < temperatures.Length; j++)
        {
            while (stack.Count > 0 && temperatures[stack.Peek()] < temperatures[j])
            {
                int prevIndex = stack.Pop();
                result[prevIndex] = j - prevIndex;
            }
            stack.Push(j);
        }
        return result;
    }
}
