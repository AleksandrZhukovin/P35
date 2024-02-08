$(
    function(){
        $('#btn').click(function(){
            $.ajax($('#btn').data('url'), {
                'type': 'POST',
                'async': true,
                'dataType': 'json',
                'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                'success': function(data){
                    document.getElementById('likes').innerHTML = data['amount'];
                    if (data['action']) {
                        $('#btn').text('Dislike');
                    } else {
                        $('#btn').text('Like');
                    }
                }
            })
        })
    }
)