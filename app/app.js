function addTask() {
    // Tu código actual...
}

function filterTasks() {
    var searchInput = document.getElementById("searchInput").value.toLowerCase();
    var tasks = document.getElementById("taskList").getElementsByTagName("li");

    for (var i = 0; i < tasks.length; i++) {
        var taskText = tasks[i].textContent.toLowerCase();

        if (taskText.includes(searchInput)) {
            tasks[i].style.display = "flex"; // Muestra la tarea
        } else {
            tasks[i].style.display = "none"; // Oculta la tarea
        }
    }
}

function sortTasks(criteria) {
    var taskList = document.getElementById("taskList");
    var tasks = Array.from(taskList.getElementsByTagName("li"));

    switch (criteria) {
        case "date":
            tasks.sort(compareDates);
            break;
        // Puedes agregar más casos según otros criterios
    }

    // Elimina las tareas actuales
    taskList.innerHTML = "";

    // Agrega las tareas ordenadas
    tasks.forEach(function (task) {
        taskList.appendChild(task);
    });
}

function compareDates(a, b) {
    var dateA = new Date(a.querySelector(".date").textContent);
    var dateB = new Date(b.querySelector(".date").textContent);

    return dateA - dateB;
}

function toggleDarkMode() {
    var body = document.body;
    body.classList.toggle('dark-mode');

    var toggleIcon = document.getElementById('toggleIcon');

    // Cambia el ícono según el modo oscuro esté activado o no
    toggleIcon.innerHTML = body.classList.contains('dark-mode') ? '&#127769;' : '&#9728;';
}
