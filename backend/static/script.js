const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");
signupBtn.onclick = (()=>{
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
});
loginBtn.onclick = (()=>{
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";
});
signupLink.onclick = (()=>{
  signupBtn.click();
  return false;
});

// const password = document.getElementById("password");
// const cpassword = document.getElementById("cpassword");
// const message = document.getElementById("password-message");
// const submitButton = document.getElementById("submit-btn");

// cpassword.addEventListener("input", function() {
//   if (password.value !== cpassword.value) {
//     message.textContent = "Password and Confirm Password do not match";
//     message.style.color = "red";
//     submitButton.disabled = true;

//   } else {
//     message.textContent = "";
//     submitButton.disabled = false;
//   }
// });


const email = document.getElementById("emailid");
const password = document.getElementById("password");
const cpassword = document.getElementById("cpassword");
const message = document.getElementById("password-message");
const submitButton = document.getElementById("submit-btn");

function validateForm() {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailRegex.test(email.value)) {
    message.textContent = "Please enter a valid email address";
    message.style.color = "red";
    submitButton.disabled = true;
  } else if (password.value !== cpassword.value) {
    message.textContent = "Password and Confirm Password do not match";
    message.style.color = "red";
    submitButton.disabled = true;
  } else {
    message.textContent = "";
    submitButton.disabled = false;
  }
}

email.addEventListener("input", validateForm);
cpassword.addEventListener("input", validateForm);

const emails = document.getElementById("log-email");
const passwords = document.getElementById("log-password");
const msg = document.getElementById("email-message");
const subBtn = document.getElementById("submit-button");

function validatedForm() {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailRegex.test(emails.value)) {
    msg.textContent = "Please enter a valid email address";
    msg.style.color = "red";
    subBtn.disabled = true;
  } else {
    msg.textContent = "";
    subBtn.disabled = false;
  }
}

emails.addEventListener("input", validatedForm);
