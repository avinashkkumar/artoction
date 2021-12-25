navslide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.links');
    const navLink = document.querySelectorAll('.links li');

    // class toggle for getting the burger menu
    burger.addEventListener('click',() => {
        nav.classList.toggle('navActive');

        navLink.forEach((link, index ) =>{
            if (link.style.animation) {
                link.style.animation = ""
            } else {
                link.style.animation = `navFade 0.4s ease forwards ${index / 12 + 0.1}s`;
            }
        });
        burger.classList.toggle('toggle');
    });

    // animationg the burger links 
    
}

navslide();

let slideIndex = 0;
showSlides();

// Next-previous control
function nextSlide() {
  slideIndex++;
  showSlides();
  timer = _timer; // reset timer
}

function prevSlide() {
  slideIndex--;
  showSlides();
  timer = _timer;
}

// Thumbnail image controlls
function currentSlide(n) {
  slideIndex = n - 1;
  showSlides();
  timer = _timer;
}

function showSlides() {
  let slides = document.querySelectorAll(".mySlides");
  let dots = document.querySelectorAll(".dots");

  if (slideIndex > slides.length - 1) slideIndex = 0;
  if (slideIndex < 0) slideIndex = slides.length - 1;
  
  // hide all slides
  slides.forEach((slide) => {
    slide.style.display = "none";
  });
  
  // show one slide base on index number
  slides[slideIndex].style.display = "block";
  
  dots.forEach((dot) => {
    dot.classList.remove("active");
  });
  
  dots[slideIndex].classList.add("active");
}

// autoplay slides --------
let timer = 7; // sec
const _timer = timer;

// this function runs every 1 second
setInterval(() => {
  timer--;

  if (timer < 1) {
    nextSlide();
    timer = _timer; // reset timer
  }
}, 1000); // 1sec