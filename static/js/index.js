const usernameInput = document.querySelector('input[name="username"]');
const passwordInput = document.querySelector('input[name="psswrd"]');
const loginButton = document.getElementById("login_button");

function toggleLoginButton() {
  if (usernameInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
    loginButton.disabled = false;
    loginButton.classList.add("active");
  } else {
    loginButton.disabled = true;
    loginButton.classList.remove("active");
  }
}

usernameInput.addEventListener("input", toggleLoginButton);
passwordInput.addEventListener("input", toggleLoginButton);

document.addEventListener("DOMContentLoaded", () => {
  toggleLoginButton();
});

document.getElementById("username").addEventListener("input", () => {
  toggleLoginButton();
  handleErrorVisibility();
});

document.getElementById("password").addEventListener("input", () => {
  toggleLoginButton();
  handleErrorVisibility();
});

function handleErrorVisibility() {
  const errorMessage = document.getElementsByClassName("error-message");

  errorMessage.style.display = "none";
}
