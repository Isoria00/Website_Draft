// Get references to form elements
const usernameInput = document.querySelector('input[name="username"]');
const passwordInput = document.querySelector('input[name="psswrd"]');
const loginButton = document.getElementById("login_button");
const invalidPassword = document.getElementsByClassName("error_message");

// Add event listeners to enable/disable the login button
function toggleLoginButton() {
  if (usernameInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
    loginButton.disabled = false;
    loginButton.classList.add("active"); // Optional for styling
  } else {
    loginButton.disabled = true;
    loginButton.classList.remove("active"); // Optional for styling
  }
}

// Add input event listeners
usernameInput.addEventListener("input", toggleLoginButton);
passwordInput.addEventListener("input", toggleLoginButton);

// Initialize the button state on page load
document.addEventListener("DOMContentLoaded", () => {
  toggleLoginButton();
});
