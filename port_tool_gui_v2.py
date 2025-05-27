import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import socket
import threading
import queue
import datetime
import os

# --- Log kuyruğu oluştur
log_queue = queue.Queue()

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    log_queue.put(log_entry)

def update_log_area():
    while not log_queue.empty():
        msg = log_queue.get()
        log_area.configure(state='normal')
        log_area.insert(tk.END, msg + '\n')
        log_area.configure(state='disabled')
        log_area.yview(tk.END)
    root.after(500, update_log_area)

# --- Port Tarayıcı
def port_scanner(target_ip, start_port, end_port):
    log_message(f"Taramaya başlandı: {target_ip} ({start_port}-{end_port})")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    log_message(f"AÇIK PORT: {port}")
        except Exception as e:
            log_message(f"Hata: {e}")
    log_message("Port taraması tamamlandı.")

def run_port_scan():
    ip = entry_target_ip.get()
    try:
        start_port = int(entry_start_port.get())
        end_port = int(entry_end_port.get())
    except ValueError:
        messagebox.showerror("Hatalı Giriş", "Başlangıç ve bitiş portları sayı olmalıdır.")
        return

    threading.Thread(target=port_scanner, args=(ip, start_port, end_port), daemon=True).start()

# --- TCP Dinleyici
def tcp_listener(port):
    log_message(f"Port {port} üzerinde dinleniyor...")
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen(5)
        while True:
            client, addr = server.accept()
            data = client.recv(1024).decode('utf-8').strip()
            log_message(f"{addr[0]}:{addr[1]} -> {data}")
            save_to_logfile(addr, data)
            client.close()
    except Exception as e:
        log_message(f"Dinleme hatası: {e}")

def save_to_logfile(addr, data):
    os.makedirs("logs", exist_ok=True)
    log_file = os.path.join("logs", "listener_log.txt")
    with open(log_file, "a") as f:
        f.write(f"{datetime.datetime.now()} - {addr[0]}:{addr[1]} -> {data}\n")

def run_listener():
    try:
        port = int(entry_listen_port.get())
        threading.Thread(target=tcp_listener, args=(port,), daemon=True).start()
    except ValueError:
        messagebox.showerror("Hatalı Giriş", "Port değeri sayı olmalıdır.")

# --- Canlı Bağlantı Testi
def test_connection(ip, port):
    log_message(f"{ip}:{port} bağlantısı test ediliyor...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((ip, port))
            log_message(f"Bağlantı BAŞARILI -> {ip}:{port}")
    except Exception as e:
        log_message(f"Bağlantı BAŞARISIZ -> {ip}:{port} - {e}")

def run_connection_test():
    ip = entry_test_ip.get()
    try:
        port = int(entry_test_port.get())
        threading.Thread(target=test_connection, args=(ip, port), daemon=True).start()
    except ValueError:
        messagebox.showerror("Hatalı Giriş", "Port değeri sayı olmalıdır.")

# --- GUI Arayüz
root = tk.Tk()
root.iconbitmap("icon.ico")  # ← ikon buraya eklendi
root.title("Port Araçları - Tarayıcı | Dinleyici | Bağlantı Testi")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill='both', expand=True)

# Sekme 1: Port Tarayıcı
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="🔍 Port Tarayıcı")

tk.Label(tab1, text="Hedef IP:").grid(row=0, column=0, sticky="e")
entry_target_ip = tk.Entry(tab1)
entry_target_ip.insert(0, "127.0.0.1")
entry_target_ip.grid(row=0, column=1)

tk.Label(tab1, text="Başlangıç Port:").grid(row=1, column=0, sticky="e")
entry_start_port = tk.Entry(tab1)
entry_start_port.insert(0, "1")
entry_start_port.grid(row=1, column=1)

tk.Label(tab1, text="Bitiş Port:").grid(row=2, column=0, sticky="e")
entry_end_port = tk.Entry(tab1)
entry_end_port.insert(0, "1024")
entry_end_port.grid(row=2, column=1)

tk.Button(tab1, text="Taramayı Başlat", command=run_port_scan).grid(row=3, column=1, pady=10)

# Sekme 2: TCP Dinleyici
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="📡 TCP Dinleyici")

tk.Label(tab2, text="Dinlenecek Port:").grid(row=0, column=0, sticky="e")
entry_listen_port = tk.Entry(tab2)
entry_listen_port.insert(0, "9999")
entry_listen_port.grid(row=0, column=1)

tk.Button(tab2, text="Dinlemeyi Başlat", command=run_listener).grid(row=1, column=1, pady=10)

# Sekme 3: Bağlantı Testi
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="🔗 Bağlantı Testi")

tk.Label(tab3, text="Hedef IP:").grid(row=0, column=0, sticky="e")
entry_test_ip = tk.Entry(tab3)
entry_test_ip.insert(0, "127.0.0.1")
entry_test_ip.grid(row=0, column=1)

tk.Label(tab3, text="Port:").grid(row=1, column=0, sticky="e")
entry_test_port = tk.Entry(tab3)
entry_test_port.insert(0, "80")
entry_test_port.grid(row=1, column=1)

tk.Button(tab3, text="Bağlantı Testini Başlat", command=run_connection_test).grid(row=2, column=1, pady=10)

# Log Alanı
log_area = scrolledtext.ScrolledText(root, height=12, state='disabled')
log_area.pack(padx=10, pady=10, fill='both', expand=True)

update_log_area()
root.mainloop()
