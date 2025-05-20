const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  res.write('This is the list of our students\n');

  countStudents(database)
    .then(() => {
      res.end();
    })
    .catch((error) => {
      res.end(error.message);
    });
});

app.listen(1245);

module.exports = app;
