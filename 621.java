class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        int max_count = 0;

        for (char task : tasks) {
            freq[(int) task - (int) 'A']++;
            max_count = Math.max(max_count, freq[(int) task - (int) 'A']);
        }

        Arrays.sort(freq);
        int time = (max_count - 1) * (n + 1);
        for (int i = freq.length - 1; i >= 0; i--) {
            if (freq[i] < max_count) {
                break;
            }
            if (freq[i] == max_count) {
                time++;
            }
        }
        return Math.max(tasks.length, time);
    }
}

// space: O(1)
// time: O(nlogn)
