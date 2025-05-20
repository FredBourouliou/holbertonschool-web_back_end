const http = require('http');
const fs = require('fs');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;
    res.write('This is the list of our students\n');
    countStudents(database)
      .then(() => {
        // countStudents already logs to console, but we need to capture output for HTTP response
        // So, let's reimplement the logic here to write to res instead of console
        fs.readFile(database, 'utf8', (err, data) => {
          if (err) {
            res.end('Cannot load the database');
            return;
          }
          const lines = data.split('\n').filter((line) => line.trim() !== '');
          if (lines.length === 0) {
            res.end('Number of students: 0');
            return;
          }
          const students = lines.slice(1);
          const fields = {};
          let total = 0;
          for (const line of students) {
            if (line.trim() !== '') {
              const parts = line.split(',');
              if (parts.length >= 4) {
                const firstname = parts[0].trim();
                const field = parts[3].trim();
                if (!fields[field]) fields[field] = [];
                fields[field].push(firstname);
                total += 1;
              }
            }
          }
          res.write(`Number of students: ${total}\n`);
          for (const [field, names] of Object.entries(fields)) {
            res.write(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`);
          }
          res.end();
        });
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
