/**
 * Created with PyCharm.
 * User: myth
 * Date: 14-7-17
 * Time: 上午11:51
 * To change this template use File | Settings | File Templates.
 */

//$('#add_modal').modal({
//  keyboard: false
//})

$('#iform').datepicker({
            inputs: $('#entry_at,#dimission_at'),
            format: "yyyy-mm-dd",
            todayBtn: "linked",
            autoclose: true,
            language: "zh-CN"
        });


$('#resign-switch').on('switch-change', function (e, data) {
    var $el = $(data.el)
      , value = data.value;
    var dimission_ele = $(".action-dimission");
    var dimission_txt = $('#dimission_at');
    var is_resign_txt = $("#is_resign");
    if(value){
        dimission_ele.removeClass('hide');
        dimission_txt.val(dimission_txt.attr('data-val'));
        is_resign_txt.val(1);
    }else{
        dimission_ele.addClass('hide');
        dimission_txt.attr('data-val', dimission_txt.val());
        dimission_txt.val('');
        is_resign_txt.val(0);

    }
});


function _alter(msg){
    $.confirm({
        'title': '操作提示',
        'message': msg,
        'buttons': {
            'Yes': {
                'class': 'blue',
                'title': '确定'

            },
            'No': {
                'class': 'gray',
                'title': '取消'
            }
        }
    });
}

$(".delete").click(function(e){
    var $this = $(this);
    var id = $this.data('id');
    $.confirm({
        'title': '删除工作经历',
        'message': '你确定删除工作经历，删除后将不能恢复！',
        'buttons': {
            'Yes': {
                'class': 'blue',
                'title': '确定',
                'after': function () {

                    $.post('/u/del/work_experience/'+id, function(data){
                        if(data.code == 200){
                            var row = $this.closest('.introduce-body');
                            row.remove();
                        }
                        _alter(data.msg);
                    }, "json");
                }
            },
            'No': {
                'class': 'gray',
                'title': '取消'
            }
        }
    });
});
