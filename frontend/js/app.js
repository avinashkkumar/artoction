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