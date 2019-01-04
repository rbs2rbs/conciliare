$(function(){
    var slide = $(".carousel-item");
    if (screen.width < 769) {
        slide.on('swiperight', function (e) { 
        $('.carousel-control-prev-icon').click();
        });
    
        slide.on('swipeleft', function (e) {
        $('.carousel-control-next-icon').click();
        });
    }
});

