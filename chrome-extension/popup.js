// Add a listener for the message so we can populate the HTML page
chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
    if (message.action === "showPopup") {
        const results = message.results;

        const resultsContainer = document.getElementById('results-container');
        resultsContainer.innerHTML = ''; // Clear previous results

        const STORE_LOGO_URLS = {
            'Aldi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/AldiWorldwideLogo.svg/400px-AldiWorldwideLogo.svg.png',
            'Walmart': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Walmart_Spark.svg/451px-Walmart_Spark.svg.png',
            'Target': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Target_logo.svg/361px-Target_logo.svg.png',
        }

        results.forEach(item => {
            const resultItem = document.createElement('div');

            if (item.price_per_unit < 0.1) {
                item.price_currency = '¢';
                item.price_per_unit = `${(100 * item.price_per_unit).toFixed(2)}`
            } else if (item.price_per_unit < 1) {
                item.price_currency = '¢';
                item.price_per_unit = `${(100 * item.price_per_unit).toFixed(2)}`
            } else {
                item.price_per_unit = `${item.price_per_unit.toFixed(2)}`
            }

            resultItem.classList.add('result-item');
            resultItem.innerHTML = `
            <a href="${item.URL}">
                <table>
                    <tr>
                        <td rowspan="3"><img src="${STORE_LOGO_URLS[item['store']]}" height="12"/></td>
                        <th>${item.Product} (${item.Quantity})</th>
                        <td rowspan="3"><img src="${item.Image}" height="36"></img></td>
                    <tr>
                        <td>Price: $ ${item.Price}</td>
                    <tr>
                        <td>Effective: ${item.price_currency} ${item.price_per_unit} per ${item.st_unit}</td>
                    </tr>
                </table>
            </a>
            `;

            resultsContainer.appendChild(resultItem);
        });
    }
    return true;
});
