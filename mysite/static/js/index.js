// Функция для подтверждения отправки формы
document.getElementById("event-form").addEventListener("submit", function (event) {
    const titleInput = this.querySelector("input[name='title']");
    if (!titleInput.value.trim()) {
        alert("Название события не может быть пустым!");
        event.preventDefault(); // Отменяем отправку формы
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".event-item");

    items.forEach((item, index) => {
        item.style.setProperty("--index", index); // Устанавливаем индекс элемента
    });

    // Добавляем эффект клика, если нужно
    items.forEach(item => {
        item.addEventListener("click", () => {
            item.classList.add("clicked");
            setTimeout(() => item.classList.remove("clicked"), 300);
        });
    });
});

