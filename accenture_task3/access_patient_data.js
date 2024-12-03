const axios = require("axios");

// colleagues solution
async function getDataForEach(ids) {
  const listForData = [];
  ids.forEach(async (id) => {
    const result = await axios.get("https://reqbin.com/echo/get/json");
    listForData.push(result.data);
  });
  return listForData;
}

// my solution
async function getDataFor(ids) {
  const listForData = [];
  for (let i = 0; i < ids.length; i++) {
    const result = await axios.get("https://reqbin.com/echo/get/json");
    listForData.push(result.data);
  }
  return listForData;
}

getDataFor([1, 2, 3]).then(() => console.log("getDataFor done"));
getDataForEach([1, 2, 3]).then(() => console.log("getDataForEach done"));

/* 
comment for colleagues solution: 

The function won’t operate as intended since forEach() expects a synchronous function, not an asynchronous function which is currently in place.
Because forEach() does not wait for promises, nothing is done with the return value.

*/
