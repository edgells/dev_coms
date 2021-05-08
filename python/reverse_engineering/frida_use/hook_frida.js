if(Java.available) {
    Java.perform(function () {
        // 这是包名（文件名）
        var class_u = Java.use('com.sina.weibo.wcfc.sobusiness.UtilitySo');
        // 定位到方法  function(paraml)括号里是这个方法的参数
        class_u.newCalculateS.implementation=function(a, paraml){
            //控制台打印消息
        send("got it c");
        send(a);
        send(paraml);
        // 给方法运行成功后返回的值
        var result = this.newCalculateS(a, paraml);
        send(result);
        return result;
        };
    });
}