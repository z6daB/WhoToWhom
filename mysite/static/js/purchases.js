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

document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('.return-button');
    if (button) {
        button.addEventListener('mousedown', () => {
            button.style.transform = 'scale(0.95)';
        });
        button.addEventListener('mouseup', () => {
            button.style.transform = 'scale(1)';
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('.btn');
    if (button) {
        button.addEventListener('mousedown', () => {
            button.style.transform = 'scale(0.95)';
        });
        button.addEventListener('mouseup', () => {
            button.style.transform = 'scale(1)';
        });
    }
});
