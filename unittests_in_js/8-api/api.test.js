const request = require('request');
const { expect } = require('chai');

describe('Index page', function() {
  const BASE_URL = 'http://localhost:7865';

  it('should return status code 200', function(done) {
    request.get(BASE_URL, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message', function(done) {
    request.get(BASE_URL, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should return content-type text/html', function(done) {
    request.get(BASE_URL, (error, response, body) => {
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });
});
