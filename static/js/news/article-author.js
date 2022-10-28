function deleteArticle() {
    $.ajax({
        method: 'DELETE',
        url: `/news/api/articles/${getArticleId()}/`,
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        success: function(data) {
            window.location = '/news/'
        },
        error: function(error) {
            alert('Error on deleting article.');
        },
    });
}

$(document).ready(function() {
    $('#delete_button').click(function() {
        deleteArticle();
    });
});