## JavaScript
---

### Solved 3/18/24
```
const createCounter = function(init) {
  let currentValue = init;
  return {
    increment: () => {
      return currentValue += 1
    },
    decrement: () => {
      return currentValue -= 1
    },
    reset: () => {
      currentValue = init;
      return currentValue
    }
  }
};
```
### Solved 3/18/24
```
const createCounter2 = function(n) {
  let count = n;
  return function() {
    count += 1;
    return (count - 1);
  };
};
```
### Solved 3/19/24
```
const expect = function(val) {
  return {
    toBe: (val2) => {
      if (val === val2) {
        return true;
      } else {
        throw new Error('Not Equal');
      }
    },
    notToBe: (val2) => {
      if (val !== val2) {
        return true;
      } else {
        throw new Error('Equal');
      }
    }
  };
};
```
/**
* @param {string} val
* @return {Object}
* expect(5).toBe(5); // true
* expect(5).notToBe(5); // throws "Equal"
*/
### Solved 3/21/24
```
const filter = function(arr, fn) {
  let filteredArr = [];
  for(let i = 0; i < arr.length; i++) {
    fn(arr[i], i) ? filteredArr.push(arr[i]) : null
  }
  return filteredArr;
};
```
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
*/
// >> int arr
// >> filtering function, fn
// << return filteredArr
// filteredArr only where fn(arr[i], i) = True

---
## TypeScript
---

### Solved 3/25/24
```
function isPalindrome(x: number): boolean {
  let numArr: string = x.toString();
  let i: number = 0;
  let j: number = numArr.length - 1;

  if (x < 0) {
    return false;
  }

  while (i < j) {
    if (numArr[i] !== numArr[j]) {
      return false;
    }
    i++;
    j--;
  }

  return true;
}
```
// >> x: int
// << if(x === palindrome) {return true}
// >> else(return false)
// for loop (i) starting from x[0]
// for loop (j) starting from x.length - 1
// if (i !== j) {return false}
### Solved 3/26/24
```
async function sleep(millis: number): Promise<void> {
  if(millis < 0){
    return null
  }
  return new Promise<void>((resolve) => {
    setTimeout(() => {
        resolve();
    }, millis)
  })
}
```
/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
// >> millis: number (positive)
// async function sleep(millis: number)
### Solved 3/27/24
```
function romanToInt(s: string): number {
  let symbolData = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  };

  let sum: number = 0;
  let prevValue: number = 0;
  s.split('').forEach((symbol: string) => {
    let value = symbolData[symbol];
    sum += value;
    if (prevValue < value) {
      sum -= 2 * prevValue;
    }
    prevValue = value;
  });

  return sum;
}
```
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000
// >> s: string
// << number
// 1. split the string
// 2. compare the symbol with array.includes
// 3. create dictionary to hold symbols and values
// 4. look up dictionary[s: string]
// 5. get the total by repeating step 4 over the whole string
### Solved 3/28/24
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
function argumentsLength(...args: JSONValue[]): number {
  let argsPassed: number = 0;
  args.forEach(arg => {
    argsPassed++
  });
  return argsPassed;
};
/**
* argumentsLength(1, 2, 3); // 3
*/
// function argumentsLength
// << args: number