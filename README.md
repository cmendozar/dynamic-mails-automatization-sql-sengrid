# dynamic-mails-automatization-sql-sengrid
An application to send dynamics mails through sengrid using sql server to get the data costumers. WIP: automatization. 


### Explicación del proyecto. 

La idea fue crear un servicio que permita enviar de manera automatizadamente mails dinamicos que puedan ir variando sus variables dentro de este con el objetivo de poder realizar estrategias inteligente de email marketing. Incluyendo la integración con una base de datos relacional. 


### Recursos Utilizados: 

- Python 3.8.0 
- Sengrid: API Sengrid. Para el envío de Emails.
- SQL SERVER para las bases de datos. 
- HTML para los emails. 

### Archivos. 

```python
+src
|_+data
  |_+queries
    |_query.sql
  |_sql.py
|_+templates
  |_example.html
|_+utils
  |_sender.py
  |_preprocessing.py
|_main.py
```

El servicio esta en una directorio source (src) donde este esta dividido en 3 secciones:
- Data: Aquí esta un archivo sql.py donde se crea una clase con SQL server para realizar las conexiones y queries necesarias. Dentro de la carpeta queries se encuentran los archivos .sql con las queries del proyecto. 

- Templates: Aqui es para incluir los archivos .html que se enviaran como correos. 

- Utils: El archivo principal del proyecto se llama sender.py donde esta configurado la API de SENGRID que nos permitirá enviar los mails y ser llamado para ir enviando los mails. Existe otro archivo preprocessing.py donde vamos colocando las funciones necesarias para preprocessar la información para que sea más limpia a la hora de meterlas en los templates. Usualmente en las bases de datos estan los nombres con mayusculas o minusculas u otra información pertinente. También incluí la idea de un call tu action que permita llevar a la persona a un link. Aquí esta función es totalmente personalizable. Sin embargo recomiendo usar un link utm con el fin de rastrear despues estas campañas a través de google analytics. 

- Un archivo Main.py: Tiene la lógica de personalización de envía de mails. 
