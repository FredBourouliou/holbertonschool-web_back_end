const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const fields = {};
      let total = 0;

      for (const student of students) {
        const parts = student.split(',');
        if (parts.length >= 4) {
          const firstname = parts[0].trim();
          const field = parts[3].trim();

          if (!fields[field]) {
            fields[field] = [];
          }

          fields[field].push(firstname);
          total += 1;
        }
      }

      console.log(`Number of students: ${total}`);
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const list = fields[field].join(', ');
          console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
        }
      }

      resolve();
    });
  });
}

module.exports = countStudents;
