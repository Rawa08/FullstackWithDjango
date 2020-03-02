$(document).ready(function () {

        $(".anup").css('cursor','pointer').mouseenter(function () {
            $(this).animate({ "top": "-25px" }, 400)
           
        });
        $(".anup").mouseleave(function () {
         
            $(this).animate({ "top": "+0px" }, 400)
        });

$(".review-box").css('display', 'none');
$("#show").css('cursor','pointer').click(function(){
  $(".review-box").show('easout');
});
    });