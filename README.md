# Mini aplicación que se conecta a AWS S3

El objetivo de esta pequeña aplicación es enviar archivos almacenados en la máquina local a un bucket en el servicio S3 de AWS, al mismo tiempo que permite descargar y visualizar los elementos almacenados.

# Requisitos

- Python 3
- dependencias (mirar archivo `requirements.txt`)

# Instalación

Se recomienda la utilización de un entorno virtual, puede ser creado dentro de la misma carpeta.

```
python -m venv venv
```

Luego se debe activar el entorno virtual e instalar las dependencias.
 
```
# activar
source venv/bin/activate para Unix
venv/Scripts/activate para Windows
```
```
# Luego de activar el ambiente virtual, hay que instalar las dependencias
pip install -r requirements.txt
```

El siguiente paso es generar el archivo que almacenará las llaves de acceso a aws. Este archivo debe llamarse `.env` y su contenido es el siguiente:
```
AWS_ACCESS_KEY_ID='PUT_HERE_YOUR_ACCESS_KEY'
AWS_SECRET_ACCESS_KEY='PUT_HERE_YOUR_SECRET_ACCESS_KEY'
```
`PUT_HERE_YOUR_ACCESS_KEY` y `PUT_HERE_YOUR_SECRET_ACCESS_KEY` se obtienen de un usuario de aws (https://console.aws.amazon.com/iam/home?#/users), sección 'Credenciales de seguridad'

 # Ejecutar programa

 Existen varios comandos. Aquí está la lista de comandos con su descripción:

 ### Comando upload_to_s3.py
```
python upload_to_s3.py ruta/a/archivo*.gz nombre_bucket
```
  Notar que la ruta al archivo puede ser un patrón, esto permite subir varios archivos a la vez.
  
 #### Ayuda
```
# consultar ayuda
python upload_to_s3.py --help

usage: upload_to_s3.py [-h] [--omit-filename-check] [--replace]
                       file [file ...] bucket

move document to S3 bucket

positional arguments:
  file                  data file path. It can be a pattern, e.g. /path/to/file or /path/to/file*.zip
  bucket                bucket name. Valid options are:

optional arguments:
  -h, --help            show this help message and exit
  --omit-filename-check It Accepts filenames with distinct format to YYYY-mm-dd.*
  --replace             It replaces file if exists in bucket, default behavior ask to user a confirmation
```

 ### Comando download_from_s3.py
```
python download_from_s3.py nombre_archivo nombre_bucket --destination-path /home/user
```
  El primer parámetro es el nombre del archivo a descargar, el segundo corresponde al nombre del bucket en que se 
  encuentra el archivo, y por último, existe un parámetro opcional que permite definir la ruta donde se guardará el 
  archivo, si es omitido el archivo será guardado en el `current working directory` (dado por `os.getcwd()`)

 #### Ayuda
```
# consultar ayuda
python download_from_s3.py --help
 
usage: download_from_s3.py [-h] [--destination-path DESTINATION_PATH]
                           filename [filename ...] bucket

download one or more objects from S3 bucket

positional arguments:
  filename              one or more filenames
  bucket                bucket name

optional arguments:
  -h, --help            show this help message and exit
  --destination-path DESTINATION_PATH
                        path where files will be saved, if it is not provided
                        we will use current path

```

 ### Comando list_objects.py
```
python list_objects.py nombre_bucket
```
El único parámetro que necesita este comando es el nombre del bucket del que quiera listar los objetos.

#### Ayuda
```
# consultar ayuda
python list_objects.py --help

usage: list_objects.py [-h] bucket

show list of elements

positional arguments:
  bucket

optional arguments:
  -h, --help  show this help message and exit
```