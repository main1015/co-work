路由规范
=====

get
------
    所有路由方法都必须在后面添加_page的后缀。如下：

        def user_register_page():


post
------
    在路由后面添加.post的后缀。如下：

        @user_page.route('/u/register.post', methods=('POST',))

    所有路由方法都必须在后面添加_post_page的后缀。如下：

        def user_register_post_page():
