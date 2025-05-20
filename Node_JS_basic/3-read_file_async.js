const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      
      try {
        // Split into lines and filter out empty lines
        const lines = data.split('\n').filter(line => line.trim() !== '');
        
        // Handle empty file
        if (lines.length <= 1) { // If there's only header or less
          console.log('Number of students: 0');
          resolve();
          return;
        }
        
        // The first line is the header
        const students = lines.slice(1);
        
        // Group students by field
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
        
        // Output the results
        console.log(`Number of students: ${total}`);
        for (const [field, names] of Object.entries(fields)) {
          console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }
        resolve();
      } catch (error) {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

module.exports = countStudents;
