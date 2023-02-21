function Upload() {

}

Upload.prototype.listenFileUploadBtn = function(){
    var uploadbtn = $('#thumbnail-btn');
    uploadbtn.click(function (e) {
        e.preventDefault();
        var file = $("#banner")[0].files[0];
        console.log(file);
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
                            'banner_desc': $("#banner_desc").val(),
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

Upload.prototype.run = function () {
    this.listenFileUploadBtn()
};


$(function () {
    var up = new Upload();
    up.run()
});