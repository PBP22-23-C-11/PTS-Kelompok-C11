// GET
$(document).ready(function(){
    $.get("/products/json", function(data){
        for (i=0; i<data.length; i++){
            $("#card-row").append(`
            <div class="card col-sm-4 mb-1 mt-4 mx-auto" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title text-center fw-semibold">${data[i].fields.product_name}</h5>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">★ By ${data[i].fields.UMKM_name}</li>
                        <li class="list-group-item">★ ${data[i].fields.price}</li>
                        <li class="list-group-item">${data[i].fields.description}</li>
                    </ul>
                </div>
            </div>
            `)
        }
    });

    // POST
    $("#add-button").click(function(){
        const UMKM_name = $("#UMKM-name").val()
        const product_name = $("#product-name").val()
        const price = $("#product-price").val()
        const description = $("#product-description").val()
        const product = {
            UMKM_name : UMKM_name, 
            product_name : product_name, 
            price : price, 
            description : description,
            csrfmiddlewaretoken : '{{ csrf_token }}'
        }
        $.ajax({url:"/products/add/", data:product, method:"POST"}).done(function(add) {
            $("#card-row").append(`
            <div class="card col-sm-4 mb-1 mt-4 mx-auto" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title text-center fw-semibold">${add.fields.product_name}</h5>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">★ By ${add.fields.UMKM_name}</li>
                        <li class="list-group-item">★ ${add.fields.price}</li>
                        <li class="list-group-item">${add.fields.description}</li>
                    </ul>
                </div>
            </div>
            `)
        })
        $('#add-product').on('hidden.bs.modal', function () {
            $('#add-product form')[0].reset(); 
        });
    });
});
