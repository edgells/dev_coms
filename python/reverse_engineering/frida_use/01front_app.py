import frida

rdev = frida.get_usb_device()
front_app = rdev.get_frontmost_application()
print(front_app)