import os

# Evita corrupción gráfica de WebKitGTK en algunas Raspberry Pi.
# Debe configurarse antes de importar pywebview.
os.environ.setdefault("WEBKIT_DISABLE_COMPOSITING_MODE", "1")

import webview


class Api:
    def salir(self):
        """Cierra la ventana principal desde el botón de la interfaz."""
        window.destroy()


HTML = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hola mundo</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      font-family: system-ui, sans-serif;
      color: #f8fafc;
      background: linear-gradient(135deg, #0f172a, #1d4ed8);
    }
    main { text-align: center; padding: 2rem; }
    h1 { margin: 0 0 1.5rem; font-size: clamp(2.5rem, 10vw, 5rem); }
    button {
      padding: .8rem 2rem;
      border: 0;
      border-radius: .75rem;
      font: inherit;
      font-weight: 700;
      color: #1e3a8a;
      background: #fff;
      cursor: pointer;
      box-shadow: 0 .5rem 1.5rem #0004;
    }
    button:hover { background: #dbeafe; }
    button:active { transform: translateY(1px); }
  </style>
</head>
<body>
  <main>
    <h1>Hola mundo</h1>
    <button type="button" onclick="pywebview.api.salir()">Salir</button>
  </main>
</body>
</html>
"""


if __name__ == "__main__":
    api = Api()
    window = webview.create_window(
        "Hola mundo",
        html=HTML,
        js_api=api,
        width=800,
        height=480,
    )
    webview.start()
