$(document).ready(function () {
//making product card jump
        $(".anup").css('cursor','pointer').mouseenter(function () {
            $(this).animate({ "top": "-25px" }, 400)
           
        });
        $(".anup").mouseleave(function () {
         
            $(this).animate({ "top": "+0px" }, 400)
        });

//hide and show review box 
$(".review-box").css('display', 'none');
$("#show").css('cursor','pointer').click(function(){
  $(".review-box").toggle(1500)
});
    });