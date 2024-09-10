const API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json";

document.addEventListener("DOMContentLoaded", async () => {
    let bitcoinPrice = localStorage.getItem("lastBitcoinPrice");
    // Retrieve the last stored Bitcoin price from localStorage, if it exists
    // Note: It should be null the first time you try running the page
  
    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      bitcoinPrice = data.bpi.USD.rate_float.toFixed(2);
      // bitcoinPrice will be re-written
  
      localStorage.setItem("lastBitcoinPrice", bitcoinPrice);
      // Save most recent price to localStorage
    } catch {
      console.log("error!");
    }
  
    console.log(bitcoinPrice);
  });