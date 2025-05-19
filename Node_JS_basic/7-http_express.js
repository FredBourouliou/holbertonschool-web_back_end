const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  fs.readFile(database, 'utf8', (err, data) => {
    if (err) {
      res.send('Cannot load the database');
      return;
    }
    let response = 'This is the list of our students\n';
    const lines = data.split('\n').filter(line => line.trim() !== '');
    if (lines.length === 0) {
      response += 'Number of students: 0';
      res.send(response);
      return;
    }
    const students = lines.slice(1);
    const fields = {};
    let total = 0;
    for (const line of students) {
      if (line.trim() === '') continue;
      const parts = line.split(',');
      if (parts.length < 4) continue;
      const firstname = parts[0].trim();
      const field = parts[3].trim();
      if (!fields[field]) fields[field] = [];
      fields[field].push(firstname);
      total++;
    }
    response += `Number of students: ${total}\n`;
    for (const [field, names] of Object.entries(fields)) {
      response += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }
    res.send(response.trim());
  });
});

app.listen(1245);

module.exports = app;
