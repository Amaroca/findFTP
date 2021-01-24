<!-- AUTO-GENERATED-CONTENT:START (STARTER) -->
<p align="center">
  <a href="https://www.faciltech.info">
    <img alt="faciltech" src="https://yt3.ggpht.com/ytc/AAUvwng4KJs5t62nl2AvqDVOuXepKCSZp-l9_AQlsKBbwg=s176-c-k-c0x00ffffff-no-rj-mo" width="160" />
  </a>
</p>
<h1 align="center">
  findFTP - Descobrindo password de servidor FTP
</h1>

A ideia nesse script simples é utilizando uma wordlist simples composta de senhas, fazer uma brute force apartir de um usuário setado.
## 🚀 Wordlist

1.  **Crie sua wordlist ou mesmo baixe ela nos seguintes sites:.**
   <ul>
    <li><a href="https://github.com/berzerk0/Probable-Wordlists/tree/master/Real-Passwords">Bezer</a></li>
    <li><a href="https://github.com/jeanphorn/wordlist">Jeanphorn</a></li>
    <li><a href="https://github.com/Screetsec/Wordlist-Dracos">Screetsec</a></li>
    <li><a href="https://github.com/en-wl/wordlist">En-wl</a></li>
    <li><a href="https://github.com/kennyn510/wpa2-wordlists">Kennyn510</a></li>
  </ul>
1.  **Como instalar?**

    Navegue dentro de seu sistema, escolha o local e execute no terminal o comando abaixo.

    ``` git clone https://github.com/faciltech/findFTP.git
        Cloning into 'findFTP'...
        remote: Enumerating objects: 10, done.
        remote: Counting objects: 100% (10/10), done.
        remote: Compressing objects: 100% (10/10), done.
        remote: Total 10 (delta 1), reused 0 (delta 0), pack-reused 0
        Receiving objects: 100% (10/10), 19.14 KiB | 612.00 KiB/s, done.
        Resolving deltas: 100% (1/1), done.
      ```

2.  **Conceda permissão para o arquivo!**
```
chmod +x findFTP.py
```

## 🧐 Como usar o script?

Você irá digitar ```./findFTP.py``` 
   ```
        _________   ____________  ____________________  __
       / ____/   | / ____/  _/ / /_  __/ ____/ ____/ / / /
      / /_  / /| |/ /    / // /   / / / __/ / /   / /_/ /
     / __/ / ___ / /____/ // /___/ / / /___/ /___/ __  /
    /_/   /_/  |_\____/___/_____/_/ /_____/\____/_/ /_/
    Autor: Eduardo Amaral - eduardo4maral@protonmail.com
    You Tube : https://www.youtube.com/faciltech
    github   : https://github.com/faciltech
    Facebook : https://www.facebook.com/faciltech123

    Use python findFTP.py 127.0.0.1 usuario
  ```

1. Caso não seja setado um alvo, ou seja um ip/dominio, será apresentado a mensagem acima, indicando o modo padrão de uso.

2.  É necessário fazer uso de um domino/IP e um usuário

3.  Dessa forma será testado uma wordlist padrão com varias senhas.

4.  Quando encontrar a senha, será mostrado na tela senha encontrada.

## 🎓 Linguagem

O utilitário é desenvolvido em linguagem python, fazendo uso de poucas bibliotecas, e fazendo uso de SOCK, sendo assim, causa menos ruídos que outras ferramentas.

<!-- AUTO-GENERATED-CONTENT:END -->


