$(window).on('load', function() {
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 100) {
            $('.fixed-top').addClass('menu-bg');
            if($('.menu-bg').length == 1 && $('.menu-bg-bot').length == 0){
                if($(window).width() > 768){
                    $('.fixed-bot').addClass('menu-bg-bot').css({
                        "opacity":"0",
                        "top":"110%",
                        "display":"block",
                    }).show().animate({
                        "opacity":"1",
                        "top":"90%"
                    })
                }else{
                    $('.fixed-bot').addClass('menu-bg-bot').css({
                        "opacity":"0",
                        "top":"110%",
                        "display":"block",
                    }).show().animate({
                        "opacity":"1",
                        "top":"90%"
                    })
                }
            }
            // $('.fixed-bot').addClass('menu-bg').css('display','block');
        } else {
            $('.fixed-top').removeClass('menu-bg');
            $('.fixed-bot').removeClass('menu-bg-bot').css('display','none');
        }
    });

});