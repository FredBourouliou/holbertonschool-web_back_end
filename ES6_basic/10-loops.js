export default function appendToEachArrayValue(array, appendString) {
  const newArray = [...array];
  for (let i = 0; i < newArray.length; i += 1) {
    newArray[i] = appendString + newArray[i];
  }
  return newArray;
}
