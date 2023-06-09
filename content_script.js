chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'summarize') {
      var transcript = [];
  
      var videoElement = document.querySelector('video');
      if (videoElement) {
        var captions = Array.from(document.querySelectorAll('.cue-group-start-offset'));
        captions.forEach(function (caption) {
          var title = caption.querySelector('.cue-group-start-offset > span').textContent;
          var pathname = window.location.pathname;
  
          transcript.push({ title: title, pathname: pathname });
        });
      }
  
      chrome.runtime.sendMessage({ action: 'sendTranscript', transcript: transcript });
    }
  });
  