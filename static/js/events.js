$(document).ready(function () {
/*    $("#s1").click(function () {
        alert('1')
    });
    $("#s2").click(function () {
        alert('2')
    });
    $("#s3").click(function () {
        alert('3')
    });
    $("#s4").click(function () {
        alert('4')
    });
    $("#s5").click(function () {
        alert('5')
    });

*/
        $(".anup").mouseenter(function () {
            $(this).animate({ "top": "-25px" }, 400)
           
        });
        $(".anup").mouseleave(function () {
         
            $(this).animate({ "top": "+0px" }, 400)
        });


    });