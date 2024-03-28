// Problem: Find the Maximum Difference
// Write a function that takes an array of numbers as input and returns the maximum difference between any two numbers in the array, where the larger number comes after the smaller number. If no such pair of numbers exists, return 0.
// For example:
// findMaxDifference([7, 2, 8, 9, 3, 1]); // Output: 7 (9 - 2)
// findMaxDifference([3, 2, 1]); // Output: 0 (no pair exists)
//
// function(arr[nums]){
// }
// return maxDifference | returns 0

let arr = [7, 2, 8, 9, 3, 1];
function findMaxDifference(arr) {
  if (arr.length < 2) return 0;

  let maxDifference = 0;
  let min = arr[0];

  for (let i = 1; i < arr.length; i++) {
    let current = arr[i];
    let difference = current - min;

    maxDifference = difference > maxDifference ? difference : maxDifference;
    min = current < min ? current : min;
  }

  return maxDifference;
}
// Test cases
console.log(findMaxDifference([7, 2, 8, 9, 3, 1]));
console.log(findMaxDifference([3, 2, 1]));


// npm install -g typescript
// npm install -g ts-node

// npm install --save-dev jest @types/jest ts-jest
  // creates node_modules folder
// create a jest.config.js file and input:
  // module.exports = {
  //   preset: 'ts-jest',
  //   testEnvironment: 'node',
  // };
// setup test files ex.. main.test.ts
  // import { } from './main';

  // test('', () => {
  //   expect().toEqual();
  // });
// use 'npx jest' to run tests

// REACT FRONTEND WITH TYPESCRIPT
// npm init -y
// npm install react react-dom typescript @types/react @types/react-dom
// Create an app.tsx file
  // App.tsx
      // import React from 'react';

      // const App: React.FC = () => {
      //   return (
      //     <div>
      //       <h1>Hello, React with TypeScript!</h1>
      //     </div>
      //   );
      // }

      // export default App;
// Create an index.html file
      // <!-- index.html -->
      // <!DOCTYPE html>
      // <html lang="en">
      // <head>
      //   <meta charset="UTF-8">
      //   <meta name="viewport" content="width=device-width, initial-scale=1.0">
      //   <title>React App</title>
      // </head>
      // <body>
      //   <div id="root"></div>
      //   <script src="dist/bundle.js"></script>
      // </body>
      // </html>
// Create a tsconfig.json file
      // {
      //   "compilerOptions": {
      //     "target": "es5",
      //     "module": "commonjs",
      //     "jsx": "react",
      //     "strict": true
      //   }
      // }
// In your package.json add:
      // "scripts": {
      //   "build": "tsc"
      // }
// npm run build
// npm install -g serve       < if you don't have serve already
// serve .
// open in browser