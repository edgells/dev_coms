import frida

dev = frida.get_usb_device(timeout=5)

processes = dev.enumerate_processes()
for process in processes:
    print(process)