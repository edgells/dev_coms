        var cpr5w = function(C4G, J4N) {
            this.tk3x.setRequestHeader(J4N, C4G)
        };
        return function(e4i) {
            var gz6t = e4i.request
              , qd9U = e4i.headers;
            this.tk3x = bk4o.byp8h();
            if (qd9U[et5y.BT5Y] === et5y.Ku9l) {
                delete qd9U[et5y.BT5Y];
                this.tk3x.upload.onprogress = this.gK6E.f4j(this, 1);
                if (gz6t.data.tagName === "FORM")
                    gz6t.data = new FormData(gz6t.data)
            }
            this.tk3x.onreadystatechange = this.gK6E.f4j(this, 2);
            if (gz6t.timeout != 0) {
                this.dJ5O = window.setTimeout(this.gK6E.f4j(this, 3), gz6t.timeout)
            }
            this.tk3x.open(gz6t.method, gz6t.url, !gz6t.sync);
            j4n.eR5W(qd9U, cpr5w, this);
            if (!!this.rg9X.cookie && "withCredentials"in this.tk3x)
                this.tk3x.withCredentials = !0;
            this.tk3x.send(gz6t.data)
        }