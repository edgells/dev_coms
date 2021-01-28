import ctypes

dll = ctypes.WinDLL("user32.dll")
dll.LockWorkStation()
