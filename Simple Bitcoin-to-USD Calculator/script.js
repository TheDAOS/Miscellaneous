const API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json";

document.addEventListener("DOMContentLoaded", async () => {
    const main = document.getElementById("main");
    const bitcoinPriceElement = document.getElementById("bitcoinPrice");
    const bitcoinAmountInput = document.getElementById("bitcoinAmount");
    const calculateBtn = document.getElementById("calculateBtn");
    const usdAmountElement = document.getElementById("usdAmount");
  
    let bitcoinPrice = localStorage.getItem("lastBitcoinPrice");
  
    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      bitcoinPrice = data.bpi.USD.rate_float.toFixed(2);
      localStorage.setItem("lastBitcoinPrice", bitcoinPrice);
  
      bitcoinPriceElement.textContent = bitcoinPrice;
      // Set the text content of bitcoinPriceElement to the current bitcoinPrice
    } catch {
      if (bitcoinPrice) {
        // If there's an existing bitcoinPrice in localStorage...
        bitcoinPriceElement.textContent = bitcoinPrice;
        // ...display whatever is saved localStorage
      } else {
        main.innerHTML = "<p>Could not fetch Bitcoin price :(</p>";
        return;
      }
    }
  
    console.log(bitcoinPrice);
  });