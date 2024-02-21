document.addEventListener("DOMContentLoaded", function () {
   const loginForm = document.getElementById("login-form");

   loginForm.addEventListener("submit", function (event) {
      event.preventDefault();

      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      const userType = document.querySelector('input[name="user"]:checked').value;

      const loginData = {
         email: email,
         password: password,
      };

      console.log(JSON.stringify(loginData));

      if (userType === "customer") {
         fetch("http://127.0.0.1:5000/api/v1/login", {
            method: "POST",
            headers: {
               "Content-Type": "application/json",
            },
            body: JSON.stringify(loginData),
         })
            .then((response) => {
               if (!response.ok) {
                  throw new Error("Network response was not ok");
               }
               window.location.href = "customer.html";
               return response.json();
            })
            .then((data) => {
               console.log(data);
            })
            .catch((error) => {
               console.log("There was a problem with your fetch operation:", error);
            });
      } else {
         fetch("http://127.0.0.1:5000/api/v1/login/admin", {
            method: "POST",
            headers: {
               "Content-Type": "application/json",
            },
            body: JSON.stringify(loginData),
         })
            .then((response) => {
               if (!response.ok) {
                  throw new Error("Network response was not ok");
               }
               window.location.href = "admin.html";
               return response.json();
            })
            .then((data) => {
               console.log(data);
            })
            .catch((error) => {
               console.log("There was a problem with your fetch operation:", error);
            });
      }
   });
});
