function Map() {

}

function checkPhone(val) {

     var
 re = /^1\d{10}$/;
    if (re.test(val)) {
        alert("正确");
        return true
    } else {
        alert("错误");
        return false
    }

}

Map.prototype.search_current_x_y = function(){
    var search = $('.search');
    var main_btn = $(".obscure");
    main_btn.click(
        function () {
            window.location.replace("https://campustm.cn")
        }
    );
    search.click(function () {
        ccajax.post({
            'url': '/map/search_x_y/',
            'data': {
            },
            'success': function (res) {
                window.init = function(){
                    alert(res['data']['x']);
                    var marker = new AMap.Marker({
    position: new AMap.LngLat(res['data']['y'], res['data']['x']),   // 经纬度对象，也可以是经纬度构成的一维数组[116.39, 39.9]
    title: '当前位置'
});
                    var map = new AMap.Map('container', {
                    center:[res['data']['y'],res['data']['x']],
                    zoom:15,
        });
                    map.add(marker)
    }()
            }
        })
    })
};


Map.prototype.set_hurryTelephoneEvent = function() {
    $('#set_telephone').click(function () {
        swal("请设置紧急联系人电话号码！", {
            content: "input",
        })
            .then((value) => {
                if (checkPhone(value)) {
                ccajax.post({
                    'url': '/mdmain/set_telephone/',
                    'data': {
                        'uid': $('#set_telephone').attr('data-uid'),
                        'telephone': value
                    },
                    'success':function (res) {
                        if (res['code'] === 200) {
                            swal(`你设置的联系人电话为: ${value}`);
                        }
                    }
                });
            }

            });
    })
};

Map.prototype.run = function () {
    this.search_current_x_y();
    this.set_hurryTelephoneEvent();
};

$(function () {
    var map = new Map();
    map.run()
});