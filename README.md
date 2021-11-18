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
#### curl:
```
curl -X POST http://localhost:5000/search?query=jackson
```

#### windows powershell:
```
Invoke-WebRequest 'http://localhost:5000/search?query=hamill+ford' -Method 'POST
```
Query should be a space seperated set of query terms.