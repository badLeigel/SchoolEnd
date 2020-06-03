//初始化高度
var height=document.documentElement.clientHeight
$("#myContent").css("height",height)
var csrf=$("input[name=csrfmiddlewaretoken]").val()

$("#registeredButton").click(function(){
    var id=$("#accountInput").val()
    var pwd=$("#passwordInput").val()
    var data = {};
    if(id!=""&&pwd!=""){
        data["name"] = id;
        data["password"] = pwd;

        $.ajaxSetup({
        beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrf);
            }
        });

        $.ajax({
            url:"/registered/",
            type:'POST',
            dataType:'json',
            contentType:'application/json;charset=UTF-8',
            data:JSON.stringify(data),
            success:function(data){
                    var error=$("<p>你的ID是："+data+"</p>")
                    error.css({"font-size":"24px","color":"red","margin-left":"24px"})
                    var a=$("#password").css("margin-top")
                    var b=parseInt(a.slice(0,2))
                    b-=24
                    var c=b.toString()+"px"
                    $("#password").css({"margin-top":c})
                    $("#password").before(error)
            }
        });
    }else{
        var error=$("<p>请填写完整信息</p>")
        error.css({"font-size":"24px","color":"red","margin-left":"24px"})
        var a=$("#password").css("margin-top")
        var b=parseInt(a.slice(0,2))
        b-=24
        var c=b.toString()+"px"
        $("#password").css({"margin-top":c})
        $("#password").before(error)
    }
})