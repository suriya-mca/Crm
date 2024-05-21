document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const dangerUser = document.getElementById('danger-username');

    const emailInput = document.getElementById('email-input');
    const dangerEmail = document.getElementById('danger-email');

    const passwordInput = document.getElementById('confirm-password-input');
    const dangerPassword = document.getElementById('danger-confirm-password');

    userInput.addEventListener('input', () => {
        if (dangerUser.innerHTML !== '') {
            dangerUser.innerHTML = '';
            userInput.classList.remove('is-danger');
        }
    });

    emailInput.addEventListener('input', () => {
        if (dangerEmail.innerHTML !== '') {
            dangerEmail.innerHTML = '';
            emailInput.classList.remove('is-danger');
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
        if (event.detail.target.id === 'danger-email' && event.detail.successful) {
            emailInput.classList.add('is-danger');
        }
    });

    document.addEventListener('htmx:afterRequest', (event) => {
        if (event.detail.target.id === 'danger-confirm-password' && event.detail.successful) {
            passwordInput.classList.add('is-danger');
        }
    });
});

function onSubmit(token) {
    document.getElementById("register-form").submit();
}