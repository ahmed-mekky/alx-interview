#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2, 3);

const fetchCharacterName = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterData = JSON.parse(body);
      resolve(characterData.name);
    });
  });
};

request(`https://swapi-api.alx-tools.com/api/films/${args}`, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  for (const characterUrl of characters) {
    const characterName = await fetchCharacterName(characterUrl);
    console.log(characterName);
  }
});
