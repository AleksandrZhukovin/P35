$(function(){
    $('#btn').click(function(){
        $.ajax($('#url').val(), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'text': $('#text').val(),
                'csrf_token': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'success': function(data){
                document.getElementById('comments').innerHTML += data['data']
            }
        })
    })
})

$(function(){
    $('#like').click(function(){
        $.ajax($('#url').val(), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'like': 1
            },
            'success': function(data){
                if (data['liked']){
                    document.getElementById('like').innerHTML = 'Dislike'
                } else {
                    document.getElementById('like').innerHTML = 'Like'
                }
                document.getElementById('likes').innerHTML = data['amount']
            }
        })
    })
})