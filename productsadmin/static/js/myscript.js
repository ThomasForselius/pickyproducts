$(document).ready(function(){
    
  const username = document.getElementById('username');
  const email = document.getElementById('email');
  const name = document.getElementById('name');
  const password1 = document.getElementById('password1');
  const password2 = document.getElementById('password2');
  const pass_check = document.getElementById('pass_check');


  name.addEventListener('keyup', (event) => {
      name.value = name.value.replace(/[^a-öA-Ö]*$/g, "");
      if(name.length < 1){
          name.className = "error";
      }
      else{
          name.className = "pass";
      }
  });

  password2.addEventListener('keyup', (event) =>
  {
     if(password2.value != password1.value){
      pass_check.innerText = "Passwords do not match";
      pass_check.className = "alert alert-danger";
      document.getElementById("submit").disabled = true;
     }
     else{
      pass_check.innerText = "";
      document.getElementById("submit").disabled = false;
      pass_check.className = "";
     }
  });




  })