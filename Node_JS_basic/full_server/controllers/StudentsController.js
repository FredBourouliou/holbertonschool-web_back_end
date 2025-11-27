import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const path = process.argv[2];

    readDatabase(path)
      .then((studentByField) => {
        const response = ['This is the list of our students'];
        const sortedFields = Object.keys(studentByField)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        for (const field of sortedFields) {
          const list = studentByField[field];
          response.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        }

        res.status(200).send(response.join('\n'));
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const path = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(path)
      .then((studentByField) => {
        const list = studentByField[major];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
