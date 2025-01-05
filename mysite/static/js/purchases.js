// Добавление интерактивных эффектов
document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".purchase-item");

    items.forEach(item => {
        item.addEventListener("click", () => {
            item.classList.add("clicked");
            setTimeout(() => item.classList.remove("clicked"), 300);
        });
    });
});
