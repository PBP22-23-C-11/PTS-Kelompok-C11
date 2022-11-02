const doneButton = document.getElementById("add-shop-submit");
const addButton = document.getElementById("btnAdd");

doneButton.onclick = function() {
    const shop_name = $("#shop_name").val()
    const category = $("#category").val()
    const desc = $("#description").val()
    const umkm_url = $("#umkm_url").val()
    const number = $("#number").val()
    const image = $("#image").val()
    const data =  {shop_name:shop_name, category:category, description:desc, umkm_url:umkm_url, number:number, image:image, csrfmiddlewaretoken:"{{ csrf_token }}"}
    $.ajax({url:"/showcase/add_shop/", data:data, method:"POST"}).done(function() {
        show_cards()
        addButton.style.display = "none"
    })
}


function show_cards() {
    $.get('/showcase/json', function(shops) {
        $('#myCards').empty()
        shops.map((shop) => {
            $('#myCards').append(`
                <div class="col-xs-12 col-sm-4">
                        <div class="card" style="background:linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.2)), url('${shop.fields.image}');">
                        <div class="card-category">
                            ${shop.fields.category}
                        </div>
                        <div class="card-description">
                            <h2>${shop.fields.shop_name}</h2>
                        </div>
                        <a class="card-link" href="/showcase/shop/${shop.pk}"></a>
                    </div>
                </div>
            `)
        })
    })
}

$(document).ready(function() {
    show_cards()
})  