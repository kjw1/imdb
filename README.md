# IMDB Crawler API

## Run

### Build Docker Image
```
docker build -t imdb:latest .
```

### Run Docker
```
docker run -it -p 5000:5000 imdb:latest
```

### Querying
```
curl -X POST http://localhost:5000/search?query=jackson
```
Query should be a space seperated set of query terms.