# youdao fanyi param
"""
    i: python
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: "" + (new Date).getTime() +
sign: 585c6405e17f42b66c1dd45644d93c78
lts: 1618452562055
bv: 77f6f59a0018c726a082dbc8637b193e
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME

      var n = e("./jquery-1.7");        // 导入 jquery dom 对象，
        e("./utils");
        e("./md5");
        var r = function (e) {
            var t = n.md5(navigator.appVersion)
                , r = "" + (new Date).getTime()
                , i = r + parseInt(10 * Math.random(), 10);
            return {
                ts: r,
                bv: t,
                salt: i,
                sign: n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")
            }
        };

"""
import hashlib
import time
import random

bv = hashlib.md5(b"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36").hexdigest()
ts = int(time.time() * 1000)
salt = ts + random.randint(0, 10)


"""
    总结
    1. 明白发起翻译请求的类型
    2. 分析请求格式， url, header, formdata
    3. 找到相关的js
"""