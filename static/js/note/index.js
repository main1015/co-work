/**
 * Created with PyCharm.
 * User: myth
 * Date: 14-7-21
 * Time: 下午5:30
 * To change this template use File | Settings | File Templates.
 */

var $div = $('.note-ul');
var z = 1;
var note_x = 196;
var note_y = 210;
var maxY = 455;
var maxX = 725;

$('.note-li').drag(function (ev, dd) {
    var div = $div.offset();
    var padding_w = ($div.innerWidth() - $div.width())/2;
    var padding_h = ($div.innerHeight() - $div.height())/2;
    var margin_w = ($(this).outerWidth(true) - $(this).outerWidth()) / 2;
    var margin_h = ($(this).outerHeight(true) - $(this).outerHeight()) / 2;

    //var Y = dd.offsetY - (div.top + padding_h);
    //var X = dd.offsetX - (div.left + padding_w);
    //
    var Y = dd.offsetY - (div.top + margin_h);
    var X = dd.offsetX - (div.left + margin_w);

    //var maxY = $div.height() - note_y;
    //var maxX = $div.width() - note_x;

    $(this).css({
        top: Math.min(maxY, Math.max(0, Y)),
        left: Math.min(maxX, Math.max(0, X))
    });
}).mouseenter(function(e){
    var zIndex = $(this).css('zIndex');
    zIndex = isNaN(parseInt(zIndex))? 0: parseInt(zIndex);
    $(this).css('zIndex', Math.min(zIndex + 500, 999));
}).mouseleave(function(e){
    var zIndex = $(this).css('zIndex');
    zIndex = isNaN(parseInt(zIndex))? 0: parseInt(zIndex);
    $(this).css('zIndex', Math.max(0, zIndex - 500));
}).dblclick(function(e){
        var title = $(this).find(".m-title")
        var content = $(this).find(".m-content")
        var pre = $("<pre></pre>").text(content.text());
        $("#showModalLabel").text(title.text());
        $("#showContent").html(pre);
        $('#show_modal').modal('toggle');
});


//$(".a-tab").click(function(e){
//    e.preventDefault();
//});

$div.dblclick(function(e){
    var _this = e.target == this;
    if(!_this){
        return;
    }
    //var maxY = $div.height() - note_y;
    //var maxX = $div.width() - note_x;

    var padding_w = ($(this).innerWidth() - $(this).width()) / 2;
    var padding_h = ($(this).innerHeight() - $(this).height()) / 2;
    var x = e.offsetX;
    var y = e.offsetY;
    var _x = x - padding_w;
    var _y = y - padding_h;

    _x = Math.min(Math.max(0, _x), maxX);
    _y = Math.min(Math.max(0, _y), maxY);

    var form = $("#iform");
    form.find("#x").val(_x);
    form.find("#y").val(_y);

    $('#add_modal').modal('toggle');
});

$(".div-hr i").click(function(e){
    var hr = $('.div-hr hr');
    var hide = $('.hide-div');
    if(hide.hasClass('hide')){
        hide.removeClass('hide');
        hr.removeClass('hide');
        $(this).removeClass('icon-chevron-down').addClass('icon-chevron-up');
    }else{
        hide.addClass('hide');
        hr.addClass('hide');
        $(this).removeClass('icon-chevron-up').addClass('icon-chevron-down');
    }
});