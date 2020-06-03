
//初始化高度
var height=document.documentElement.clientHeight
$("#myContent").css("height",height)
var csrf=$("input[name=csrfmiddlewaretoken]").val()

$("#uploadButton button").click(function(){
    var formData={}
    formData["title"]=$("#title textarea").val()
    formData["worksContent"]=$("#worksContent textarea").val()

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
        data:JSON.stringify(formData),
         success: function(data) {
            alert(data)
            if(data==0){
                window.location.assign("/worksManage/")
            }
        }
    });

})