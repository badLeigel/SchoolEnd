$("#choise1").css("background-color","#061334")
$("#choise3").css("background-color","#050c1c")
//初始化高度
var height=document.documentElement.clientHeight
$("#myContent").css("height",height)
var csrf=$("input[name=csrfmiddlewaretoken]").val()

$("#uploadButton button").click(function(){
    console.log("dianjile")
    var formData=new FormData();
    formData.append("file",$("#works").files[0])
    formData.append("video",$("#video").files[0])
    formData.append("title",$("#title textarea").val())
    formData.append("worksContent",$("#worksContent textarea").val())


    $.ajax({
    url: window.location.href,
    type:'POST',
    data: formData,
    cache: false,
    processData: false,
    contentType: false,
    success: function(data) {
        if(data==0){
            }
        }
    });

})