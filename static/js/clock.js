/**
 * Created with PyCharm.
 * User: myth
 * Date: 14-7-23
 * Time: 下午3:49
 * To change this template use File | Settings | File Templates.
 */

$(function(){

    var hour = $('#clock-hour');
    var minute = $('#clock-minute');
    var second = $('#clock-second');

    function AddZero(n) {
        if (n < 10) {
            return '0' + n;
        }
        return '' + n;
    }

    function showTime() {

        var oDate = new Date();
        var iHours = oDate.getHours();
        var iMinute = oDate.getMinutes();
        var iSecond = oDate.getSeconds();

        hour.text(AddZero(iHours));
        minute.text(AddZero(iMinute));
        second.text(AddZero(iSecond));

    }

    showTime();
    setInterval(showTime,1000);
});
