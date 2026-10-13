public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        if (position.Length == 0) return 0;

        var cars = position
            .Select((p, i) => new { pos = p, time = (double)(target - p) / speed[i] })
            .OrderByDescending(c => c.pos)
            .ToList();

        int fleets = 0;
        double currMaxTime = 0;

        foreach (var car in cars) {
            if (car.time > currMaxTime) {
                fleets++;
                currMaxTime = car.time;
            }
        }

        return fleets;
    }
}
