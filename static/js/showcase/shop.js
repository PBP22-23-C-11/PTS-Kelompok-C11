const doneButton = document.getElementById("rate-shop-submit");
const rateButton = document.getElementById("btnRate");
const forCsrf = document.getElementById("for-csrf").value;
const forPk = document.getElementById("for-pk").value;

doneButton.onclick = function() {
    const rating_total = $("#rating_total").val()
    const data = {rating_total:rating_total, csrfmiddlewaretoken:forCsrf}
    $.ajax({url:`/showcase/rate_shop/${forPk}`, data:data, method:"POST"})
}