$(
    function(){
        $(document).click(function(event){
            var element = $(event.target);
            if (element.attr('class') == 'like_button'){
                $.ajax('/posts/', {
                    'type': 'POST',
                    'async': true,
                    'dataType': 'json',
                    'data': {
                         'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                         'id': element.attr('id')
                    },
                    'success': function(data){
                        element.text(data['action']);
                        document.getElementById(`likes${element.attr('id')}`).innerHTML = data['amount'];
                    }
                })
            }
        })
    }
)