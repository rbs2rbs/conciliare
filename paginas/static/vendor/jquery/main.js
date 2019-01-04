$(function(){
    $('.menu').on('click',function(){
        $('.menu').removeClass('ativo')
        $(this).addClass('ativo');       
    });
    $("#home, #logo").on("click", function() {
        $("html, body").animate({ scrollTop: 0 }, "slow");
    });
    $( "a.scroll" ).click(function( event ) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: $($(this).attr("href")).offset().top }, 1000);
    });
    $("#dropmenu").on('click',function(){
        if($(this).hasClass('dropmenu')){
            $("#top").removeClass('dropmenu');
        } else{
            $("#top").addClass('dropmenu');
        }
    });
});
