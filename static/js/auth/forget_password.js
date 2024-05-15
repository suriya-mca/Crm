document.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.getElementById('email-input');
    const dangerEmail = document.getElementById('danger-email');

    emailInput.addEventListener('input', () => {
        if (dangerEmail.innerHTML !== '') {
            dangerEmail.innerHTML = '';
            emailInput.classList.remove('is-danger');
        }
    });

    document.addEventListener('htmx:afterRequest', (event) => {
        if (event.detail.target.id === 'danger-email' && event.detail.successful) {
            emailInput.classList.add('is-danger');
        }
    });
});