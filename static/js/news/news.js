// Query
let title;
let umkm;
let umkmType;
let sortByValue;
let sortByDirection;
let sortBy;

function submitForm() {
    data = {
        title: title,
        sort_by: sortBy,
        category: getCategory(),
    };
    if (getCategory() == 'umkm') {
        data.umkm = umkm;
        data.umkm_type = umkmType;
    }
    $.ajax({
        method: 'GET',
        url: '/news/api/article/',
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        data: data,
        success: function(data) {
            refreshArticleList(data);
        },
        error: function(error) {
            alert('Error on fetching articles from server.')
        },
    });
}

function updateNonSortBy() {
    title = $('#title').val();
    umkm = $('#umkm').val();
    umkmType = $('#umkm_type').val();
}

function updateSortBy() {
    sortByValue = $('input[name=sort_by_value]:checked').val();
    sortByDirection = $('input[name=sort_by_direction]:checked').val();
    sortBy = `${sortByValue}_${sortByDirection}`;
}

function refreshArticleList(data) {
    let articleList = $('#article_list');
    articleList.empty();
    
    data.articles.forEach(function(article) {
        let title = escapeHTML(article.title);
        let authorName = escapeHTML(article.author.name);
        let createdAt = article.created_at;
        createdAt = new Date(createdAt).toDateString() + " " + new Date(createdAt).toTimeString().substring(0, 8);
        let likes = article.likes;
        let id = article.id;
        let imageSource = article.image;
        if (imageSource == null) {
            imageSource = 'https://upload.wikimedia.org/wikipedia/commons/3/39/C_Hello_World_Program.png'; // TODO: Change Placeholder
        }
        articleList.append(`
            <div class="card article-card">
                <img src=${imageSource} class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">${title}</h5>
                    <span class="d-block">${authorName}</span>
                    <span class="d-block">${createdAt}</span>
                    <span class="d-block">Likes: ${likes}</span>
                    <a href="/news/${id}" class="btn btn-primary">Read Article</a>
                </div>
            </div>
        `);
    });
}

$(document).ready(function() {
    updateNonSortBy();
    updateSortBy();
    submitForm();
    
    $('#search_form').submit(function(event) {
        event.preventDefault();
        updateNonSortBy();
        updateSortBy();
        submitForm();
    });
    
    $('input[name=sort_by_value], input[name=sort_by_direction]').change(function() {
        updateSortBy();
        submitForm();
    });
});

function getCsrfToken() {
    return $('#value-csrf-token').text();
}

function getCategory() {
    return $('#value-category').text();
}