import sys

import frida

def on_message(message, data):
    print(message, data)

jsCode = """
Java.perform(function() {
    var MainActivity = Java.use('com.example.myapplication.MainActivity');
    MainActivity.getString.implementation= function() {
        send("Start! hook");
        return "hook getString method";
    }
})"""

process = frida.get_remote_device().attach("com.example.myapplication")
script = process.create_script(jsCode)
script.on('message', on_message)
script.load()
sys.stdin.read()