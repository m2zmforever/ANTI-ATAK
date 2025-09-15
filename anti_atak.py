import os
import time
import subprocess
import threading
import platform
import psutil

try:
    import ctypes
except Exception:
    ctypes = None

try:
    from win10toast import ToastNotifier
except Exception:
    ToastNotifier = None

try:
    from plyer import notification
except Exception:
    notification = None

ASCII_ART = r"""
▄████████ ███▄▄▄▄       ███      ▄█     ▄████████     ███        ▄████████    ▄█   ▄█▄ 
  ███    ███ ███▀▀▀██▄ ▀█████████▄ ███    ███    ███ ▀█████████▄   ███    ███   ███ ▄███▀ 
  ███    ███ ███   ███    ▀███▀▀██ ███▌   ███    ███    ▀███▀▀██   ███    ███   ███▐██▀   
  ███    ███ ███   ███     ███   ▀ ███▌   ███    ███     ███   ▀   ███    ███  ▄█████▀    
▀███████████ ███   ███     ███     ███▌ ▀███████████     ███     ▀███████████ ▀▀█████▄    
  ███    ███ ███   ███     ███     ███    ███    ███     ███       ███    ███   ███▐██▄   
  ███    ███ ███   ███     ███     ███    ███    ███     ███       ███    ███   ███ ▀███▄ 
  ███    █▀   ▀█   █▀     ▄████▀   █▀     ███    █▀     ▄████▀     ███    █▀    ███   ▀█▀ 
                                                                                ▀         

    made by m2_zm 2024-2025 © MIT - PERSONAL USAGE ONLY
"""

def set_console_title(title: str = "Anti-Atak || discord m2_zm.") -> None:
    try:
        os.system(f"title {title}")
    except Exception:
        pass

def kill_and_restart_processes() -> None:
    try:
        subprocess.call(["taskkill", "/F", "/IM", "servisatk.exe"], shell=False)
    except Exception:
        pass
    try:
        subprocess.call(["taskkill", "/F", "/IM", "explorer.exe"], shell=False)
    except Exception:
        pass
    time.sleep(0.4)
    try:
        subprocess.Popen(["explorer.exe"], shell=False)
    except Exception:
        pass

def show_notification(title: str, msg: str) -> None:
    if ToastNotifier is not None:
        try:
            toaster = ToastNotifier()
            toaster.show_toast(title, msg, duration=10, threaded=False)
            return
        except Exception:
            pass
    if notification is not None:
        try:
            notification.notify(title=title, message=msg, timeout=10)
            return
        except Exception:
            pass

def show_notification_delayed(title: str, msg: str, delay: float = 10.0) -> None:
    try:
        timer = threading.Timer(delay, lambda: show_notification(title, msg))
        timer.daemon = True
        timer.start()
    except Exception:
        pass

def main() -> None:
    set_console_title()
    print(ASCII_ART)
    kill_and_restart_processes()
    show_notification_delayed("Akıllı Tahta Akıllı Kontrol:", "Sayın Developer m2_zm Hoş Geldiniz!", delay=10.0)

    print("\n--- Sistem Bilgileri ---")
    print(f"Bilgisayar Adı: {platform.node()}")
    print(f"İşletim Sistemi: {platform.system()} {platform.release()} ({platform.version()})")
    # İnternet bağlantısı kontrolü
    import urllib.request
    site_url = "http://m2zm.is-best.net"
    try:
        response = urllib.request.urlopen(site_url, timeout=5)
        if response.status == 200:
            print(f"İnternet Bağlantısı: Var ({site_url})")
        else:
            print(f"İnternet Bağlantısı: Yok veya siteye erişilemiyor ({site_url}, Durum kodu: {response.status})")
    except Exception:
        print(f"İnternet Bağlantısı: Yok veya siteye erişilemiyor ({site_url})")
    try:
        cpu = platform.processor()
        if not cpu:
            cpu = platform.uname().processor
        print(f"CPU: {cpu}")
    except Exception:
        print("CPU bilgisi alınamadı.")
    try:
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"IP Adresi: {ip_address}")
    except Exception:
        print("IP bilgisi alınamadı.")
    try:
        ram = psutil.virtual_memory()
        print(f"Toplam RAM: {round(ram.total / (1024**3), 2)} GB")
    except Exception:
        print("RAM bilgisi alınamadı.")
    try:
        print("Depolama Alanları:")
        partitions = psutil.disk_partitions()
        for p in partitions:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                print(f"  {p.device} ({p.mountpoint}): {round(usage.free / (1024**3), 2)} GB / {round(usage.total / (1024**3), 2)} GB boş")
            except Exception:
                print(f"  {p.device} ({p.mountpoint}): Bilgi alınamadı.")
    except Exception:
        print("Depolama bilgisi alınamadı.")

    # Sonsuz döngü ile programı açık tut
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()