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

describe('Cart page', function() {
  const BASE_URL = 'http://localhost:7865';

  it('should return status code 200 when :id is a number', function(done) {
    request.get(`${BASE_URL}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message when :id is a number', function(done) {
    request.get(`${BASE_URL}/cart/12`, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return status code 404 when :id is not a number', function(done) {
    request.get(`${BASE_URL}/cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return status code 404 for mixed alphanumeric id', function(done) {
    request.get(`${BASE_URL}/cart/12abc`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return status code 200 for large numbers', function(done) {
    request.get(`${BASE_URL}/cart/999999999`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 999999999');
      done();
    });
  });
});
