document.getElementById("create-goal").addEventListener("click", function() {
    var form = document.getElementById("todo-form");
    if (form.style.display === "none" || form.style.display === "") {
        form.style.display = "block";
    } else {
        form.style.display = "none";
    }
});
