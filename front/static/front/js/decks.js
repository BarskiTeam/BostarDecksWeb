$( document ).ready(function() {
  console.log("decks.js")
  let destinationUrl = revers_urls.api_v1_deck_list
  console.log("destinationUrl:" + destinationUrl)
  $.ajax({
      url: destinationUrl,
      type: "GET",
  }).done(function (response) {
      for(i=0; i<response.length; i++){
          console.log("response[i].id:"+response[i].id)
          $('#table_decks').append(
            '<tr>' +
                '<td>' + response[i].id + '</td>' +
                '<td>' + response[i].name + '</td>' +
                '<td>' + response[i].description + '</td>' +
                '<td>' + response[i].public + '</td>' +
                '<td>' + ' <a href="' + revers_urls.front_deck + "/" +response[i].id + '" class="button">' + response[i].name + '</a>' +
                '</td>' +
             '</td>');
          }
  }).fail(function () {
    alert("Exist problem with connection to api")
  })
})
