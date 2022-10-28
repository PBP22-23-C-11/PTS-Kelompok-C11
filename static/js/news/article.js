function getCsrfToken() {
    return $('#value-csrf-token').text();
}

function getUserId() {
    return parseInt($('#value-user-id').text());
}

function getArticleId() {
    return parseInt($('#value-article-id').text());
}

function getAuthorId() {
    return parseInt($('#value-author-id').text());
}