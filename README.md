# K3ySpy

**K3ySpy** é um keylogger que permite a captura de teclas digitadas e do conteúdo da área de transferência (clipboard) e envia os dados capturados para um endereço IP configurado e salva arquivos localmente. Ele oferece três funcionalidades:

## 🛠️ Funcionalidades

### `rede`
**rede**: Envia as teclas capturadas diretamente para uma conexão de rede.
```bash
python k3yspy.py rede
```
---
### `local`
**local**: Salva as teclas e o conteúdo do clipboard localmente.

```bash
python k3yspy.py local
```
---
### `ambos`
**ambos**: Executa as capturas locais e envia as teclas pela rede e localmente.
```bash
python k3yspy.py ambos
```



## 📋 Requisitos
- Python 3.x
Instale as dependências usando o comando:
```bash
pip install -r requirements.txt
```

## ⚙️ Configurações
Você pode configurar o endereço IP, porta e os caminhos dos arquivos para salvar os logs de teclas e clipboard diretamente no código:

- **ip**: Defina o endereço IP do servidor que receberá as teclas.
- **porta**: Defina a porta do servidor.
- **arquivo_ctrl_c**: Defina o caminho do arquivo onde será salvo o conteúdo do clipboard.
- **arquivo_log**: Defina o caminho do arquivo onde será salvo o log das teclas.

---
## ⚠️ Aviso

Este projeto deve ser usado apenas para fins educacionais ;).
