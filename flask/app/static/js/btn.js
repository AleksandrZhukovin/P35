$(function(){
    $('#btn').click(function(){
        $.ajax('/form/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'text': $('#text').val()
            },
            'success': function(data){
                alert(data['a'])
            }
        })
    })
})

$(function(){
    $('#like').click(function(){
        $.ajax('/form/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'text': $('#text').val()
            },
            'success': function(data){
                alert(data['a'])
            }
        })
    })
})