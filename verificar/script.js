document.addEventListener("DOMContentLoaded", function() {
    cargarLista();
  });
  
  function cargarLista() {
    var listaAlumnos = JSON.parse(localStorage.getItem("alumnos")) || [];
    var listaAlumnosHTML = "";
  
    listaAlumnos.forEach(function(alumno) {
      listaAlumnosHTML += `<li class='list-group-item' data-nombre='${alumno.nombre}' data-apellido='${alumno.apellido}' data-aprobado='${alumno.aprobado}' data-asistio='${alumno.asistio}'>${alumno.nombre} ${alumno.apellido}</li>`;
    });
  
    document.getElementById("listaAlumnos").innerHTML = listaAlumnosHTML;
  }
  
  function verificar() {
    var nombre = document.getElementById("nombre").value.trim();
    var apellido = document.getElementById("apellido").value.trim();
    var aprobado = document.getElementById("aprobado").checked;
    var asistio = document.getElementById("asistio").checked;
  
    if (nombre === "" || apellido === "") {
      alert("Por favor, ingrese nombre y apellido.");
      return;
    }
  
    var resultado = `
      Alumno: ${nombre} ${apellido}<br>
      Aprobado: ${aprobado ? "Sí" : "No"}<br>
      Asistió a la clase: ${asistio ? "Sí" : "No"}<br>
    `;
  
    document.getElementById("resultado").innerHTML = resultado;
  
    var nuevoAlumno = { nombre: nombre, apellido: apellido, aprobado: aprobado, asistio: asistio };
    var listaAlumnos = JSON.parse(localStorage.getItem("alumnos")) || [];
    listaAlumnos.push(nuevoAlumno);
    localStorage.setItem("alumnos", JSON.stringify(listaAlumnos));
  
    limpiarFormulario();
    cargarLista();
  }
  
  function eliminarUltimoAlumno() {
    var listaAlumnos = JSON.parse(localStorage.getItem("alumnos")) || [];
    listaAlumnos.pop();
    localStorage.setItem("alumnos", JSON.stringify(listaAlumnos));
  
    cargarLista();
  }
  
  function limpiarFormulario() {
    document.getElementById("nombre").value = "";
    document.getElementById("apellido").value = "";
    document.getElementById("aprobado").checked = false;
    document.getElementById("asistio").checked = false;
  }
  
  function mostrarDetalle(event) {
    var target = event.target;
  
    if (target.tagName === 'LI') {
      var nombre = target.dataset.nombre;
      var apellido = target.dataset.apellido;
      var aprobado = target.dataset.aprobado === 'true' ? 'Sí' : 'No';
      var asistio = target.dataset.asistio === 'true' ? 'Sí' : 'No';
  
      var detalle = `
        Detalle del Alumno:<br>
        Nombre: ${nombre} ${apellido}<br>
        Aprobado: ${aprobado}<br>
        Asistió a la clase: ${asistio}
      `;
  
      document.getElementById("resultado").innerHTML = detalle;
    }
  }
  