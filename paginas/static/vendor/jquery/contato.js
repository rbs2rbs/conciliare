$(document).ready(function(){ 
    $('#caracterRestante').text('440 caracteres Restantes');
    $('#id_message').wrap( "<div></div>" );
    $('#id_message').keydown(function () {
        var max = 440;
        var len = $(this).val().length;
        if (len >= max) {
            $('#caracterRestante').text('You have reached the limit');
            $('#caracterRestantet').addClass('red');
            $('#btnSubmit').addClass('disabled');            
        } 
        else {
            var ch = max - len;
            $('#caracterRestante').text(ch + ' caracteres Restantes');
            $('#btnSubmit').removeClass('disabled');
            $('#caracterRestante').removeClass('red');            
        }
    });    
});
