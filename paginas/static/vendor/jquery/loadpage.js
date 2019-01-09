$(function(){
    $("html").addClass('cl-preload');
})
$(window).on('load',function(){
    $("#loader").fadeOut("slow", function() {
        // will fade out the whole DIV that covers the website.
        $("#preloader").delay(300).fadeOut("slow");
        $("html").removeClass('cl-preload');
        $("html").addClass('cl-loaded');
    }); 
});
