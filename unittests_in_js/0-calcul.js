/**
 * Rounds two numbers and returns their sum
 * @param {number} a - First number to round and add
 * @param {number} b - Second number to round and add
 * @returns {number} The sum of the rounded numbers
 */
function calculateNumber(a, b) {
  return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;
