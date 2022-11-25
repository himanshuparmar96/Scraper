const axios = require("axios");
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const fs = require("fs/promises");

const TOTAL_PAGES = 5;
let ids = [];
const TOTAL = "176";
const STATE = "37";

(async () => {
  for (let i = 1; i <= TOTAL_PAGES; i++) {
    console.log("scrapping page", i);
    const url = `https://ngodarpan.gov.in/index.php/home/statewise_ngo/${TOTAL}/${STATE}/${i}?per_page=100`;
    const pageIds = await scrapeData(url);
    if (pageIds.length === 0) {
      break;
    }
    ids = [...ids, ...pageIds];
  }
  await fs.writeFile(`./ids/${STATE}.json`, JSON.stringify(ids));
})();

async function scrapeData(url) {
  const { data } = await axios.get(url);

  const anchors = [...data.matchAll(/show_ngo_info\(\"(\d+)\"\)/g)];

  const ids = anchors.map((anchor) => {
    return anchor[1];
  });
  return ids;
}

// scrapeData();
