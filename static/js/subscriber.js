let subscribeForm = document.getElementById('subscribeForm')


subscribeForm.addEventListener('submit', function(e){
        let email = document.getElementById('email').value
         e.preventDefault()
         fetch('http://127.0.0.1:8000/api/subscriber/',{
            method : "POST",
            headers:{
                'Content-type': 'application/json',
                'X-CSRFToken' : subscribeForm.csrfmiddlewaretoken.value
            },
            body: JSON.stringify({'email':email})
         }).then(
            response =>{
                if (response.ok){
                    subscribeForm.innerHTML('<h2Successfully Sent!</h2>')
                }
            }
         )


})