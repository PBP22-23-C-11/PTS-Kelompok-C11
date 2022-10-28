function previewImage() {
    imageURL = $('#create-article-image').val();
    $('#create-article-image-preview').attr('src', imageURL);
}

function createArticleSubmit() {
    title = $('#create-article-title').val();
    body = $('#create-article-body').val();
    imageURL = $('#create-article-image').val();
    $.ajax({
        method: 'POST',
        url: "/news/api/article/",
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        data: {
            title: title,
            body: body,
            image: imageURL,
        },
        success: function(data) {
            window.location = `/news/${data.id}`;
        },
        error: function(error) {
            alert('Error on posting article to server.');
        },
    });
}

$(document).ready(function() {
    $('#create-article-image').blur(previewImage);
    $('#create-article-submit').click(function() {
        createArticleSubmit();
    });
});