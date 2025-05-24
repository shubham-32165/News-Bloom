const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
const signInForm = document.querySelector(".sign-in-form")
const signUpForm = document.querySelector(".sign-up-form")

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
  setTimeout(()=>{
    signInForm.style.display = "none"
    signUpForm.style.display = "flex"
  }, 600)
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
  setTimeout(()=>{
    signInForm.style.display = "flex"
    signUpForm.style.display = "none"
  }, 600)
});

function showPassword(target){
  var inputfield = document.getElementById(target);
  var slash = document.querySelector(`#${target} + .slash span`);
  console.log(inputfield);
  console.log(slash)
  if (inputfield.type === "password") {
    slash.style.width = '0px';
    slash.style.right = '2px';
    slash.style.bottom = '4px';
    inputfield.type = "text";
  } else {
    slash.style.width = '25px';
    slash.style.bottom = '10px';
    slash.style.right = '-4px';
    inputfield.type = "password";
  }
}