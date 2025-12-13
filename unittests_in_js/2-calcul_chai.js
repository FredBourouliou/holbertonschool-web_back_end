/**
 * Performs arithmetic operations on rounded numbers
 * @param {string} type - The operation type: 'SUM', 'SUBTRACT', or 'DIVIDE'
 * @param {number} a - First number to round
 * @param {number} b - Second number to round
 * @returns {number|string} The result of the operation or 'Error' for division by zero
 */
function calculateNumber(type, a, b) {
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);

  if (type === 'SUM') {
    return roundedA + roundedB;
  }
  if (type === 'SUBTRACT') {
    return roundedA - roundedB;
  }
  if (type === 'DIVIDE') {
    if (roundedB === 0) {
      return 'Error';
    }
    return roundedA / roundedB;
  }
}

module.exports = calculateNumber;
