function getCsrfToken() {
    return $('#value-csrf-token').text();
}

function showMessage(message) {
    $('#message').html(message);
}

$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault();
        
        username = $('#username').val();
        password = $('#password').val();
        
        $.ajax({
            method: 'POST',
            url: '/login/',
            headers: {
                'X-CSRFToken': getCsrfToken(),
            },
            data: {
                username: username,
                password: password,
            },
            success: function(data) {
                window.location = '/'
            },
            error: function(error) {
                console.log(error);
                showMessage('Error');
            },
        });
    })
});