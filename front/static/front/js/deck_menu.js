console.log("ahoj")
let number_of_deck=null
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
  console.log("deck_menu.js - ajax function")
  destination_url = revers_urls.api_deck + number_of_deck + "/flashcards/"
  console.log("destination_url:"+destination_url)
  $('#table_flashcard').DataTable({
    ajax: {
       url: destination_url,
       type: "GET",
       dataSrc: "",
    },

    dom: 'Bfrtip',
    buttons: [
        {
            extend: 'copyHtml5',
            exportOptions: {
                columns: [ 0, ':visible' ]
            }
        },
        {
            extend: 'excelHtml5',
            exportOptions: {
                columns: ':visible'
            }
        },
        {
            extend: 'pdfHtml5',
            exportOptions: {
                columns: [ 0, 1, 2 ]
            }
        },
        {
            extend: 'colvis',
            columns: ':not(.noVis)'
        }
    ],
    columns: [
        { data: 'id' },
        { data: 'name' },
        { data: 'averse' },
        { data: 'edit',
          render: function (data, type, full, meta) {
            numer = data
            return '<a href="' + revers_urls.flashcards + numer + '" class="btn btn-w-m btn-success"> Edit </a>';
          }
        },
    ]
  });
})