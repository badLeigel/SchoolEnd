$("#postData button").click(function(){
    userId=$("#id").val()
    userName=$("#name").val()
    userPassword=$("#pwd").val()
    url="/selectUser/"
    if(userId!=""){
        url+=userId
        url+="/"
    }else{
        url+="0"
        url+="/"
    }
    if(userName!=""){
        url+=userName
        url+="/"
    }else{
        url+="none"
        url+="/"
    }
    if(userPassword!=""){
        url+=userPassword
        url+="/"
    }else{
        url+="none"
        url+="/"
    }
    window.location.assign(url)
})
$("#addUser button").click(function(){
    window.location.assign("/addUser/")
})
function deleteUser(e){
    id=e['id']
    $.ajax({
            url:"/deleteUser/"+id+"/",
            type:'GET',
            success:function(data){
                if(data==1){
                    window.location.assign("/userManage/")
                }else{
                    alert("删除失败")
                }
            }
    });
}

function changeUser(e){
    id=e['id']
    window.location.assign("/changeUser/"+id+"/")
}