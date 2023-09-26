document.addEventListener('DOMContentLoaded', function () {
      
    const preferedColorScheme = window.matchMedia('prefers-color-scheme:dark').matches ? 'dark' : 'light';
    const slider = document.getElementById('slider');


    const setTheme = (theme) => {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);

        if (theme === 'dark') {
            slider.checked = true; // Marcar el input si el tema es "dark"
          } else {
            slider.checked = false; // Desmarcar el input si el tema no es "dark" o no se encuentra en localStorage
          }

    }


    slider.addEventListener('change', ()=>{


        let switchToTheme = localStorage.getItem('theme') === 'dark' ? 'light' : 'dark';
        setTheme(switchToTheme);
        
    

    

    })

    setTheme(localStorage.getItem('theme') || preferedColorScheme);
    

});


