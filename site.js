const loginForm = document.getElementById("loginForm");
const formMessage = document.getElementById("formMessage");
const forgotLink = document.getElementById("forgotLink");

if (forgotLink) {
    forgotLink.addEventListener("click", (event) => {
        event.preventDefault();
        showMessage("Password recovery would be handled by your real backend in the full app.", "success");
    });
}

if (loginForm) {
    loginForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (!email || !password) {
            showMessage("Please fill in both fields.", "error");
            return;
        }

        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            showMessage("Please enter a valid email address.", "error");
            return;
        }

        showMessage("Sign-in demo successful. In the Flask app, this would continue to the authenticated dashboard.", "success");
        loginForm.reset();
    });
}

function showMessage(message, type) {
    if (!formMessage) {
        return;
    }

    formMessage.className = `form-message show ${type}`;
    formMessage.textContent = message;
}
