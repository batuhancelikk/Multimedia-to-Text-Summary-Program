chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'sendTranscript') {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, { action: 'sendTranscript', transcript: request.transcript });
      });
    }
  });
  