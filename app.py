import os
from pathlib import Path

# Evita corrupción gráfica de WebKitGTK en algunas Raspberry Pi.
# Debe configurarse antes de importar pywebview.
os.environ.setdefault("WEBKIT_DISABLE_COMPOSITING_MODE", "1")

import webview


class Api:
    def salir(self):
        """Cierra la ventana principal desde el botón de la interfaz."""
        window.destroy()


if __name__ == "__main__":
    pagina = (Path(__file__).parent / "html" / "index.html").resolve().as_uri()
    api = Api()
    window = webview.create_window(
        "Hola mundo",
        url=pagina,
        js_api=api,
        fullscreen=True,
    )
    webview.start()
