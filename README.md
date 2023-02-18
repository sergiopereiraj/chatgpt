# chatgpt local y dockerizado

Este repositorio contiene el código para utilizar chatgpt de modo local en tu terminal.
Ademas, si quieres ir un paso mas allá, este se encuentra Dockerizado, con la idea que puedas usarlo desde un contenedor.

### Para su uso debes tener cuenta en openai, y obtener key

### Si lo usas de modo local debes

1. Clonar este repositorio
2.Tener instalado Python
3. Asegurarte de tener instalado el gestor pip
4. En tu terminal ejecutar (si estas desde windowns)
```
pip install openai
```
5. Des comenta la línea 4 y agrega tu key entre “”. Comenta con # línea 5 
6. En la terminal, desde la carpeta que contenga este proyecto ejecutar 
```
python chatgpt.py
```
7. Interactúa desde tu terminal con el chatgpt

### Para modo Dockerizado:

#### Debes tener instalado Docker Desktop.
1. Clonar este repositorio
2. Desde la terminal, en la carpeta del proyecto ejecutar
```
docker build -t chatgpt .
```
Esto creara la imagen del proyecto
3. En su Docker desktop aplicar “run” a su imagen, colocar en variable de entorno:
###### variable: “OPENAI_API_KEY”, value : “you key”(obtenida desde pagina)
4. Desde la terminal de tu contenedor ejecuta:
```
python chatgpt.py
```
5. Interactúa con tu terminal
