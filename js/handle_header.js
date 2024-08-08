let lastScrollTop = 0;
const header = document.getElementById('header');
const headerPlaceholder = document.getElementById('header-placeholder');

window.addEventListener('scroll', function() {
    let currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScrollTop > lastScrollTop) {
        // Rolando para baixo
        header.classList.add('hidden');
    } else {
        // Rolando para cima
        header.classList.remove('hidden');
    }

    lastScrollTop = currentScrollTop <= 0 ? 0 : currentScrollTop;
});
