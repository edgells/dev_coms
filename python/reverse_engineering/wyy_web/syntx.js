(function () {

    function f(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
                e = Math.floor(e),
                c += b.charAt(e);
        return c

    }

    console.log(f(16))
}());

function j4n_bf4j(k4o, cF4J, O4S) {
  if (!k4o || !k4o.length || !j4n.gS6M(cF4J))
            return this;
        if (!!k4o.forEach) {
            k4o.forEach(cF4J, O4S);
            return this
        }
        for (var i = 0, l = k4o.length; i < l; i++)
            cF4J.call(O4S, k4o[i], i, k4o);
        return this
}

(function brx6r(cJp8h) {
    var m4q = [];
    j4n_bf4j(cJp8h, function (cJo8g) {
        m4q.push(Sc1x.emj[cJo8g])
    });
    return m4q.join("")
})