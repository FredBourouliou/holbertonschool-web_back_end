const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
  describe('Basic addition', function() {
    it('should return 4 when inputs are 1 and 3', function() {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should return 5 when inputs are 1 and 3.7', function() {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });

    it('should return 5 when inputs are 1.2 and 3.7', function() {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });

    it('should return 6 when inputs are 1.5 and 3.7', function() {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });

  describe('Rounding behavior', function() {
    it('should round down 1.2 to 1', function() {
      assert.strictEqual(calculateNumber(1.2, 0), 1);
    });

    it('should round up 1.5 to 2', function() {
      assert.strictEqual(calculateNumber(1.5, 0), 2);
    });

    it('should round down 1.4 to 1', function() {
      assert.strictEqual(calculateNumber(1.4, 0), 1);
    });

    it('should round up 2.5 to 3', function() {
      assert.strictEqual(calculateNumber(2.5, 0), 3);
    });

    it('should round 2.4999 down to 2', function() {
      assert.strictEqual(calculateNumber(2.4999, 0), 2);
    });

    it('should round 2.5001 up to 3', function() {
      assert.strictEqual(calculateNumber(2.5001, 0), 3);
    });
  });

  describe('Negative numbers', function() {
    it('should return -4 when inputs are -1 and -3', function() {
      assert.strictEqual(calculateNumber(-1, -3), -4);
    });

    it('should return -5 when inputs are -1.4 and -3.6', function() {
      assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
    });

    it('should return -4 when inputs are -1.5 and -3.5', function() {
      assert.strictEqual(calculateNumber(-1.5, -3.5), -4);
    });

    it('should return 0 when inputs are -2.5 and 2.5', function() {
      assert.strictEqual(calculateNumber(-2.5, 2.5), 1);
    });
  });

  describe('Zero handling', function() {
    it('should return 0 when both inputs are 0', function() {
      assert.strictEqual(calculateNumber(0, 0), 0);
    });

    it('should return 0 when inputs are 0.4 and 0.4', function() {
      assert.strictEqual(calculateNumber(0.4, 0.4), 0);
    });

    it('should return 0 when inputs are 0.4 and -0.4', function() {
      assert.strictEqual(calculateNumber(0.4, -0.4), 0);
    });

    it('should return 1 when inputs are 0.5 and 0.4', function() {
      assert.strictEqual(calculateNumber(0.5, 0.4), 1);
    });
  });

  describe('Large numbers', function() {
    it('should handle large positive numbers', function() {
      assert.strictEqual(calculateNumber(1000000.4, 1000000.5), 2000001);
    });

    it('should handle large negative numbers', function() {
      assert.strictEqual(calculateNumber(-1000000.4, -1000000.5), -2000000);
    });
  });

  describe('Edge cases with decimal precision', function() {
    it('should return 2 when inputs are 0.6 and 0.6', function() {
      assert.strictEqual(calculateNumber(0.6, 0.6), 2);
    });

    it('should return 0 when inputs are 0.1 and 0.1', function() {
      assert.strictEqual(calculateNumber(0.1, 0.1), 0);
    });

    it('should return 0 when inputs are 0.49 and 0.49', function() {
      assert.strictEqual(calculateNumber(0.49, 0.49), 0);
    });

    it('should return 2 when inputs are 0.51 and 0.51', function() {
      assert.strictEqual(calculateNumber(0.51, 0.51), 2);
    });
  });

  describe('Mixed positive and negative', function() {
    it('should return 2 when inputs are 5.5 and -3.5', function() {
      assert.strictEqual(calculateNumber(5.5, -3.5), 3);
    });

    it('should return -2 when inputs are -5.5 and 3.5', function() {
      assert.strictEqual(calculateNumber(-5.5, 3.5), -1);
    });
  });
});
