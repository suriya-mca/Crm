document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password-input');
    const dangerPassword = document.getElementById('danger-password');

    const confirmPasswordInput = document.getElementById('confirm-password-input');
    const confirnDangerPassword = document.getElementById('danger-confirm-password');

    passwordInput.addEventListener('input', () => {
        if (dangerPassword.innerHTML !== '') {
            dangerPassword.innerHTML = '';
            passwordInput.classList.remove('is-danger');
        }
    });

    confirmPasswordInput.addEventListener('input', () => {
        if (confirnDangerPassword.innerHTML !== '') {
            confirnDangerPassword.innerHTML = '';
            confirmPasswordInput.classList.remove('is-danger');
        }
    });

    document.addEventListener('htmx:afterRequest', (event) => {
        if (event.detail.target.id === 'danger-password' && event.detail.successful) {
            passwordInput.classList.add('is-danger');
        }
    });

    document.addEventListener('htmx:afterRequest', (event) => {
        if (event.detail.target.id === 'danger-confirm-password' && event.detail.successful) {
            confirmPasswordInput.classList.add('is-danger');
        }
    });
});