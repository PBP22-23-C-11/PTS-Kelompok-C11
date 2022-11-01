// GET
$(document).ready(function(){
    $.get("/products/json", function(data){
        for (i=0; i<data.length; i++){
            $("#card-row").append(`
            <div class="card-col col">
                <div class="card shadow-xl m-auto h-100 duration-300 hover:scale-105" id="report-${data[i].pk}">
                    <div class="card-body">
                        <div class="grid grid-cols-6 gap-7 content-start">
                            <div class="col-span-5"><h1 class="card-title font-bold text-red-500 text-xl">${data[i].fields.product_name}</h1></div>
                        </div>
                        <p class="card-text font-normal">UMKM Name: ${data[i].fields.UMKM_name}</p>
                        <p class="card-text font-normal">Price: ${data[i].fields.price}</p>
                        <p class="card-text font-normal">Description: ${data[i].fields.description}</p>
                    </div>
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
            <div class="card-col col">
                <div class="card shadow-xl m-auto h-100 duration-300 hover:scale-105" id="report-${add.pk}">
                    <div class="card-body">
                        <div class="grid grid-cols-6 gap-7 content-start">
                            <div class="col-span-5"><h1 class="card-title font-bold text-red-500 text-xl">${add.fields.product_name}</h1></div>
                        </div>
                        <p class="card-text font-normal">UMKM Name: ${add.fields.UMKM_name}</p>
                        <p class="card-text font-normal">Price: ${add.fields.price}</p>
                        <p class="card-text font-normal">Description: ${add.fields.description}</p>
                    </div>
                </div>
            </div>
            `)
        })
        $('#add-product').on('hidden.bs.modal', function () {
            $('#reportModal form')[0].reset(); 
        });
    });
});
