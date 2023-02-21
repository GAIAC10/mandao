function Auth() {

}

Auth.prototype.loginbtnClickEvent = function(){
    var btn = $('.login-button');
    btn.click(function () {
        var telephone = $('input[name="telephone"]').val();
        var password = $("input[name='password']").val();
        ccajax.post({
            'url': '/auth/login/',
            'data': {
                'telephone': telephone,
                'password': password
            },
            'success': function (result) {
                console.log(result);
                if(result["code"] === 200){
                    window.messageBox.showSuccess("登录成功！");
                    if (result["data"] == "super"){
                        window.location.replace("https://campustm.cn/cms")
                    }
                    else{
                        window.location.replace("https://campustm.cn/map/map")
                    }
                }else{
                    window.messageBox.showError(result["message"]);
                    setTimeout(function(){window.location.reload()}, 3000);
                    if (result["message"] === "您已登陆！"){
                        window.location.replace('https://campustm.cn/map/map')
                    }

                }
            },
            'failed': function (error) {
                window.messageBox.showError(error)
            }
        })
    })
};



Auth.prototype.run = function () {
    this.loginbtnClickEvent();

};


$(function () {
    var auth = new Auth();
    auth.run();
});