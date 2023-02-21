function Comment() {

}
Comment.prototype.listencommitbtnclick = function(){

    $(".comment-btn").click(function () {
            var com = $('#message').val();
            var news_id =$('#message').attr('data-newsid');
            ccajax.post({
                'url': '/mdmain/comment/',
                'data': {
                    'comment': com,
                    'id': news_id
                },
                'success': function (res) {
                        if(res['code'] === 200){
                            var tpl = template('comment-item',{"comment": res['data']});
                            var commentListGroup = $(".comment-list");
                            commentListGroup.prepend(tpl);
                            console.log(commentListGroup.length);
                            window.messageBox.showSuccess('评论发表成功！');
                            $('#message').val("");
                        }
                }
            })
    })
};

Comment.prototype.run = function(){
    this.listencommitbtnclick();
};

$(function () {
    var comment = new Comment();
    comment.run();
});