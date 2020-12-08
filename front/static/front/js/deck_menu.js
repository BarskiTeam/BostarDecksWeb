url_home=get_urls().url_home
let number_of_deck=null
let regex = null
function func_for_number_of_deck(){
  let url = window.location.href
  table_of_url = url.split('/')
  console.log(table_of_url)
  if (table_of_url[table_of_url.length - 1] == '') {
    number_of_deck = table_of_url[table_of_url.length - 2]
  }
  else {
    number_of_deck = table_of_url[table_of_url - 1]
  }
  console.log("url:"+window.location.href)
  console.log("number_of_deck:"+number_of_deck)
}

$( document ).ready(function() {
  func_for_number_of_deck()
  console.log("deck_menu.js")
  $.ajax({
      url: url_home + get_urls().api_deck + number_of_deck+ "/flashCards/",
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