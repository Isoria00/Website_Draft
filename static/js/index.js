// Get references to form elements
const usernameInput = document.querySelector('input[name="username"]');
const passwordInput = document.querySelector('input[name="psswrd"]');
const loginButton = document.getElementById("login_button");

// Add event listeners to enable/disable the login button
function toggleLoginButton() {
  if (usernameInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
    loginButton.disabled = false;
    loginButton.classList.add("active");
  } else {
    loginButton.disabled = true;
    loginButton.classList.remove("active");
  }
}

// Add input event listeners
usernameInput.addEventListener("input", toggleLoginButton);
passwordInput.addEventListener("input", toggleLoginButton);

// Initialize the button state on page load
document.addEventListener("DOMContentLoaded", () => {
  toggleLoginButton();
});

// Event listeners to handle user input and login attempt
document.getElementById("username").addEventListener("input", () => {
  toggleLoginButton();
  handleErrorVisibility();
});

document.getElementById("password").addEventListener("input", () => {
  toggleLoginButton();
  handleErrorVisibility();
});

// Function to handle error message visibility
function handleErrorVisibility() {
  const errorMessage = document.getElementsByClassName("error-message");

  // If the error message is showing, hide it when the user starts typing
  errorMessage.style.display = "none";
}
