
# NetCrypt

## 🛠️ Funcionalidades
1. **Criptografia AES**: Os arquivos são criptografados usando o algoritmo AES-256 em modo CBC de forma recursiva entre os diretórios.
3. **Conexão Cliente-Servidor**: O cliente envia a chave AES e o IV ao servidor, que utiliza esses dados para criptografar os arquivos.

## Uso
### ⚙️ Configuração do NetCrypt
1. Execute o NetCrypt Pc Vítima.

```bash
python NetCrypt.py <diretório_alvo>
```
2. O servidor ficará aguardando uma conexão do cliente, recebendo a chave AES e o IV, e criptografando arquivos presentes em um diretório especificado.
---
### ⚙️ Configuração do Connect
1. O código cria as chaves AES e IV e envia para o NetCrypt.
2. Também é escrito no terminal as chaves utilizadas.

```bash
python connect.py <host> <porta>
```
---
## 📋 Requisitos
Certifique-se de que você tenha o Python 3.x instalado e as bibliotecas necessárias.
```bash
pip install -r requirements.txt
```
## ⚠️ Aviso

Este projeto é destinado apenas para fins educacionais ;).
