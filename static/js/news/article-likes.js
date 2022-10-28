function setLikeButton() {
    $.ajax({
        method: 'GET',
        url: `/news/api/articles/${getArticleId()}/likes/`,
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        success: function(data) {
            if (data.liked) {
                $('#like_button').text('Unlike');
            } else {
                $('#like_button').text('Like');
            }
            $('#like_count').text(data.count);
        },
        error: function(error) {
            alert('Error on fetching like data.');
        },
    });
}

function like() {
    $.ajax({
        method: 'PUT',
        url: `/news/api/articles/${getArticleId()}/likes/`,
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        success: function(data) {
            setLikeButton();
        },
        error: function(error) {
            alert('Error on updating like data.');
        },
    });
}

$(document).ready(function() {
    setLikeButton();
});