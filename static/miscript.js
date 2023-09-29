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


  slider.addEventListener('change', () => {


    let switchToTheme = localStorage.getItem('theme') === 'dark' ? 'light' : 'dark';
    setTheme(switchToTheme);





  })

  setTheme(localStorage.getItem('theme') || preferedColorScheme);




});


document.addEventListener('DOMContentLoaded', function () {
  //   // Tu código JavaScript aquí




  // let pahoConfig = {
  // hostname: "6eef623dbafd42238df342ee595d441a.s1.eu.hivemq.cloud",  //The hostname is the url, under which your FROST-Server resides.
  // port: "8883",           //The port number is the WebSocket-Port,
  //                         // not (!) the MQTT-Port. This is a Paho characteristic.
  // clientId: "cliente-web"    //Should be unique for every of your client connections.
  // }

  const serverUrl = "wss://6eef623dbafd42238df342ee595d441a.s1.eu.hivemq.cloud:8884/mqtt"; // Reemplaza con la URL de tu servidor MQTT
  const clientId = "cliente-web";

  // Configura las credenciales de autenticación

  client = new Paho.MQTT.Client(serverUrl, clientId);
  // const client = new Paho.MQTT.Client(pahoConfig.hostname, Number(pahoConfig.port), pahoConfig.clientId);
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;

  client.connect({
    userName: "juan-camilo",
    password: "iNM123456789",
    onSuccess: onConnect


  });

  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Connected with Server");
    client.subscribe("temperatura1");

  }

  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:" + responseObject.errorMessage);
    }
  }

  // while(!client.onMessageArrived){
  //   const time= 15000;
  //   setTimeout(function () {
  //     j = "Desconectado"; 
  //     console.log("Variable no encontrada");
  //     const datoid = document.getElementById('sensores');
  //     datoid.textContent = j;
  //   }, time);
  // }





  let temporizador = null;

  function onMessageArrived(message) {

    clearTimeout(temporizador);
    let j = (message.payloadString);//JSON.parse
    handleMessage(j);

    temporizador = setTimeout(function () { 
      j = "no encontrado";
      handleMessage(j);
    }, 15000);
    console.log(j);
  }

  function handleMessage(message) {
    if (message != null || message != undefined) {

      let dato1 = message;
      console.log(dato1);
      const datoid = document.getElementById('sensores');
      if (dato1 == "no encontrado"){
        datoid.textContent = dato1;
      }  
      else{
        datoid.textContent = dato1 + " °C";
      }
      
      // despues de un cierto intervalo de tiempo si no envia un dato, limpiar lo que se ve en pantalla
      // Espera 15 segundos
    }
  }
});




