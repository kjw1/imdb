# IMDB Crawler API

## Run
To host the api, build and run the docker container. Building the image runs the web crawler.
### Build Docker Image
```
docker build -t imdb:latest .
```

### Run Docker
```
docker run -it -p 5000:5000 imdb:latest
```

### Querying
#### curl:
```
curl -X POST http://localhost:5000/search?query=jackson
```

#### windows powershell:
```
Invoke-WebRequest 'http://localhost:5000/search?query=hamill+ford' -Method 'POST
```
Query should be a space seperated set of query terms.

## Dev instructions
1. Install requirements with `pip install -r requirements.txt`
### Crawler
1. Go to the movies directory `cd movies`
1. Run `scrapy crawl imdb` to build `items.json`

### Api
1. Run `python api.py`