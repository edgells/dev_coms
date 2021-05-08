(function(X4b, e4i) {
        var i4m = {}
          , e4i = NEJ.X({}, e4i)
          , mx8p = X4b.indexOf("?");
        if (window.GEnc && /(^|\.com)\/api/.test(X4b) && !(e4i.headers && e4i.headers[et5y.BT5Y] == et5y.Ku9l) && !e4i.noEnc) {
            if (mx8p != -1) {
                i4m = j4n.gN6H(X4b.substring(mx8p + 1));
                X4b = X4b.substring(0, mx8p)
            }
            if (e4i.query) {
                i4m = NEJ.X(i4m, j4n.fV6P(e4i.query) ? j4n.gN6H(e4i.query) : e4i.query)
            }
            if (e4i.data) {
                i4m = NEJ.X(i4m, j4n.fV6P(e4i.data) ? j4n.gN6H(e4i.data) : e4i.data)
            }
            i4m["csrf_token"] = u4y.gU6O("__csrf");
            X4b = X4b.replace("api", "weapi");
            e4i.method = "post";
            delete e4i.query;
            var bZe2x = window.asrsea(JSON.stringify(i4m), brx6r(["流泪", "强"]), brx6r(Sc1x.md), brx6r(["爱心", "女孩", "惊恐", "大笑"]));
            e4i.data = j4n.cr4v({
                params: bZe2x.encText,
                encSecKey: bZe2x.encSecKey
            })
        }
        var cdnHost = "y.music.163.com";
        var apiHost = "interface.music.163.com";
        if (location.host === cdnHost) {
            X4b = X4b.replace(cdnHost, apiHost);
            if (X4b.match(/^\/(we)?api/)) {
                X4b = "//" + apiHost + X4b
            }
            e4i.cookie = true
        }
        cJn8f(X4b, e4i)
    })