import shutil

disk = shutil.disk_usage("/")
total = disk.total
used = disk.used
free = disk.free

total_gb = total / (1024 ** 3)
used_gb = used / (1024 ** 3) 
free_gb = free / (1024 ** 3)
percent = used / total * 100

print("=" * 40)
print("DISK MONITOR")
print("=" * 40)
print(f"Total: {total_gb:.2f} GB")
print("=" * 40)
print(f"Used: {used_gb:.2f} GB")
print("=" * 40)
print(f"Free: {free_gb:.2f} GB")
print("=" * 40)

if percent >= 90:
    status = ("Critical low!!")
elif percent >= 60:
    status = ("Medium")
else:
    status = ("Normal")

print(f"Usage: {percent:.1f}% - {status} space")
