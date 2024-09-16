document.getElementById('upload-form').addEventListener('submit',function (e) {

    // Stop the form from submitting when reloading the page
    e.preventDefault(); 

    // Get the form data
    let fdata= new FormData(this);

    // Send the form data to the server through a post request in this route /upload
    fetch('/upload', {
        method: 'POST',
        body: fdata
    })
    .then(response => response.json() ) 
    .then (data => {
        document.getElementById('result').innerText = "Result: " + data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}); 