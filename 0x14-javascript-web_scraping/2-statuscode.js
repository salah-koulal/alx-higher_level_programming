#!/usr/bin/node

const https = require('https');

const url = 'https://example.com';

https.get(url, (response) => {
  console.log('Status code:', response.statusCode);
}).on('error', (error) => {
  console.error('Error:', error.message);
});
