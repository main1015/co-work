/**
 * Created by myth on 15-12-28.
 */
$(function(){
    $(".typing").typed({
        //strings: ["First sentence.", "Second sentence."],
        stringsElement: $('.txt'),
        //typeSpeed: 0,
        showCursor: false
    });

    $(".animation img").zoomy("click");
});