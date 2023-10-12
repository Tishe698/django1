document.addEventListener("DOMContentLoaded", function () {
    var popupForm = document.getElementById("popupForm2");
    var formaOtkroisyElements = document.querySelectorAll(".forma_otkroisy2");
    var krestik = document.querySelectorAll(".krestik");

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

    krestik.forEach(function(krestikElement) {
        krestikElement.addEventListener("click", function () {
            popupForm.classList.remove("active");
            popupForm.classList.add("closed");
        });
    });
});
