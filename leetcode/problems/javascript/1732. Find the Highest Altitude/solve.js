/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function (gain) {
  let maxAlutitude = 0;
  gain.reduce((h, g) => {
    h += g;
    maxAlutitude = Math.max(maxAlutitude, h);
    return h;
  }, 0);
  return maxAlutitude;
};
