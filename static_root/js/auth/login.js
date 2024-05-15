document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const dangerUser = document.getElementById('danger-username');

    const passwordInput = document.getElementById('password-input');
    const dangerPassword = document.getElementById('danger-password');

    userInput.addEventListener('input', () => {
        if (dangerUser.innerHTML !== '') {
            dangerUser.innerHTML = '';
            userInput.classList.remove('is-danger');
        }
    });

    passwordInput.addEventListener('input', () => {
        if (dangerPassword.innerHTML !== '') {
            dangerPassword.innerHTML = '';
            passwordInput.classList.remove('is-danger');
        }
    });

    document.addEventListener('htmx:afterRequest', (event) => {
        if (event.detail.target.id === 'danger-username' && event.detail.successful) {
            userInput.classList.add('is-danger');
        }
    });

    document.addEventListener('htmx:afterRequest', (event) => {
        if (event.detail.target.id === 'danger-password' && event.detail.successful) {
            passwordInput.classList.add('is-danger');
        }
    });
});