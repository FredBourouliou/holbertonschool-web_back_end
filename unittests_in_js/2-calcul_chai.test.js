const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return 6 when adding 1.4 and 4.5', function() {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 4 when adding 1 and 3', function() {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    });

    it('should return 5 when adding 1 and 3.7', function() {
      expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    });

    it('should return 5 when adding 1.2 and 3.7', function() {
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    });

    it('should return 6 when adding 1.5 and 3.7', function() {
      expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
    });

    it('should return 0 when adding 0 and 0', function() {
      expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    });

    it('should return -4 when adding -1 and -3', function() {
      expect(calculateNumber('SUM', -1, -3)).to.equal(-4);
    });

    it('should return 0 when adding 0.4 and 0.4', function() {
      expect(calculateNumber('SUM', 0.4, 0.4)).to.equal(0);
    });

    it('should return 2 when adding 0.5 and 0.5', function() {
      expect(calculateNumber('SUM', 0.5, 0.5)).to.equal(2);
    });
  });

  describe('SUBTRACT', function() {
    it('should return -4 when subtracting 4.5 from 1.4', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return 0 when subtracting 1 from 1', function() {
      expect(calculateNumber('SUBTRACT', 1, 1)).to.equal(0);
    });

    it('should return -2 when subtracting 3 from 1', function() {
      expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    });

    it('should return 2 when subtracting 1 from 3', function() {
      expect(calculateNumber('SUBTRACT', 3, 1)).to.equal(2);
    });

    it('should return -3 when subtracting 3.7 from 1.2', function() {
      expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
    });

    it('should return 0 when subtracting 0 from 0', function() {
      expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    });

    it('should return 2 when subtracting -3 from -1', function() {
      expect(calculateNumber('SUBTRACT', -1, -3)).to.equal(2);
    });

    it('should return -4 when subtracting 3 from -1', function() {
      expect(calculateNumber('SUBTRACT', -1, 3)).to.equal(-4);
    });

    it('should return 0 when subtracting 0.4 from 0.4', function() {
      expect(calculateNumber('SUBTRACT', 0.4, 0.4)).to.equal(0);
    });
  });

  describe('DIVIDE', function() {
    it('should return 0.2 when dividing 1.4 by 4.5', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return Error when dividing by 0', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return Error when dividing by 0.4 (rounds to 0)', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0.4)).to.equal('Error');
    });

    it('should return 2 when dividing 4 by 2', function() {
      expect(calculateNumber('DIVIDE', 4, 2)).to.equal(2);
    });

    it('should return 2.5 when dividing 5 by 2', function() {
      expect(calculateNumber('DIVIDE', 5, 2)).to.equal(2.5);
    });

    it('should return -2 when dividing -4 by 2', function() {
      expect(calculateNumber('DIVIDE', -4, 2)).to.equal(-2);
    });

    it('should return -2 when dividing 4 by -2', function() {
      expect(calculateNumber('DIVIDE', 4, -2)).to.equal(-2);
    });

    it('should return 2 when dividing -4 by -2', function() {
      expect(calculateNumber('DIVIDE', -4, -2)).to.equal(2);
    });

    it('should return 1 when dividing 1 by 1', function() {
      expect(calculateNumber('DIVIDE', 1, 1)).to.equal(1);
    });

    it('should return 0 when dividing 0 by 5', function() {
      expect(calculateNumber('DIVIDE', 0, 5)).to.equal(0);
    });

    it('should return 4 when dividing 8.4 by 2.4', function() {
      expect(calculateNumber('DIVIDE', 8.4, 2.4)).to.equal(4);
    });
  });

  describe('Rounding behavior for all types', function() {
    it('should round 1.4 down to 1 for SUM', function() {
      expect(calculateNumber('SUM', 1.4, 0)).to.equal(1);
    });

    it('should round 1.5 up to 2 for SUM', function() {
      expect(calculateNumber('SUM', 1.5, 0)).to.equal(2);
    });

    it('should round both numbers for SUBTRACT', function() {
      expect(calculateNumber('SUBTRACT', 2.6, 1.4)).to.equal(2);
    });

    it('should round both numbers for DIVIDE', function() {
      expect(calculateNumber('DIVIDE', 5.5, 2.4)).to.equal(3);
    });
  });
});
