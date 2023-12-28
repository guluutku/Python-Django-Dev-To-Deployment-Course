const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Fades out alert
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);