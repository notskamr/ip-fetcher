import socket
import requests
import tkinter as tk



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

ext_ip = requests.get('http://ifconfig.me/ip').text

def copy_ip():
    clipboard = tk.Tk()
    clipboard.withdraw()
    clipboard.clipboard_clear()
    clipboard.clipboard_append(ip)
    clipboard.update()
    clipboard.destroy()

def copy_ext_ip():
    clipboard = tk.Tk()
    clipboard.withdraw()
    clipboard.clipboard_clear()
    clipboard.clipboard_append(ext_ip)
    clipboard.update()
    clipboard.destroy()


window = tk.Tk()
window.title("IP Fetcher")
window.geometry("225x50")

icon = tk.PhotoImage(file = "D:\Skamr\Documents\ip-fetcher\icon.png")
window.iconphoto(False, icon)
ip_frame = tk.Frame(master=window)
ext_ip_frame = tk.Frame(master=window)

ip_widget = tk.Label(text="Internal IP: " + ip, master=ip_frame)
ip_copy = tk.Button(text="Copy", master=ip_frame, command=copy_ip)
ext_ip_widget = tk.Label(text="External IP: " + ext_ip, master=ext_ip_frame)
ext_ip_copy = tk.Button(text="Copy", master=ext_ip_frame, command=copy_ext_ip)

ip_widget.pack(side=tk.LEFT)
ip_copy.pack(side=tk.RIGHT)

ext_ip_widget.pack(side=tk.LEFT)
ext_ip_copy.pack(side=tk.RIGHT)

ip_frame.pack(fill=tk.BOTH)
ext_ip_frame.pack(fill=tk.BOTH)


window.mainloop()
