class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let s2 =  Array.from(s).sort().join('');
        let t2 =  Array.from(t).sort().join('');

           return s2 === t2;

    }
}
