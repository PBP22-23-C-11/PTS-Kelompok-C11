function displayLomba(data) {
    if (data.length == 0) {
        // If lomba is empty
        var pesan = document.createElement('p');
        pesan.innerHTML = 'Tidak ada lomba';

        $("#pesan").append(pesan);
        $("#ganti").show();

    } else {
        $.each( data, function(key, val) {
            var outerDiv = document.createElement('div');
            outerDiv.classList.add('col-sm-6');

            var card_outer = document.createElement('div');
            card_outer.classList.add('card', 'text-center');
            card_outer.style.marginBottom = "15px";

            var body = document.createElement('div');
            body.classList.add('card-body');

            var title = document.createElement('h5');
            var text = document.createElement('p');
            var buttonDetail = document.createElement('button');
            var links = document.createElement('a');
            
            links.appendChild(document.createTextNode("Detail"));
            links.href = "data/" + val.pk;
            buttonDetail.appendChild(links);

            title.classList.add('card-title');
            text.classList.add('card-text');
            buttonDetail.classList.add('btn', 'btn-primary');
            links.classList.add('link-light', 'text-decoration-none');

            title.innerHTML = val.fields.namaLomba;
            text.innerHTML = val.fields.keterangan;

            body.appendChild(title);
            body.appendChild(text);
            body.appendChild(buttonDetail);

            card_outer.appendChild(body);

            var footer = document.createElement('div');
            footer.classList.add('card-footer', 'text-muted');
            footer.innerHTML = "Tanggal ditambahkan: " + val.fields.tanggal;

            card_outer.appendChild(footer);

            outerDiv.appendChild(card_outer);

            $("#main-lomba").append(outerDiv);
        });
    }
}

$(document).ready(function(){

    // For displaying lomba data
    $.get( "/lomba/all/data/json", function(data) {
        displayLomba(data); 
    });

});