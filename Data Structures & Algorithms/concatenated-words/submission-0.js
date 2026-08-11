class Solution {
    /**
     * @param {string[]} words
     * @return {string[]}
     */
    findAllConcatenatedWordsInADict(words) {
         const wordSet = new Set(words);
    const result = [];

    function dfs(word, memo) {
        if (memo.has(word)) return memo.get(word);

        for (let i = 1; i < word.length; i++) {
            const prefix = word.slice(0, i);
            const suffix = word.slice(i);

            // prefix is a valid word
            if (wordSet.has(prefix)) {
                // suffix is a word OR can be formed recursively
                if (wordSet.has(suffix) || dfs(suffix, memo)) {
                    memo.set(word, true);
                    return true;
                }
            }
        }

        memo.set(word, false);
        return false;
    }

    for (const word of words) {
        wordSet.delete(word);
          if (dfs(word, new Map())) {
            result.push(word);
        }

        wordSet.add(word);
    }
        return result;

    }
}
