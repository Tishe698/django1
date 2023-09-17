document.addEventListener("DOMContentLoaded", function () {
    var popupForm = document.getElementById("popupForm");
    var formaOtkroisyElements = document.querySelectorAll(".forma_otkroisy");
    var krestik = document.querySelector(".krestik");

    formaOtkroisyElements.forEach(function(element) {
        element.addEventListener("click", function () {
            if (popupForm.classList.contains("active")) {
                popupForm.classList.remove("active");
                popupForm.classList.add("closed");
            } else {
                popupForm.classList.remove("closed");
                popupForm.classList.add("active");
            }
        });
    });

    // Добавляем обработчик события клика на крестик для закрытия формы
    krestik.addEventListener("click", function () {
        popupForm.classList.remove("active");
        popupForm.classList.add("closed");
    });
});
