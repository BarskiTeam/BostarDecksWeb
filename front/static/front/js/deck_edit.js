let start_name=''
let start_description=''
let start_public=''
let start_tag=''
let home_page=''
function func_for_number_of_deck(){
  let url = window.location.href
  table_of_url = url.split('/')
  console.log(table_of_url)
  home_page=table_of_url[0]+"//"+table_of_url[2]
  if (table_of_url[table_of_url.length - 1 ] == '') {
    console.log("length1:"+table_of_url.length)
    number_of_deck = table_of_url[table_of_url.length - 3]
  }
  else {
    console.log("length2:"+table_of_url.length)
    number_of_deck = table_of_url[table_of_url.length - 2 ]
  }
  console.log("url:"+window.location.href)
  console.log("number_of_deck:"+number_of_deck)
  return number_of_deck
}
$( document ).ready(function() {
  console.log("deck_edit.js - halu")
  console.log("revers_urls.api_deck: "+ revers_urls.api_deck)
  number_of_deck = func_for_number_of_deck()
  destination_url=home_page+revers_urls.api_deck+number_of_deck
  console.log("home_page:"+home_page)
  console.log("destination_url:"+destination_url)
  $.ajax({
      url:  destination_url,
      type: "GET",
  }).done(function(response) {
      console.log("udalo sie połączyć z ajaksa dane !")
      $('#name_deck').attr('value', response.name)
      $('#description_deck').attr('value', response.description)
      $('#public_deck').attr('value', response.public)
      $('#tag_deck').attr('value', response.tag)
   }).fail(function() {
      alert("Ahjo Wystąpił błąd w połączeniu z djangorestapi")
   }).then(function() {
      start_name=$('#name_deck').val()
      start_description=$('#description_deck').val()
      start_public=$('#public_deck').val()
      start_tag$('#tag_deck').val()
      console.log(start_name)
      console.log(start_description)
      console.log(start_public)
      console.log(start_tag)
   })
})
