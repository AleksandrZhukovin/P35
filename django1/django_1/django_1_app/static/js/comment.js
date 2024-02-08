$(function(){
    $('#btn').click(function(){
        $.ajax($('#btn').data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': $('#text').val()
            },
            'success': function(data){
                document.getElementById('comments').innerHTML += data;
            }
        })
    })
})