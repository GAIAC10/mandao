function CmsUser() {

}
CmsUser.prototype.listenturnblack = function(){
      $(".icon-lahei").click(function () {
          console.log(this);
          var name = this.getAttribute('data-name');
          var uid = this.getAttribute('data-uid');
            swal({
        title: "确认将"+name+"拉黑吗？",
        text: "拉黑后无法恢复！",
        type: "info",
        showCancelButton: true,
        cancelButtonText: "取消",
        showConfirmButton: true,
        confirmButtonText: "确定"
    },
    function () {
        ccajax.post({
            'url': '/cms/turn_black/',
            'data': {
                'id': uid,
            },
            'success': function (res) {
                if(res["code"] === 200){
                    window.messageBox.showSuccess("拉黑成功！")
                }else{
                window.messageBox.showError(res['message'])
            }
            }
        })
    }
)

      })
};

CmsUser.prototype.listendelblack = function(){
      $(".icon-chahao").click(function () {
          var name = this.getAttribute('data-name');
          var uid = this.getAttribute('data-uid');
            swal({
        title: "确认将"+name+"删除吗？",
        text: "删除后无法恢复！",
        type: "info",
        showCancelButton: true,
        cancelButtonText: "取消",
        showConfirmButton: true,
        confirmButtonText: "确定"
    },
    function () {
        ccajax.post({
            'url': '/cms/delete/',
            'data': {
                'id': uid,
            },
            'success': function (res) {
                if(res["code"] === 200){
                    window.messageBox.showSuccess("删除成功！");
                    window.location.reload()
                }else{
                window.messageBox.showError(res['message'])
            }
            }
        })
    }
)

      })
};

CmsUser.prototype.listenedit = function(){
      $(".icon-xiugai").click(function () {
          var uid = this.getAttribute('data-uid');
           swal({
      title: "<small>请输入相关信息</small>!",
      text: "图片描述 <input type='text' name='myinput' id='desc'>"
      +"链接 <input type='text' name='myinput' id='link'>"
      +"标题 <input type='text' name='myinput' id='name'>"
      +"优先级(优先级越高越前) <input type='text' name='myinput' id='youxian'>",
      html: true,
      type: "prompt",
      showCancelButton:true,
      cancelButtonText:'取消'
  }, function (inputValue) {
    var descTag = $("input[id='desc']").val();
    var linkTag = $("input[id='link']").val();
    var nameTag = $("input[id='name']").val();
    var youxianTag = $("input[id='youxian']").val();
    if(descTag== null){
        window.messageBox.showInfo("请输入图片描述");
    }else if(linkTag == null){
        window.messageBox.showInfo("请输入图片链接");
    }else if(nameTag == null){
        window.messageBox.showInfo("请输入图片标题");
    }else{
         window.messageBox.showInfo("请输入图片优先级");
    }
        ccajax.post({
            'url': '/cms/edit_banner/',
            'data': {
                'id': uid,
                'desc': descTag,
                'name': nameTag,
                'link': linkTag,
                'youxian': youxianTag,
            },
            'success': function (res) {
                if(res["code"] === 200){
                    window.messageBox.showSuccess("修改成功！");
                    window.location.reload()
                }else{
                window.messageBox.showError(res['message'])
            }
            }
        })
    }
           )
      })
};

CmsUser.prototype.listenchangeFile = function(){
    $("#uploadimg").change(function () {
      var file = $('#uploadimg')[0].files[0];
      var name = file['name'];
        $('input[name="img"]').val(name)
    })
};

CmsUser.prototype.listenuploadImg = function(){
    var descTag = $('input[name="desc"]');
    var linkTag = $('input[name="link"]');
    var youxianTag = $('input[name="youxian"]');
    var nameTag = $('input[name="title"]');
        $('.upload').click(function () {
            var desc = descTag.val();
            var link = linkTag.val();
            var youxian = youxianTag.val();
            var name = nameTag.val();
            var file =  $('#uploadimg')[0].files[0];
            var fileDate = new FormData();
            fileDate.append('file', file);
             ccajax.post({
            'url': '/mdmain/upload/',
            'data': fileDate,
            'processData': false,
            'contentType': false,
            'success': function (result) {
                if(result['code']===200){
                    var file_name = result['data'];
                    ccajax.post({
                        'url': '/mdmain/add_banners/',
                        'data': {
                            'img': file_name,
                            'link': link,
                            'banner_desc': desc,
                            'youxian': youxian,
                            'name': name,
                        },
                        'success': function (result) {
                            if(result["code"] === 200){
                                window.messageBox.showSuccess("上传成功！")
                            }
                        }
                    })
                }

            }
        })
        })
};
CmsUser.prototype.setCompanyBaseInformations = function(){
    var companyTag = $('input[name="company"]');
    var addrTag = $('input[name="addr"]');
    var kefuTag = $('input[name="kefu"]');
    var qqTag = $('input[name="qq"]');
    var telephoneTag = $('input[name="telephone"]');
    var emailTag = $('input[name="email"]');

    $(".save").click(function () {
        var company = companyTag.val();
        var addr = addrTag.val();
        var kefu = kefuTag.val();
        var qq = qqTag.val();
        var telephone = telephoneTag.val();
        var email = emailTag.val();
        var file =  $('#uploadimg')[0].files[0];
            var fileDate = new FormData();
            fileDate.append('file', file);
                  ccajax.post({
            'url': '/cms/upload/',
            'data': fileDate,
            'processData': false,
            'contentType': false,
            'success': function (result) {
                if(result['code']===200){
                    var file_name = result['data'];
                    ccajax.post({
                        'url': '/cms/wechatEcode/',
                        'data': {
                            'name': company,
                            'addr': addr,
                            'kefu': kefu,
                            'qq': qq,
                            'telephone': telephone,
                            'Email': email,
                            'wechat': file_name,
                        },
                        'success': function (result) {
                            if(result["code"] === 200){
                                window.messageBox.showSuccess("上传成功！")
                            }
                        }
                    })
                }

            }
        })
        // ccajax.post({
        //     'url': '/cms/webset/',
        //     'data': {
        //         'company': company,
        //         'addr': addr,
        //         'kefu': kefu,
        //         'qq': qq,
        //         'telephone': telephone,
        //         'email': email,
        //
        //     }
        // })
    })
};


CmsUser.prototype.listenadminedit = function(){
      $(".icon-bianji").click(function () {
          var uid = this.getAttribute('data-uid');
           swal({
      title: "<small>请输入相关信息</small>!",
      text: "管理密码 <input type='text' name='myinput' id='password'>",
      html: true,
      type: "prompt",
      showCancelButton:true,
      cancelButtonText:'取消',
      showConfirmButton:true,
                   confirmButtonText: "确定",
  },
               function (inputValue) {
               if(inputValue){
    var passwordTag = $("input[id='password']");
        ccajax.post({
            'url': '/cms/user/',
            'data': {
                'uid': uid,
                'password': passwordTag.val(),
            },
            'success': function (res) {
                if(res["code"] === 200){

                    ccajax.post({
                        'url': '/cms/send_sms/',
                        'data': {
                            'uid': uid,
                            'password': passwordTag.val(),
                        },
                        'success': function (res) {
                            if(res['code'] === 200){
                                window.messageBox.showSuccess('短信发送成功！');
                                window.location.reload()
                            }else{

                            }
                        }
                    });

                }else{
                window.messageBox.showError(res['message'])
            }
            }
        })
    }}
           )
      })
};

CmsUser.prototype.listenvipedit = function(){
      $(".icon-bianji1").click(function () {
          var uid = this.getAttribute('data-uid');
           swal({
      title: "<small>请输入相关信息</small>!",
      text: "会员密码 <input type='text' name='myinput' id='password'>",
      html: true,
      type: "prompt",
      showCancelButton:true,
      cancelButtonText:'取消',
               closeOnConfirm: false
  }.then(function (inputValue) {
      if(inputValue){
    var passwordTag = $("input[id='password']");
        ccajax.post({
            'url': '/cms/user/',
            'data': {
                'uid': uid,
                'password': passwordTag.val(),
            },
            'success': function (res) {
                if(res["code"] === 200){
                    window.messageBox.showSuccess("修改成功！");
                    ccajax.post({
                        'url': '/cms/send_sms/',
                        'data': {
                            'uid': uid,
                            'password': passwordTag.val(),
                        },
                        'success': function (res) {
                            if(res['code'] === 200){
                                window.messageBox.showSuccess('短信发送成功！');
                                window.location.reload()
                            }else{

                            }
                        }
                    });

                }else{
                window.messageBox.showError(res['message'])
            }
            }
        })
    }})
           )
      })
};

CmsUser.prototype.listencreateadminbuttonclickevent = function(){
    var usernameTag = $('input[name="username"]');
    var telephoneTag = $('input[name="telephone"]');
    var passwordTag = $('input[name="password"]');
        $('.create_admin').click(function () {
            var username = usernameTag.val();
            var telephone = telephoneTag.val();
            var password = passwordTag.val();
            var select  = $('#creat_admin').val();
            ccajax.post({
                'url': '/cms/creat_admin/',
                'data': {
                    'username':username,
                    'telephone': telephone,
                    'password': password,
                    'select': select
                },
                'success': function (res) {
                    if(res['code']===200){
                        window.messageBox.showSuccess("创建成功！")
                    }else{
                        window.messageBox.showError(res['message'])
                    }
                }
            })
        })
};

CmsUser.prototype.run = function(){
    this.listenturnblack();
    this.listendelblack();
    this.listenedit();
    this.listenchangeFile();
    this.listenuploadImg();
    this.setCompanyBaseInformations();
    this.listenvipedit();
    this.listencreateadminbuttonclickevent();
    this.listenadminedit();
};


$(function () {
    var user = new CmsUser();
    user.run()
});