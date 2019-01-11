$(function(){
    if(screen.width < 769){
        $(".linha-servico").each(function(){
            $(this).removeClass();
        });

        $('#boneco').each(function () {
            $(this).insertBefore($(this).prev('.boneco'));
        });
        console.log($(".caneta"));
        console.log($(".boneco"));
        $('#caneta').each(function () {
            $(this).insertBefore($(this).prev('.caneta'));
        });
    }
})