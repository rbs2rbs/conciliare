$(document).ready(function(){
    var caixa = $("#caixa").children();
    if (screen.width < 769) {
        console.log('cel');
        caixa.each(function(i){
            if($(this).hasClass("divisor")==false){
                $(this).removeClass("col");
                $(this).addClass("col-sm-3");
            } else{
                $(this).removeClass("divisor");
            }
        });
    }
});

