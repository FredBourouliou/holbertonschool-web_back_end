# Node.js Basics

This project contains exercises to learn the fundamentals of Node.js development.

## Learning Objectives

- Run JavaScript using Node.js
- Use Node.js modules
- Use specific Node.js modules to read files
- Use process to access command line arguments and the environment
- Create a small HTTP server using Node.js
- Create a small HTTP server using Express.js
- Create advanced routes with Express.js
- Use ES6 with Node.js with Babel-node
- Use Nodemon to develop faster

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using node (version 20.x.x)
- All files should end with a new line
- Code should use the `.js` extension
- Code will be tested using Jest and the command `npm run test`
- Code will be verified against lint using ESLint
- All functions/classes must be exported using: `module.exports = myFunction;`

## Files

### Basic Tasks
- `0-console.js` - Basic console output function
- `1-stdin.js` - Reading from stdin
- `2-read_file.js` - Reading files synchronously
- `3-read_file_async.js` - Reading files asynchronously
- `4-http.js` - Basic HTTP server using Node.js http module
- `5-http.js` - HTTP server with routing using Node.js http module
- `6-http_express.js` - Basic HTTP server using Express
- `7-http_express.js` - HTTP server with routing using Express

### Full Server
- `full_server/` - Complete Express server with proper structure
  - `utils.js` - Database reading utility
  - `controllers/AppController.js` - Application controller
  - `controllers/StudentsController.js` - Students controller
  - `routes/index.js` - Route definitions
  - `server.js` - Main server file

## Installation

```bash
npm install
```

## Usage

### Running individual files
```bash
node 0-console.js
node 1-stdin.js
node 2-read_file.js database.csv
# etc.
```

### Running servers
```bash
# Basic HTTP server
node 4-http.js

# Express servers
node 6-http_express.js
node 7-http_express.js database.csv

# Full server with Babel
npm run dev
```

## Testing

```bash
npm run test
npm run check-lint
npm run full-test
```

## Database

The project uses `database.csv` which contains student information with fields:
- firstname
- lastname  
- age
- field (CS or SWE)