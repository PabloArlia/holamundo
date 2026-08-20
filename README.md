# Hola mundo para Raspberry Pi

Aplicación Python de escritorio que usa un WebView y muestra un botón para cerrar la ventana.

## Instalación en Raspberry Pi OS

```bash
sudo apt update
sudo apt install -y python3-venv python3-gi gir1.2-webkit2-4.1
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Si tu versión de Raspberry Pi OS no encuentra `gir1.2-webkit2-4.1`, instala
`gir1.2-webkit2-4.0` en su lugar.

## Ejecutar

```bash
source .venv/bin/activate
python app.py
```
