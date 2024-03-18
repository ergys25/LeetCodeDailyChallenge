#include <vector>
#include <algorithm>

class Solution {
public:
    int findMinArrowShots(std::vector<std::vector<int>>& points) {
        if (points.empty()) { // If the input vector is empty, return 0
            return 0;
        }

        // Sort the points vector based on the end coordinate of each interval in ascending order
        std::sort(points.begin(), points.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1];
        });

        int arrows = 1; // Initialize the number of arrows needed to 1
        int first_end = points[0][1]; // Set the end coordinate of the first interval

        // Iterate through the remaining intervals
        for (size_t i = 1; i < points.size(); i++) {
            int x_start = points[i][0]; // Get the start coordinate of the current interval
            int x_end = points[i][1]; // Get the end coordinate of the current interval

            // If the end coordinate of the previous interval is less than the start coordinate of the current interval,
            // increment the number of arrows needed and update the end coordinate of the previous interval
            if (first_end < x_start) {
                arrows++;
                first_end = x_end;
            }
        }

        return arrows; // Return the total number of arrows needed
    }
};



// Space Complexity: O(1)
// Time Complexity: O(nlogn) (due to the sorting operation) where n is the number of intervals in the input vector. The rest of the operations take O(n) time. Thus, the overall time complexity is O(nlogn).

