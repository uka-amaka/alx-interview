#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(movieUrl, async function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    for (const characterUrl of characters) {
      try {
        const characterResponse = await new Promise((resolve, reject) => {
          request(characterUrl, (err, res, html) => {
            if (err) {
              reject(err);
            } else {
              resolve(JSON.parse(html).name);
            }
          });
        });
        
        console.log(characterResponse);
      } catch (err) {
        console.error("Error:", err);
      }
    }
  }
});
