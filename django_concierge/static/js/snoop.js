document.addEventListener("DOMContentLoaded", function () {
    data = {
        referrer: document.referrer,
        location: document.location.href,
        title: document.title,
        userAgent: navigator.userAgent,
        screenWidth: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
        screenHeight: window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight,
    };
    fetch(concierge.api_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': concierge.csrf_token,
        },
        body: JSON.stringify(data),
    });
});