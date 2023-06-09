document.addEventListener('DOMContentLoaded', function () {
    var button = document.querySelector('button');
    button.addEventListener('click', function () {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, { action: 'summarize' });
      });
    });
  });
  
  chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'sendTranscript') {
      var ul = document.querySelector('ul');
      ul.innerHTML = '';
  
      request.transcript.forEach(function (line) {
        var template = document.getElementById('li_template');
        var clone = template.content.cloneNode(true);
  
        var title = clone.querySelector('.title');
        title.textContent = line.title;
  
        var pathname = clone.querySelector('.pathname');
        pathname.textContent = line.pathname;
  
        ul.appendChild(clone);
      });
    }
  });
  