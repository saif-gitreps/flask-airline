const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const signupForm = document.getElementById("signup-form");
const signupButton = document.getElementById("signup-form-submit");

loginButton.addEventListener("click", (e) => {
   e.preventDefault();
   const username = loginForm.username.value;
   const password = loginForm.password.value;
});
