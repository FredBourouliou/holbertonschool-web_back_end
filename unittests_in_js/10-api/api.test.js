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
});

describe('Available payments', function() {
  const BASE_URL = 'http://localhost:7865';

  it('should return status code 200', function(done) {
    request.get(`${BASE_URL}/available_payments`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct payment methods object', function(done) {
    request.get(`${BASE_URL}/available_payments`, (error, response, body) => {
      const expected = {
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      };
      expect(JSON.parse(body)).to.deep.equal(expected);
      done();
    });
  });

  it('should return content-type application/json', function(done) {
    request.get(`${BASE_URL}/available_payments`, (error, response, body) => {
      expect(response.headers['content-type']).to.include('application/json');
      done();
    });
  });
});

describe('Login', function() {
  const BASE_URL = 'http://localhost:7865';

  it('should return status code 200', function(done) {
    const options = {
      url: `${BASE_URL}/login`,
      method: 'POST',
      json: { userName: 'Betty' },
    };
    request(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return welcome message with username', function(done) {
    const options = {
      url: `${BASE_URL}/login`,
      method: 'POST',
      json: { userName: 'Betty' },
    };
    request(options, (error, response, body) => {
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });

  it('should return welcome message with different username', function(done) {
    const options = {
      url: `${BASE_URL}/login`,
      method: 'POST',
      json: { userName: 'John' },
    };
    request(options, (error, response, body) => {
      expect(body).to.equal('Welcome John');
      done();
    });
  });
});
