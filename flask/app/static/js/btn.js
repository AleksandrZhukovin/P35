$(function(){
    $('#btn').click(function(){
        var formData = new FormData();
        formData.append('text', $('#text').val());
        formData.append('file', document.getElementById('file').files[0]);
        $.ajax('/form/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': formData,
            'processData': false,
            'contentType': false,
            'success': function(data){
                alert(data['a'])
            }
        })
    })
})

