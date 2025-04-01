# ES6 Promises

This project demonstrates the use of ES6 Promises in JavaScript. It covers various Promise-related concepts including:

- Creating and working with Promises
- Promise chaining with then, catch, and finally
- Promise.all and Promise.race
- Error handling with try/catch
- Async/await syntax

## Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using Node.js 20.x and npm 9.x
- All files should end with a new line
- Code must use the .js extension
- Code tested with Jest and verified with ESLint
- All functions must be exported

## Setup

```bash
# Install NodeJS 20.x
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y

# Verify versions
nodejs -v
npm -v

# Install dependencies
npm install
```

## Testing

```bash
# Run tests
npm test

# Run linter
npm run lint
``` 