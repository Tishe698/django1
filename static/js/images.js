var imageClicks = document.querySelectorAll(".image-click");
var plusIcons = document.querySelectorAll(".plus-icon");
var modals = document.querySelectorAll(".image-modal");

imageClicks.forEach(function (imageClick, index) {
    var modal = modals[index];
    var plusIcon = plusIcons[index];

    // Обработчик события для изображения
    imageClick.addEventListener("click", function () {
        modal.style.display = "block";
        plusIcon.style.display = "none"; // Скрыть плюсик при клике на изображение
    });

    // Обработчик события для плюсика
    plusIcon.addEventListener("click", function () {
        modal.style.display = "block";
        plusIcon.style.display = "none"; // Скрыть плюсик при клике на плюсик
    });

    // Обработчик события для закрытия модального окна
    modal.addEventListener("click", function () {
        modal.style.display = "none";
        plusIcon.style.display = "block"; // Показать плюсик после закрытия модального окна
    });
});
