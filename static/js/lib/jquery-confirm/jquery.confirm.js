/**
 * Created with PyCharm.
 * User: myth
 * Date: 14-7-24
 * Time: 下午5:00
 * To change this template use File | Settings | File Templates.
 */
(function($){

	$.confirm = function(params){

		if($('#confirmOverlay').length){
			// A confirm is already shown on the page:
			return false;
		}

		var buttonHTML = '';
		$.each(params.buttons,function(name,obj){

			// Generating the markup for the buttons:

            var title = name;
            if(obj.title){
                title = obj.title;
            }
			buttonHTML += '<a href="#" class="button '+obj['class']+'">'+title+'<span></span></a>';

			if(!obj.before){
				obj.before = function(){};
			}
            if(!obj.after){
                obj.after = function () {};
            }
		});

		var markup = [
			'<div id="confirmOverlay">',
			'<div id="confirmBox">',
			'<h1>',params.title,'<i class=', params.icon,'></i></h1>',
			'<p>',params.message,'</p>',
			'<div id="confirmButtons">',
			buttonHTML,
			'</div></div></div>'
		].join('');

		$(markup).hide().appendTo('body').fadeIn();

		var buttons = $('#confirmBox .button'),
			i = 0;

		$.each(params.buttons,function(name,obj){
			buttons.eq(i++).click(function(){

				// Calling the action attribute when a
				// click occurs, and hiding the confirm.

				obj.before();
				$.confirm.hide(obj.after);
				return false;
			});
		});
	}

	$.confirm.hide = function(callback){
		$('#confirmOverlay').fadeOut(function(){
			$(this).remove();
            callback && callback();
		});
	}

})(jQuery);