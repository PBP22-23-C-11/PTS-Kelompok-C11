function addDropDownUser() {
    var option = []
    var users = JSON.parse(document.getElementById('users').textContent);
    var opposite = JSON.parse(document.getElementById('opposite').textContent);
    option.push(`<option value="All `+opposite+`">All `+opposite+`</option>`);
    for (let i = 0; i < users.length; i++) {
        option.push(`<option value="`+users[i].trim()+`">`+users[i].trim()+`</option>`);
    }
    document.getElementById("toWho").innerHTML = option.join("");
}

function getFormData($form) {
    var unindexedSerializeArray = $form.serializeArray();
    var indexedSerializeArray = {};
    $.map(unindexedSerializeArray, function (n, i) {
        indexedSerializeArray[n['name']] = n['value'];
    });
    return indexedSerializeArray;
}

function displayCards(json) {
    var cards = [];
    var tipe_user = JSON.parse(document.getElementById('tipe_user').textContent);
    var user_and_type = JSON.parse(document.getElementById('user_and_type').textContent);
    var current_user = JSON.parse(document.getElementById('current_user').textContent);
    $.each(json, function (index, val) {
        var fields = val.fields
        var from = fields.username;
        var to = fields.toWho;

        var type_from = ` [`+user_and_type[from]+`]`;
        var type_to = "";
        if (!to.startsWith("All"))
            var type_to = ` [`+user_and_type[to]+`]`;
            
        if ((from==current_user) || (to==current_user) || (to==`All `+tipe_user)) {
            var divMain = document.createElement("div");
            divMain.classList.add("card");
            divMain.classList.add("text-white");
            divMain.classList.add("mb-2");
            divMain.classList.add("mt-2");
            divMain.style.cssText += 'max-width: 80rem; background-image:url(https://i.ibb.co/Cbt7ck3/wallpapersden-com-colorful-gradient-waves-8k-1280x720.jpg); ';
            var card_header = document.createElement("div");
            card_header.classList.add("card-header")
            card_header.classList.add("mt-2")
            card_header.style.cssText += 'background-image: url(https://wallpapersmug.com/download/1920x1080/1fdcf1/gradient-purple-blue.jpg);';
            var date = fields.date;
            card_header.innerHTML = date.substring(0, date.length-5).replace("T", " ");
            divMain.appendChild(card_header);
            var card_body = document.createElement("div");
            card_body.classList.add("card-body");
            var card_title = document.createElement("h5");
            card_title.classList.add("card-title");
            card_title.innerHTML = fields.title;
            card_body.appendChild(card_title);

            var card_description = document.createElement("p");
            card_description.classList.add("card-text");
            card_description.innerHTML = fields.message;
            card_body.appendChild(card_description)
            divMain.append(card_body);

            var card_footer = document.createElement("div");
            card_footer.classList.add("card-footer");
            card_footer.classList.add("text-white");
            card_footer.classList.add("mb-2");

            card_footer.innerHTML = `<b style="color:#90EE90; font-family:verdana;">From:</b> `+ from + type_from +
                `<br><b style="color:#90EE90; font-family:verdana;">To:</b> `+ to + type_to +`<br>`;
            if (from==current_user) {
                card_footer.style.cssText += 'background-color: green';
                var button_group = document.createElement("div");
                button_group.classList.add("btn-group");
                var delete_button = document.createElement("button");
                delete_button.classList.add("btn");
                delete_button.classList.add("btn-danger");
                delete_button.classList.add("btn-sm");
                delete_button.innerHTML = "Unsend";
                delete_button.style.cssText += 'border-radius: 5px;';
                delete_button.setAttribute('onclick', `deleteCard(${val.pk})`);
                button_group.appendChild(delete_button);
                card_footer.appendChild(button_group);
            } else if (to==current_user) {
                card_footer.style.cssText += 'background-color: orange';
            } else if (to==`All `+tipe_user) {
                card_footer.style.cssText += 'background-color: #3c1361';
            } 
            divMain.append(card_footer);
        
            cards.push(divMain.outerHTML);
        }
    });
    

    document.getElementById("card-container").innerHTML = cards.join("");
}

function updateCards() {
    $.getJSON("/obrolan/json", displayCards);
}

function deleteCard(pk) {
    $.ajax({
        url:`delete-disc/${pk}/`,
        type: "POST",
        data: {},
        success: updateCards,
    });
}

$(document).ready(function () {
    addDropDownUser();
    $.getJSON("/obrolan/json", displayCards);
    document.getElementById("modalButton").setAttribute('onclick', '$("#formModal").modal("show")');

    $("#createDiscForm").submit(function (e) {
        e.preventDefault();
        $(".btnClick").prop('disabled', true);
        $(".btnClick").text('Processing');
        var $form = $(this);
        var serializedData = getFormData($form);
        $.ajax({
            url: "/obrolan/add/",
            type: "POST",
            data: serializedData,
            dataType: 'text',
            success: function (data) {
                $(".btnClick").prop('disabled', false);
                $(".btnClick").text('Submit');
                $.getJSON("/obrolan/json", displayCards);
                $("#formModal").modal('hide');
                $('#createDiscForm').each(function () {
                    this.reset();
                });
            }
        });
    });
});