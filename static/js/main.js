const openIcon = document.querySelector('.learn-icon');
const linksWrapper = document.querySelector('.learn-links-wrapper');
const backdrop = document.querySelector('.learn-backdrop');
const closeIcon = document.querySelector('.learn-close-btn');

openIcon.addEventListener('click', () => {
    linksWrapper.classList.add('open');
});


closeIcon.addEventListener('click', () => {
    linksWrapper.classList.remove('open');
});

backdrop.addEventListener('click', () => {
    linksWrapper.classList.remove('open');
});