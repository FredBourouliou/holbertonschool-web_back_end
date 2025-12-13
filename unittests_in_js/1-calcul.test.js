const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return 6 when adding 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return 4 when adding 1 and 3', function() {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });

    it('should return 5 when adding 1 and 3.7', function() {
      assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    });

    it('should return 5 when adding 1.2 and 3.7', function() {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });

    it('should return 6 when adding 1.5 and 3.7', function() {
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    });

    it('should return 0 when adding 0 and 0', function() {
      assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    });

    it('should return -4 when adding -1 and -3', function() {
      assert.strictEqual(calculateNumber('SUM', -1, -3), -4);
    });

    it('should return 0 when adding 0.4 and 0.4', function() {
      assert.strictEqual(calculateNumber('SUM', 0.4, 0.4), 0);
    });

    it('should return 2 when adding 0.5 and 0.5', function() {
      assert.strictEqual(calculateNumber('SUM', 0.5, 0.5), 2);
    });
  });

  describe('SUBTRACT', function() {
    it('should return -4 when subtracting 4.5 from 1.4', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return 0 when subtracting 1 from 1', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1, 1), 0);
    });

    it('should return -2 when subtracting 3 from 1', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
    });

    it('should return 2 when subtracting 1 from 3', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 3, 1), 2);
    });

    it('should return -3 when subtracting 3.7 from 1.2', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
    });

    it('should return 0 when subtracting 0 from 0', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
    });

    it('should return 2 when subtracting -3 from -1', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', -1, -3), 2);
    });

    it('should return -4 when subtracting 3 from -1', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', -1, 3), -4);
    });

    it('should return 0 when subtracting 0.4 from 0.4', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 0.4, 0.4), 0);
    });
  });

  describe('DIVIDE', function() {
    it('should return 0.2 when dividing 1.4 by 4.5', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return Error when dividing by 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return Error when dividing by 0.4 (rounds to 0)', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
    });

    it('should return 2 when dividing 4 by 2', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 4, 2), 2);
    });

    it('should return 2.5 when dividing 5 by 2', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 5, 2), 2.5);
    });

    it('should return -2 when dividing -4 by 2', function() {
      assert.strictEqual(calculateNumber('DIVIDE', -4, 2), -2);
    });

    it('should return -2 when dividing 4 by -2', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 4, -2), -2);
    });

    it('should return 2 when dividing -4 by -2', function() {
      assert.strictEqual(calculateNumber('DIVIDE', -4, -2), 2);
    });

    it('should return 1 when dividing 1 by 1', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1, 1), 1);
    });

    it('should return 0 when dividing 0 by 5', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 0, 5), 0);
    });

    it('should return 4 when dividing 8.4 by 2.4', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 8.4, 2.4), 4);
    });
  });

  describe('Rounding behavior for all types', function() {
    it('should round 1.4 down to 1 for SUM', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 0), 1);
    });

    it('should round 1.5 up to 2 for SUM', function() {
      assert.strictEqual(calculateNumber('SUM', 1.5, 0), 2);
    });

    it('should round both numbers for SUBTRACT', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.6, 1.4), 2);
    });

    it('should round both numbers for DIVIDE', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 5.5, 2.4), 3);
    });
  });
});
