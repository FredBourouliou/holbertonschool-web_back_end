export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const Species = Symbol('Species');
    this[Species] = this.constructor;
    return new this[Species]();
  }
}
