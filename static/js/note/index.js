/**
 * Created with PyCharm.
 * User: myth
 * Date: 14-7-21
 * Time: 下午5:30
 * To change this template use File | Settings | File Templates.
 */

var $div = $('.note-ul');
var z = 1;
$('.note-li').drag("start",function (ev, dd) {
    dd.limit = $div.offset();
    var top = dd.limit.top;
    var left = dd.limit.left;
    var padding_w = ($div.innerWidth() - $div.width())/2;
    var padding_h = ($div.innerHeight() - $div.height())/2;
    var margin_w = ($(this).outerWidth(true) - $(this).outerWidth()) / 2;
    var margin_h = ($(this).outerHeight(true) - $(this).outerHeight()) / 2;
    dd.limit.top +=  padding_w;
    dd.limit.left +=  padding_h;

    dd.limit.bottom = top + ($div.outerHeight()-padding_w) - $(this).outerHeight()-margin_w;
    dd.limit.right = left + ($div.outerWidth() - padding_h) - $(this).outerWidth()-margin_h;
    $(this).css('zIndex', z++);
}).drag(function (ev, dd) {
    $(this).css({
        top: Math.min(dd.limit.bottom, Math.max(dd.limit.top, dd.offsetY)),
        left: Math.min(dd.limit.right, Math.max(dd.limit.left, dd.offsetX))
    });
}).click(function(e){
    $(this).css('zIndex', z++);
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

    var padding_w = ($(this).innerWidth() - $(this).width()) / 2;
    var padding_h = ($(this).innerHeight() - $(this).height()) / 2;
    var x = e.offsetX;
    var y = e.offsetY;
    var _x = x - padding_w;
    var _y = y - padding_h;

    _x = Math.min(Math.max(0, _x), 650);
    _y = Math.min(Math.max(0, _y), 415);

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