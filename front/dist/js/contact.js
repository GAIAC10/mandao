function Contact() {

}
Contact.prototype.listencontactbtnclickevent = function(){
    var usernameTag = $('input[name="username"]');
    var telephoneTag = $('input[name="telephone"]');
    var contentTag = $('textarea[name="content"]');
    $('.btn-contact').click(function () {
            var username = usernameTag.val();
            var telephone = telephoneTag.val();
            var content = contentTag.val();

            ccajax.post({
                'url': '/mdmain/contact/',
                'data':{
                    'username': username,
                    'telephone': telephone,
                    'content': content
                },
                'success': function (res) {
                    if(res['code'] === 200){
                        window.messageBox.showSuccess("留言成功！我们会尽快与您取得联系！")
                    }
                }
            })
    })
};

Contact.prototype.run = function () {
    this.listencontactbtnclickevent();
};


$(function () {
    var c = new Contact();
    c.run();
});