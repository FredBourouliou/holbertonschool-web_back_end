/**
 * Gets a payment token from the API
 * @param {boolean} success - Whether the API call should succeed
 * @returns {Promise|undefined} A resolved promise with data if success is true
 */
function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API' });
  }
}

module.exports = getPaymentTokenFromAPI;
