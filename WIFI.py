import subprocess
import os
import sys

# Criar um arquivo
arquivo = open('senhas.txt', 'w')
arquivo.write("Seguem as senhas:\n\n")
arquivo.close()

# Criando listas
wifi_files = []
wifi_names = []
wifi_passwords = []

command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True)

# Pegar diretório atual
path = os.getcwd()

for file in os.listdir(path):
  if file.startswith("Wi-Fi") and file.endswith(".xml"):
    wifi_files.append(file)

print(wifi_files)

for i in wifi_files:
    senha_encontrada = False
    nome_encontrado = False
    with open(i, "r") as f:
        for line in f.readlines():
            if 'name' in line and not nome_encontrado:
                stripped = line.strip()
                # Remove os 6 primeiros caracteres
                front = stripped [6:]
                back = front[:-7]
                wifi_names.append(back)
                nome_encontrado = True
            
            if 'keyMaterial' in line:
                stripped = line.strip()
                # Remove os 13 primeiros caracteres
                front = stripped [13:]
                back = front[:-14]
                wifi_passwords.append(back)
                senha_encontrada = True
                print(senha_encontrada)

            #print(senha_encontrada)
        if not senha_encontrada and wifi_names:
            print(str(senha_encontrada))
            wifi_names.pop()

print(wifi_names)
print(wifi_passwords)

for x, y in zip(wifi_names, wifi_passwords):
    sys.stdout = open("senhas.txt", "a")
    print("Nome da rede: " + x + "\nSenha: " + y + "\n")
    sys.stdout.close()
