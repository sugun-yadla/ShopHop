// Add a listener for the message so we can populate the HTML page
chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
    if (message.action === "showPopup") {
      const results = message.results;

      const resultsContainer = document.getElementById('results-container');
      resultsContainer.innerHTML = ''; // Clear previous results

      results.forEach(item => {
        const resultItem = document.createElement('div');
        resultItem.classList.add('result-item');
        resultItem.innerHTML = `
            <a href="${item.URL}">
                <h3>${item.Product} (${item.Quantity})</h3>
                <p>Price: $ ${item.Price} </p>
                <p>Effective: ${item.price_currency} ${item.price_per_unit} per ${item.st_unit}</p>
                <img src="${item.Image}" alt="${item.Product}" width="100" />
            </a>
        `;
        resultsContainer.appendChild(resultItem);
      });
    }
    return true;
});
