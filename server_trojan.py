import socket
import pyautogui

host = "localhost"
port = 12345

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket oluşturuldu")

    s.bind((host, port)) 
    print("socket {} nolu porta bağlandı".format(port))

    s.listen(5)      
    print("socket dinleniyor")
except socket.error as msg:
    print("Hata:",msg)

while True: 

   # Client ile bağlantı kurulursa 
   c, addr = s.accept()      
   print('Gelen bağlantı:', addr)

   # Bağlanan client tarafına hoşgeldin mesajı gönderelim.  
   mesaj = 'selam '
   mesaj = input("Bir komut yolla :")
   c.send(mesaj.encode('utf-8'))
   if mesaj == "mauseTo":
       pyautogui.moveTo(100, 150,duration=3)
       

   # Bağlantıyı sonlandıralım 
   #C.close
