

$(function(){
    $('#btn').click(function(){
        $.ajax('/ajax/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': $('#text').val() // document.getElementById('text').value
            },
            'success': function(data){
                document.getElementById('msg').innerHTML = data['status'];
                // $('#msg').text(data['status'])
            }
        })
    })
})

$(document).redy(function(){  // window.onload

})


// відправити у відповідь з сервера повідомлення про успішний запит і вивести в тег
// на сторінці