console.log("ShopHop extension is running");

BACKEND_URL = "http://127.0.0.1:8000"

var lastUrl = "";
var currentUrl = "";

const ELEMENT_IDS = {
    "Target": "#search",
    "Aldi": "#search-bar-input",
    "Walmart": 'input[aria-label="Search"]'
}

const QUERY_PARAM = {
    "Target": "searchTerm",
    "Aldi": "q",
    "Walmart": 'q'
}

async function fetchWebsiteData() {
    if (currentUrl == lastUrl) {
        return;
    }

    lastUrl = currentUrl;
    console.log("currentUrl:", currentUrl)

    var store = "";
    if (currentUrl.includes("https://www.walmart.com")) {
        store = "Walmart";
    } else if (currentUrl.includes("https://new.aldi.us")) {
        store = "Aldi";
    } else if (currentUrl.includes("https://www.target.com")) {
        store = "Target";
    }

    const searchQuery = await scrapeSearchQuery(ELEMENT_IDS[store]);
    if (searchQuery === "") {
        console.log("Search query empty");
        return;
    } else {
        console.log("Searching for", searchQuery)
    }

    const results = await fetchSearchResults(searchQuery);
    await showResults(results, store);
}


async function scrapeSearchQuery(elementId) {
    const searchInput = document.querySelector(elementId);
    if (searchInput) {
        return searchInput.value;
    } else {
        console.log("Search input not found.");
        return "";
    }
}


async function fetchSearchResults(searchQuery) {
    console.log("Fetching price comparison")
    const url = `${BACKEND_URL}/api/products/${searchQuery}`;

    const response = await fetch(url);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }

    results = await response.json();
    return results;
}


async function showResults(results, currentWebsite) {
    console.log('Results:', results);

    // This condition means it's cheaper elsewhere
    if (results[0]["store"] != currentWebsite) {
        chrome.runtime.sendMessage({ action: "showPopup", results: results }, response => {});
    } else {
        console.log("This website has the cheapest price")
    }
}


document.addEventListener("DOMContentLoaded", async () => {
    await fetchWebsiteData();

    // Create an observer to watch for URL changes to the document
    // This lets us rerun the price comparison function when the user searches for something else
    const observer = new MutationObserver(async () => {
        currentUrl = window.location.href;
        await fetchWebsiteData();
    });

    observer.observe(document, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ['href', 'src'],
    });
});
