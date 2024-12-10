chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "showPopup") {
        chrome.action.openPopup();

        // Allow a delay of 1500ms for the listener to be set up before we send a message
        setTimeout(() => {
            chrome.runtime.sendMessage({ action: "showPopup", results: message.results });
        }, 1500);

        setTimeout(() => {
            sendResponse({ status: "success", message: "Popup opened and results sent." });
        }, 1000);

      return true;
    }
});
