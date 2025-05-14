Explicación del proceso:

1. Se creó un archivo llamado cookies_extractor.py, cuyo propósito es extraer cookies de los navegadores más populares: Microsoft Edge, Google Chrome y Mozilla Firefox. El proceso se realiza de forma silenciosa. Una vez extraídas, las cookies se envían automáticamente a través de un bot de Telegram, y luego se eliminan para no dejar rastros en el sistema.

2. El archivo cookies_extractor.py fue subido a un repositorio en GitHub. Dado que una computadora limpia (sin Python instalado) no puede ejecutar directamente archivos .py, se creó un archivo por lotes llamado AdminSilent.bat. Este archivo se ejecuta de forma silenciosa con privilegios de administrador y se encarga de instalar automáticamente las dependencias necesarias para ejecutar el script cookies_extractor.py directamente desde la web. Una vez ejecutado, el script se elimina del sistema para no dejar rastros. 

3. Finalmente el archivo .bat fue convertido a un ejecutable (Spotify.exe) que actúa como señuelo, camuflándose como una aplicación legítima. Al ejecutarse, inicia todo el proceso de forma inmediata.


Este método utiliza una técnica común en el análisis de malware, donde se disfraza el comportamiento malicioso dentro de una aplicación aparentemente legítima.

Nota importante: Esta herramienta fue desarrollada únicamente con fines educativos, para estudiar el comportamiento de las cookies, su importancia en la seguridad informática y los riesgos asociados. El uso indebido o con fines antiéticos es responsabilidad exclusiva del usuario. No se promueve ni se avala ninguna actividad ilegal o malintencionad

