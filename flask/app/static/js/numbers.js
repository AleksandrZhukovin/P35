$(function(){
    $('#create_post').click(function(){
        if (document.getElementById('windows').open){
            document.getElementById('windows').close()
        } else {
            document.getElementById('windows').show()
        }
    })
})

$(function(){
    $('#send').click(function(){
        var formData = new FormData();
        formData.append('title', $('#title').val());
        formData.append('text', $('#text').val());
        formData.append('file', document.getElementById('file').files[0]);
        $.ajax('/create_post', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': formData,
            'contentType': false,
            'processData': false,
            'success': function(data){
                document.getElementById('posts').innerHTML += data['html'];
            }
        })
    })
})