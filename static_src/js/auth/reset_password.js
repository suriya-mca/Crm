document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('confirm-password-input');
    const dangerPassword = document.getElementById('danger-confirm-password');

    passwordInput.addEventListener('input', () => {
        if (dangerPassword.innerHTML !== '') {
            dangerPassword.innerHTML = '';
            passwordInput.classList.remove('is-danger');
        }
    });

    document.addEventListener('htmx:afterRequest', (event) => {
        if (event.detail.target.id === 'danger-confirm-password' && event.detail.successful) {
            passwordInput.classList.add('is-danger');
        }
    });
});