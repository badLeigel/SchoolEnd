//初始化高度
var height=document.documentElement.clientHeight
$("#myContent").css("height",height)

$("#loginButton").click(function(){
    window.location.assign("/login/")
})