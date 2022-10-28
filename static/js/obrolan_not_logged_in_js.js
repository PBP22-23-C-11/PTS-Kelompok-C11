function displayCards(json) {
    var cards = [];
    var user_and_type = JSON.parse(document.getElementById('user_and_type').textContent);
    $.each(json, function (index, val) {
        var fields = val.fields
        var from = fields.username;
        var to = fields.toWho;

        var type_from = ` [`+user_and_type[from]+`]`;
        var type_to = "";
        if (!to.startsWith("All"))
            var type_to = ` [`+user_and_type[to]+`]`;
            
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
        card_footer.style.cssText += 'background-image: url(https://wallpapersmug.com/download/1920x1080/1fdcf1/gradient-purple-blue.jpg);';
        divMain.append(card_footer);
    
        cards.push(divMain.outerHTML);
    });
    

    document.getElementById("card-container").innerHTML = cards.join("");
}

$(document).ready(function () {
    $.getJSON("/obrolan/json", displayCards);
});