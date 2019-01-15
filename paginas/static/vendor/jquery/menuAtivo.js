$(window).scroll(function() {
    var scrollDistance = $(window).scrollTop() + 508.312 // NUMERO ADICIONADO ARBRITARIAMENTE PARA AJUSTAR A AÇÃO
    $('.pos').each(function(i) {
            if ($(this).position().top <= (scrollDistance)) {
                $('.nav-item').removeClass('ativo');
                $('.nav-item').eq(i).addClass('ativo');
            }
    });
}).scroll();

$(document).ready(function(){
    $(".nav-item").click(function(){
        var irPara = $(this).children().attr('id').slice(0,-1);
        $('html, body').animate({
            scrollTop: $("#" + irPara).offset().top - 300
        }, 1000);
    });
});