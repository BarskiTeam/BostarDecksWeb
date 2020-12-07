url_home="http://127.0.0.1:8000"
$( document ).ready(function() {
  console.log("deck_menu.js")
  $.ajax({
      url: url_home+get_urls().deck_flashcards,
      type: "GET",
  }).done(function (response) {
      for(i=0; i<response.length; i++){
          console.log("response[i].id:"+response[i].id)
          $('#table_flashCard').append(
            '<tr>' +
                '<td>' + response[i].id + '</td>' +
                '<td>' + response[i].name + '</td>' +
                '<td>' + response[i].averse + '</td>' +
                '<td>' + ' <a href="'+ get_urls().front_flashcard + /*response[i].id +*/ '" class="button">' + response[i].name + '</a>' +
                '</td>' +
             '</td>');
          }
  }).fail(function () {
    alert("Exist problem with connection to api")
  })
})