# Queuing System in JS

This project implements a queuing system using Redis and Node.js.

## Learning Objectives

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

## Requirements

- Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- Code uses the js extension

## Setup

### Install Redis

```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
```

### Start Redis Server

```bash
src/redis-server &
```

### Test Redis

```bash
src/redis-cli ping
# Should return: PONG
```

### Set and Get Values

```bash
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```

### Install Node Dependencies

```bash
npm install
```

## Files

- `dump.rdb` - Redis database dump containing the Holberton key
- `package.json` - Node.js project configuration
- `.babelrc` - Babel configuration for ES6 support
