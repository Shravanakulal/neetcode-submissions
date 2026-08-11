class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
    let zeroCount = 0;
    let totalProduct = 1;

    for (let num of nums) {
        if (num === 0) {
            zeroCount++;
        } else {
            totalProduct *= num;
        }
    }

    let result = new Array(nums.length);

    for (let i = 0; i < nums.length; i++) {
        if (zeroCount > 1) {
            result[i] = 0;
        } else if (zeroCount === 1) {
            result[i] = nums[i] === 0 ? totalProduct : 0;
        } else {
            result[i] = totalProduct / nums[i];
        }
    }

    return result;
};
    }

