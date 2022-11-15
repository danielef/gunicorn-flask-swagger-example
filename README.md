# gunicorn-flask-swagger-example

## Downloads
```
git clone https://github.com/danielef/gunicorn-flask-swagger-example.git
```

## Development
First, create a virtual environment as follows:
```
cd gunicorn-flask-swagger-example
virtualenv -p python3.7 env
source env/bin/activate
```

Then, install using `pip`:
```
pip install .
```

And run it with:
```
gsfe
```

Display all the options with `-h`:
```
$ gfse -h
usage: gfse [-h] [-b HOST] [-p PORT] [-v] [-r]

optional arguments:
  -h, --help            show this help message and exit
  -b HOST, --host HOST  APIn Host
  -p PORT, --port PORT  API Port
  -v, --verbose         API debug
  -r, --use-reloader    API use reloader
 ```
 
 ## Running with gunicorn
 
 ```
 gunicorn -w 4 gfse.app:app
 ```
 
