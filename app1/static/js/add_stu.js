function add_click() {
    $('.dropdown-menu a').click(function () {
            //获取点击的超链接的内容
            let txt = $(this).text();
            $(this).parents('.dropdown').children('button').html(txt);
        });
}


function ajax_request(url, data, method, callback) {
    $.ajax({
        url:url,
        data:data,
        type:method,
        success:function (res) {
            callback(JSON.parse(res));
        }
    })
}