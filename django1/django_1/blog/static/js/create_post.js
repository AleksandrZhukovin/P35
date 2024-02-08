$(
    function(){
        $('#open').click(function(){
            if (document.getElementById('dialog').open) {
                document.getElementById('dialog').close();
            } else {
                document.getElementById('dialog').show();
            }
        })
    }
)

$(
    function(){
        $('#send').click(function(){
            var formData = new FormData();

            formData.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
            formData.append('text', $('#text').val());
            formData.append('file', document.getElementById('file').files[0]);

            $.ajax('/posts/', {
                'type': 'POST',
                'async': true,
                'dataType': 'json',
                'data': formData,
                'processData': false,
                'contentType': false,
                'success': function(data){
                    document.getElementById('post').innerHTML = data + document.getElementById('post').innerHTML;
                    document.getElementById('dialog').close();
                }
            })
        })
    }
)