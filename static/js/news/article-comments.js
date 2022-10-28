function getComments() {
    $.ajax({
        method: 'GET',
        url: `/news/api/articles/${getArticleId()}/comments/`,
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        success: function(data) {
            commentList = $('#comment_list');
            commentList.empty();
            data.comments.forEach(function(comment) {
                deleteButton = '';
                if (getUserId() === comment.user.id) {
                    deleteButton = `<button type="button" onclick="deleteComment(${comment.id});" class="btn btn-danger">Delete</button>`
                }
                commentList.append(`
                    <div class="card mt-2">
                        <div class="card-body">
                            <div class="d-flex justify-content-between">
                                <div>
                                    <span class="d-block">${comment.user.name}</span>
                                    <span class="d-block">${new Date(comment.created_at).toDateString() + " " + new Date(comment.created_at).toTimeString().substring(0, 8)}</span>
                                </div>
                                <div>
                                    ${deleteButton}
                                </div>
                            </div>
                            <span>${comment.body}</span>
                        </div>
                    </div>
                `);
            });
        },
        error: function(error) {
            alert('Error on fetching comments from server.');
        },
    });
}

function postComment() {
    commentBody = $('#comment_body').val();
    $('#comment_body').val('');
    $.ajax({
        method: 'POST',
        url: `/news/api/articles/${getArticleId()}/comments/`,
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        data: {
            'body': commentBody,
        },
        success: function(data) {
            getComments();
        },
        error: function(error) {
            alert('Error on posting comment to server.');
        },
    });
}

function deleteComment(commentId) {
    $.ajax({
        method: 'DELETE',
        url: `/news/api/articles/${getArticleId()}/comments/${commentId}/`,
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        success: function(data) {
            getComments();
        },
        error: function(error) {
            alert('Error on deleting comment.');
        },
    });
}

$(document).ready(function() {
    getComments();
    $('#post-comment-button').click(function() {
        postComment();
    });
});