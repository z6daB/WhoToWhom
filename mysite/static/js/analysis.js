document.addEventListener('DOMContentLoaded', function() {
    const debtCards = document.querySelectorAll('.debt-card');
    const modal = document.getElementById('debtModal');
    const closeModalButton = document.getElementById('closeModal');
    const debtAmountInput = document.getElementById('debtAmount');
    const debtUpdateForm = document.getElementById('debtUpdateForm');
    let currentDebtId = null;

    // Открытие модального окна
    debtCards.forEach(card => {
        card.addEventListener('click', function() {
            currentDebtId = card.getAttribute('data-debt-id');
            const debtAmount = card.querySelector('.debt-amount').textContent.trim();
            debtAmountInput.value = debtAmount;
            modal.classList.add('show'); // Показываем модальное окно
        });
    });

    closeModalButton.addEventListener('click', function() {
        modal.classList.remove('show'); // Скрываем модальное окно
    });

    debtUpdateForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const amount = debtAmountInput.value;
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch(`/update_debt/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ debt_id: currentDebtId, amount: amount })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const debtCard = document.querySelector(`[data-debt-id="${currentDebtId}"]`);
                debtCard.querySelector('.debt-amount').textContent = data.new_amount;
                modal.classList.remove('show'); // Закрытие модального окна
            } else if (data.status === 'deleted') {
                const debtCard = document.querySelector(`[data-debt-id="${currentDebtId}"]`);
                debtCard.remove();
                modal.classList.remove('show'); // Закрытие модального окна
            } else {
                alert('Ошибка: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert('Произошла ошибка при обновлении долга');
        });
    });
});