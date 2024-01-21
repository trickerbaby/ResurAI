const Tesseract = require('tesseract.js');
const fs = require('fs');

// Specify the path to the image file
const imagePath = 'resume.png';

// Read the image file
const imageBuffer = fs.readFileSync(imagePath);

// Perform OCR using Tesseract
Tesseract.recognize(
  imageBuffer,
  'eng', // Language code for English. You can change it as needed.
  { logger: info => console.log(info) } // Optional logger to see progress
).then(({ data: { text } }) => {
  // Output the extracted text
  console.log('Extracted Text:', text);
}).catch(error => {
  console.error('Error:', error.message || error);
});
