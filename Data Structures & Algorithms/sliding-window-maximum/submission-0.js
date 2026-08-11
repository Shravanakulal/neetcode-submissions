class Solution {
    maxSlidingWindow(nums, k) {
        const deque = [];   // stores indices
        const ans = [];

        for (let i = 0; i < nums.length; i++) {

            // Remove indices that are out of the current window
            while (deque.length && deque[0] <= i - k) {
                deque.shift();
            }

            // Remove smaller elements from the back
            while (deque.length && nums[deque[deque.length - 1]] <= nums[i]) {
                deque.pop();
            }

            // Add current index
            deque.push(i);

            // Store the maximum once the first window is complete
            if (i >= k - 1) {
                ans.push(nums[deque[0]]);
            }
        }

        return ans;
    }
}