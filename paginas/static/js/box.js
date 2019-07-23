$(window).on('load', function() {
    // $('.btn-common').on('click', function () {
    $('#NumForm, #EmailForm, #MensagemForm').submit(function(){
        var valido =  $.ajax({
            headers: {
            "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val(),
            },
            data: $(this).serialize(),
            url: '/valido',
            processData: false,
            'type': 'POST',
            
            contentType: "application/json",
            beforeSend: function() { 

            },
            success: function(msg) {
                $('#butaoModal').click();
                $('.box-load').removeClass();
            }
        });
      })

})