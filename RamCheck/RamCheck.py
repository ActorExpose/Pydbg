import ctypes

class MemoryStatus(ctypes.Structure):
	_fields_ = [
		("dwLength", ctypes.c_ulong),
		("dwMemoryLoad", ctypes.c_ulong),
		("ullTotalPhys", ctypes.c_ulonglong),
		("ullAvailPhys", ctypes.c_ulonglong),
		("ullTotalPageFile", ctypes.c_ulonglong),
		("ullAvailPageFile", ctypes.c_ulonglong),
		("ullTotalVirtual", ctypes.c_ulonglong),
		("ullAvailVirtual", ctypes.c_ulonglong),
		("sullAvailExtendedVirtual", ctypes.c_ulonglong),
	]

m = MemoryStatus()
m.dwLength = ctypes.sizeof(m)
ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
ram = m.ullTotalPhys/1073741824

if ram <= 2:
	print("Running in a vm...")
	exit()

print("All good")