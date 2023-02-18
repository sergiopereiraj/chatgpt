# ChatGPT: local y/o dockerizado

Este repositorio contiene el código para utilizar chatgpt de modo local en tu terminal.
Ademas, si quieres ir un paso mas allá, este se encuentra Dockerizado, con la idea que puedas usarlo desde un contenedor.

### Para su uso debes tener cuenta en openai, y obtener key

### Modo local debes

1. Tener instalado Python
2. Clonar este repositorio
3. Asegurarte de tener instalado el gestor pip (python)
4. En tu terminal ejecutar (si estas desde windowns):
```
pip install openai
```
5. Des comenta la línea 4 y agrega tu key entre “”. 
6. Comenta con # línea 5 
7. En la terminal, desde la carpeta que contenga este proyecto ejecutar:
```
python chatgpt.py
```
7. Interactúa desde tu terminal con el chatgpt

### Modo Dockerizado:

1. Debes tener instalado Docker Desktop.
2. Clonar este repositorio
3. Desde la terminal, en la carpeta del proyecto ejecutar
```
docker build -t chatgpt .
```
Esto creara la imagen del proyecto
4. En su Docker desktop aplicar “run” a su imagen, colocar en variable de entorno:
###### variable: “OPENAI_API_KEY”, value : “you key”(obtenida desde pagina)
5. Desde la terminal de tu contenedor ejecuta:
```
python chatgpt.py
```
6. Interactúa con tu terminal
