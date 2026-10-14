public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        int n = position.Length;
        if (n == 0) return 0;

        // Step 1: Compute times
        double[] times = new double[n];
        for (int i = 0; i < n; i++) {
            times[i] = (double)(target - position[i]) / speed[i];
        }

        // Step 2: Sort positions descending, keeping times aligned
        Array.Sort(position, times); // sorts ascending by position
        Array.Reverse(position);
        Array.Reverse(times);

        // Step 3: Count fleets
        int fleets = 0;
        double currMaxTime = 0;
        for (int i = 0; i < n; i++) {
            if (times[i] > currMaxTime) {
                fleets++;
                currMaxTime = times[i];
            }
        }

        return fleets;
    }
}
