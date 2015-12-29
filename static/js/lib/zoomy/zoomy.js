/**
 * Created by myth on 15-12-28.
 */

! function($){
    var Zoomy = function(el, options){
        this.el = $(el);
         // options
        this.options = $.extend({}, $.fn.zoomy.defaults, options);
        this.init(options);
    };
    Zoomy.prototype = {
        constructor: Zoomy,
        init: function(options){
            var self = this;
            self.click(options)

        },
        click: function(options){
            var self = this;
            $(self.el).on("click",function(){
                console.log("2");
                self._html(self.el);
                //self._css(self.el)
            });
            console.log("1");
        },
        _html: function(ele){
            var div = "<div id='zoomy'>111</div>";
            var offset = $(ele).offset();
            var left = offset.left;
            var top = offset.top;
            var width = $(ele).width();
            var height = $(ele).height();
            div = $(div).insertAfter(ele);
            console.log(div);
            div.css("position", "absolute");
            div.css("z-index", "999");
            div.css("top", top+"px");
            div.css("left", left + "px");
            div.css("min-width", "200px");
            div.css("min-height", "200px");
            div.css("border", "1px green solid");
            div.addClass("clearfix");

        },
        _css:function(ele){
            var offset = $(ele).offset();
            var width = $(ele).width();
            //var max_width = screen.width;
            var max_width = $("body").width();
            var left = offset.left;
            var top = offset.top;
            var zoom = 1.5;

            var _left = max_width - zoom * width;

            $.keyframe.define([{
                name: 'wt',
                '0%': {'transform' : 'translateX(20px) rotate(10deg)'},
                '30%': {'transform' :'translateX(60px) rotate(50deg)'},
                '60%': {'transform' : 'translateX(100px) rotate(90deg)'},
                '100%': {'transform' : 'translateX(120px) rotate(180deg)'}
            }]);
            $(ele).playKeyframe({
                name: 'wt',
                duration: "3s",
                timingFunction: 'linear',
                delay: "0.1s",
                iterationCount: '1'
            });
        }
    };
    /*$.fn.zoomy = function (method) {
        console.log(method);
        if (methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        } else if (typeof method === 'object' || !method) {
            return methods.init.apply(this, arguments);
        } else {
            $.error('Method ' + method + ' does not exist on jQuery.zoomy');
        }
    };*/

    $.fn.zoomy = function(option){
        return this.each(function() {
            var $this = $(this),
                data = $this.data('typed'),
                options = typeof option == 'object' && option;

            //if (!data) $this.data('typed', (data = new Zoomy(this, options)));
            //if (typeof option == 'string') data[option]();
            return new Zoomy(this, options)
        });
    };

    $.fn.zoomy.defaults = {

    };
}(window.jQuery);