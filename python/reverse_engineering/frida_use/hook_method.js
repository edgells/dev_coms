Java.perform(function() {
    var MainActivity = Java.use('com.example.myapplication1.MainActivity');
    // 注意这个方法是否有重载
    MainActivity.getString.overload().implementation= function() {
        send("Start! hook");
        return "hook getString method";
    }
})