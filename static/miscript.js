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


document.addEventListener('DOMContentLoaded', function() {
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
    userName : "juan-camilo",
    password : "iNM123456789",
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


  function onMessageArrived(message) { 
  // console.log("onMessageArrived:" + j);
  let j = JSON.parse(message.payloadString);
  handleMessage(j);


  
  }




  // console.log("Topic:     " + message.destinationName);
  // console.log("QoS:       " + message.qos);
  // console.log("Retained:  " + message.retained);
  // // Read Only, set if message might be a duplicate sent from broker
  // console.log("Duplicate: " + message.duplicate);



function handleMessage(message) {
  if (message != null || message != undefined) {
    
    let dato1 = message;
    const datoid = document.getElementById('sensores');
    datoid.textContent = dato1 + " °C";
    console.log(dato1);
    // despues de un cierto intervalo de tiempo si no envia un dato, limpiar lo que se ve en pantalla

    setTimeout(function () {
      dato1 = "vacio"; 
      console.log("Variable no encontrada");
      datoid.textContent = dato1;
    }, 15000); // Espera 15 segundos
  



  }
}

});




