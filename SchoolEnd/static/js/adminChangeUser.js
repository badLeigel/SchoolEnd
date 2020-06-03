$("#loginButton").click(function(){
    id=$("#accountInput").val()
    name=$("#username").val()
    password=$("#passwordInput").val()
    data={}
    data["id"]=id
    data["password"]=password
    data["name"]=name
    csrf=$("#csrf input").val()
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
                    var error=$("<p>你输入的用户id已经重复</p>")
                    error.css({"font-size":"24px","color":"red","margin-left":"24px"})
                    var a=$("#password").css("margin-top")
                    var b=parseInt(a.slice(0,2))
                    b-=24
                    var c=b.toString()+"px"
                    $("#password").css({"margin-top":c})
                    $("#password").before(error)

                }else{
                    window.location.assign("/userManage/");
                }
            }
        });
})