const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  it('should stub Utils.calculateNumber and verify console.log', function() {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnce(stub);
    sinon.assert.calledWith(stub, 'SUM', 100, 20);
    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWith(consoleSpy, 'The total is: 10');

    stub.restore();
    consoleSpy.restore();
  });
});
