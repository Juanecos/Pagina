const preferedColorScheme = window.matchMedia('prefers-color-scheme:dark').matches ? 'dark' : 'light';
const slider = document.getElementById('slider');

const setTheme = (theme) => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);


}

setTheme{localStorage.setItem('theme') || preferedColorScheme};