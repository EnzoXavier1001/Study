## Configurando dispositivo para emular
1. Ativar modo Desenvolvedor do celular;
2. Conectar via USB e ativar Modo Depuração USB;
4. Instalação SCRCPY
  - Linux: `sudo apt install scrcpy`;
  - MacOS: `brew install scrcpy`
6. Verificar se esta sendo reconhecido com o comando `adb devices -l`;
7. Iniciar aplicação mobile: `npx react-native start`;
8. Em outro terminal executar: `adc reverse tcp:8081 tcp:8081`

## Dispositivo Wireless
1. adb tcpip 5555
2. adb connect <ip_do_celular>:5555
