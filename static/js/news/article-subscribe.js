function setSubscribeButton() {
    $.ajax({
        method: 'GET',
        url: `/news/api/subscribes/${getAuthorId()}/`,
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        success: function(data) {
            if (data.subscribed) {
                $('#subscribe_button').text('Unsubscribe');
            } else {
                $('#subscribe_button').text('Subscribe');
            }
        },
        error: function(error) {
            alert('Error on fetching subscription data.');
        },
    });
}

function subscribe() {
    $.ajax({
        method: 'PUT',
        url: `/news/api/subscribes/${getAuthorId()}/`,
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        success: function(data) {
            setSubscribeButton();
        },
        error: function(error) {
            alert('Error on updating subscription data.');
        },
    });
}

$(document).ready(function() {
    setSubscribeButton();
});