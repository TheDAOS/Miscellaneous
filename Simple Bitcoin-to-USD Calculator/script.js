const API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json";

document.addEventListener("DOMContentLoaded", async () => {
    // Run an asynchronous function once the DOM content has loaded
    let bitcoinPrice; // Initialize the variable
  
    try {
      const response = await fetch(API_URL);
      // Await a response from the HTTP request sent to the API URL
  
      const data = await response.json();
      // Await the json content of the response
  
      bitcoinPrice = data.bpi.USD.rate_float.toFixed(2);
      // Reassign the bitcoinPrice variable to the USD value of Bitcoin, rounded to the nearest 2 decimal places.
    } catch {
      console.log("error!"); // In case of error
    }
  
    console.log(bitcoinPrice); // Log the price in the console
});
