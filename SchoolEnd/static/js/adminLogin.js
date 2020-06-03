//初始化高度
var height=document.documentElement.clientHeight
$("#myContent").css("height",height)
var csrf=$("input[name=csrfmiddlewaretoken]").val()

//登陆按钮点击触发事件
$("#loginButton").click(function(){
    var id=$("#accountInput").val()
    var pwd=$("#passwordInput").val()
    if(id!=""&&pwd!=""){
        var data = {};
        data["Id"] = id;
        data["password"] = pwd;
        //make cookies

        //
        $.ajaxSetup({
        beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrf);
            }
        });

        $.ajax({
            url:window.location.href,
            type:'POST',
            dataType:'json',
            contentType:'application/json;charset=UTF-8',
            data:JSON.stringify(data),
            success:function(data){
                if(data!=1){
                    var error=$("<p>帐号或密码错误</p>")
                    error.css({"font-size":"24px","color":"red","margin-left":"24px"})
                    var a=$("#password").css("margin-top")
                    var b=parseInt(a.slice(0,2))
                    b-=24
                    var c=b.toString()+"px"
                    $("#password").css({"margin-top":c})
                    $("#password").before(error)

                }else{
                    window.location.assign("/adminPage/");
                }
            }
        });
    }else{
        var error=$("<p>清填写完整信息</p>")
                    error.css({"font-size":"24px","color":"red","margin-left":"24px"})
                    var a=$("#password").css("margin-top")
                    var b=parseInt(a.slice(0,2))
                    b-=24
                    var c=b.toString()+"px"
                    $("#password").css({"margin-top":c})
                    $("#password").before(error)
    }
})

//注册按钮点击触发事件
$("#registeredButton").click(function(){
    window.location.assign("/registered/")
})