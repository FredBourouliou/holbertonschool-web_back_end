import { readDatabase } from '../utils.js';

class StudentsController {
  static getAllStudents(req, res) {
    // Use first command-line argument that's not the script name as database path
    const database = process.argv.length > 2 ? process.argv[2] : '';
    
    readDatabase(database)
      .then((fields) => {
        let response = 'This is the list of our students\n';
        // Sort fields case-insensitive alphabetical order
        const sortedFields = Object.keys(fields).sort((a, b) => 
          a.toLowerCase().localeCompare(b.toLowerCase())
        );
        
        // Calculate total number of students across all fields
        const total = Object.values(fields).reduce(
          (sum, students) => sum + students.length, 0
        );
        
        response += `Number of students: ${total}\n`;
        
        // Add each field's student count and names
        for (const field of sortedFields) {
          response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
        }
        
        res.status(200).send(response.trim());
      })
      .catch((error) => {
        res.status(500).send(error.message || 'Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    // Use first command-line argument that's not the script name as database path
    const database = process.argv.length > 2 ? process.argv[2] : '';
    const { major } = req.params;
    
    // Validate major parameter
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }
    
    readDatabase(database)
      .then((fields) => {
        // Handle the case where the field doesn't exist
        if (!fields[major] || fields[major].length === 0) {
          return res.status(200).send('List:');
        }
        
        res.status(200).send(`List: ${fields[major].join(', ')}`);
      })
      .catch((error) => {
        res.status(500).send(error.message || 'Cannot load the database');
      });
  }
}

export default StudentsController; 