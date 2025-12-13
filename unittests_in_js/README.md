# Unit Tests in JavaScript

This project covers unit testing in JavaScript using Mocha, Chai, and Sinon.

## Requirements

- Node 20.x.x
- Ubuntu 20.04

## Installation

```bash
npm install
```

For API projects (8-api, 9-api, 10-api):

```bash
cd 8-api && npm install
cd 9-api && npm install
cd 10-api && npm install
```

## Running Tests

### Unit tests (Tasks 0-7)

```bash
npm test <test-file>
```

Example:
```bash
npm test 0-calcul.test.js
npm test 1-calcul.test.js
```

### Integration tests (Tasks 8-10)

Start the server first, then run tests:

```bash
# Terminal 1
cd 8-api && node api.js

# Terminal 2
cd 8-api && npm test api.test.js
```

## Project Structure

- **Task 0**: Basic test with Mocha and Node assertion library
- **Task 1**: Combining descriptions (SUM, SUBTRACT, DIVIDE)
- **Task 2**: Basic test using Chai assertion library
- **Task 3**: Spies with Sinon
- **Task 4**: Stubs with Sinon
- **Task 5**: Hooks (beforeEach/afterEach)
- **Task 6**: Async tests with done callback
- **Task 7**: Skip failing tests
- **Task 8**: Basic Integration testing with Express
- **Task 9**: Regex integration testing
- **Task 10**: Deep equality & Post integration testing
