# 🛠️ Guía de Instalación: VS Code + Python Extension Pack

> **Tarea obligatoria ANTES de la primera clase.**
> Tener listo tu entorno nos permitirá aprovechar al máximo cada minuto de la sesión en vivo.

---

## 💻 Paso 1: Descargar e Instalar Visual Studio Code (VS Code)

**Visual Studio Code** es el editor de código más popular y utilizado en el mundo de la programación.

1. Entra al sitio web oficial: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Haz clic en el botón azul de descarga correspondiente a tu sistema operativo:
   - 🪟 **Windows**: Descargar `.exe` (User Installer x64).
   - 🍎 **macOS**: Descargar `.zip` (Universal o Apple Silicon / Intel).
   - 🐧 **Linux**: Descargar `.deb` (Debian/Ubuntu) o `.rpm` (Fedora/RHEL).
3. Ejecuta el archivo descargado y sigue el asistente de instalación (*Siguiente -> Siguiente -> Finalizar*).
   - 💡 **Recomendación en Windows:** Marcar las casillas que dicen *"Agregar 'Abrir con Code' al menú contextual de archivos y carpetas"* y *"Agregar a PATH"*.

---

## 🐍 Paso 2: Instalar la extensión "Python Extension Pack"

Dentro de VS Code instalaremos el paquete oficial de herramientas para trabajar cómodamente con Python:

1. Abre **Visual Studio Code**.
2. En la barra lateral izquierda, haz clic en el ícono de **Extensiones** (un ícono con 4 bloques/cuadrados) o presiona el atajo:
   - `Ctrl + Shift + X` (en Windows/Linux)
   - `Cmd + Shift + X` (en macOS)
3. En el buscador escribe: `Python Extension Pack`.
4. Selecciona la extensión publicada por **Don Jayamanne** (o la suite oficial de **Microsoft** que la integra).
5. Haz clic en el botón azul **Install**.

---

## 🔍 Paso 3: Verificar que Python esté instalado en tu sistema

1. Abre una terminal dentro de VS Code:
   - Menú superior -> `Terminal` -> `New Terminal` (o presiona ``Ctrl + ` ``).
2. Escribe el siguiente comando y presiona `Enter`:
   ```bash
   python --version
   ```
   *(Si estás en Mac/Linux y no funciona, prueba con `python3 --version`)*.
3. Si ves algo como `Python 3.x.x`, ¡todo está perfecto!
4. Si sale un error de "comando no encontrado", descarga Python desde [python.org](https://www.python.org/downloads/) asegurándote de marcar la casilla **"Add Python to PATH"** durante la instalación.

---

## ✅ Checklist de verificación

- [ ] VS Code abre correctamente.
- [ ] La extensión Python está instalada y habilitada.
- [ ] La terminal reconoce el comando `python` o `python3`.

Si tienes algún inconveniente en este proceso, consúltalo en el grupo de WhatsApp/Telegram para apoyarte de inmediato.
