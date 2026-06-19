/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  const MaxLen = Math.max(word1.length, word2.length);
  let merged = "";
  for (let i = 0; i < MaxLen; i++) {
    merged += (word1[i] ?? "") + (word2[i] ?? "");
  }
  return merged;
};
