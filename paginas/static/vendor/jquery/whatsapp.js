$(window).scroll(function() {
    var winScrollTop = $(window).scrollTop();
    var winHeight = $(window).height();
    var floaterHeight = $('#whats').outerHeight(true);
    var fromBottom = 20;
    var top = winScrollTop + winHeight - floaterHeight - fromBottom;
	$('#whats').css({'top': top + 'px'});
});

$("#whats").on({
    mouseenter :function(){
        $("#whats").css("background-color","#202d40");
    } ,
    mouseleave :function(){
        $("#whats").css("background-color","#77badd");
    }
});
