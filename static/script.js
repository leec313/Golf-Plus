// This displays the newsletter after 5 seconds of page load
// Then if the user enters an email and submits, or closes 
// the modal, it will not show again by using the browser cookies 

document.addEventListener("DOMContentLoaded", function () {
    // Check if the modal has been shown before
    if (getCookie('modalShown') !== 'true') {
        setTimeout(openModal, 5000);
    }
});

function openModal() {
    document.getElementById('newsletter-modal').style.display = 'block';
    // Set a cookie to indicate that the modal has been shown
    document.cookie = 'modalShown=true; expires=Fri, 31 Dec 9999 23:59:59 GMT';
}

function closeModal() {
    document.getElementById('newsletter-modal').style.display = 'none';
}

window.onclick = function (event) {
    var modal = document.getElementById('newsletter-modal');
    if (event.target === modal) {
        closeModal();
    }
};

// This is the function that get's the user's cookie info
function getCookie(name) {
    var cookieArr = document.cookie.split(';');
    for (var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split('=');
        if (cookiePair[0].trim() === name) {
            return cookiePair[1];
        }
    }
    return null;
}

// timeout function for alert messages
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);


// For index.html .hero-carousel slideshow
document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector('.hero-carousel');
    const slides = carousel.querySelectorAll('img');

    let currentIndex = 0;

    function showImage(index) {
        slides.forEach((slide, i) => {
            if (i === index) {
                slide.classList.add('active');
                slide.style.display = 'block'; // Show the active image
            } else {
                slide.classList.remove('active');
                slide.style.display = 'none'; // Hide non-active images
            }
        });
    }

    // Show the first image initially
    showImage(currentIndex);

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showImage(currentIndex);
    }

    // Change slide every 3 seconds
    setInterval(nextSlide, 5000);
});