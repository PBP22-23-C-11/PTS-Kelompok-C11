const doneButton = document.getElementById("rate-shop-submit");
const rateButton = document.getElementById("btnRate")

doneButton.onclick = function() {
    const rating_total = $("#rating_total").val()
    const data = {rating_total:rating_total, csrfmiddlewaretoken:"{{ csrf_token }}"}
    $.ajax({url:"/showcase/rate_shop/{{ umkm.pk }}", data:data, method:"POST"})
}