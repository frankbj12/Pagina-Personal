let menuVisible = false;
//Función que oculta o muestra el menu
function mostrarOcultarMenu(){
    if(menuVisible){
        document.getElementById("nav").classList ="";
        menuVisible = false;
    }else{
        document.getElementById("nav").classList ="responsive";
        menuVisible = true;
    }
}

function seleccionar(){
    //oculto el menu una vez que selecciono una opcion
    document.getElementById("nav").classList = "";
    menuVisible = false;
}
//Funcion que aplica las animaciones de las habilidades
function efectoHabilidades(){
    var skills = document.getElementById("skills");
    var distancia_skills = window.innerHeight - skills.getBoundingClientRect().top;
    if(distancia_skills >= 300){
        let habilidades = document.getElementsByClassName("progreso");
        
        habilidades[0].classList.add("HtmlCss");
        habilidades[1].classList.add("javascript");
        habilidades[2].classList.add("Python");
        habilidades[3].classList.add("C");
        habilidades[4].classList.add("C++");
        habilidades[5].classList.add("BBD");
        habilidades[6].classList.add("SQL");
        habilidades[7].classList.add("SQLServer");
        habilidades[8].classList.add("Redes");
        habilidades[9].classList.add("ConocientosBasicosdeCiberseguridad");
        habilidades[10].classList.add("Ruby");
        habilidades[11].classList.add("BootStrap");
        habilidades[12].classList.add("Comunicacion");
        habilidades[13].classList.add("TrabajoEquipo");
        habilidades[14].classList.add("Creatividad");
        habilidades[15].classList.add("Dedicacion");
        habilidades[16].classList.add("Autodidacta");
        habilidades[17].classList.add("ResolucionProblemas");
        habilidades[18].classList.add("Adaptabilidad");
    }
}


//detecto el scrolling para aplicar la animacion de la barra de habilidades
window.onscroll = function(){
    efectoHabilidades();
}