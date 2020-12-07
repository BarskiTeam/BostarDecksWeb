$( document ).ready(function() {
  console.log("decks.js")
  $.ajax({
      url: "http://127.0.0.1:8000/api/v1/deck/",
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
                '<td>' + ' <a href="/front/decks/details/' + response[i].id + '" class="button">' + response[i].name + '</a>' +
                '</td>' +
             '</td>');
          }
  }).fail(function () {
    alert("Exist problem with connection to api")
  })
})