# Asyncio Examples
This is an exaple comparing Django and Sanic.

This example include this docker containers:

* Django  # Example Django project
* Sanic  # Example Sanic project
* Redis
* Postgres  # Shared database

## Performance Testing
First run `docker-compose up` to run this example.

Next, To run performance test I used **wrk**.

**Download WRK**
```bash
docker pull williamyeh/wrk
```

**Django Tests:**
```bash
docker run --rm williamyeh/wrk -t2 -c10 -d60s --timeout 2s http://{IP}:8080/
```
Results:
```
Running 1m test @ http://{IP}:8080/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    40.01ms   10.41ms 121.69ms   75.21%
    Req/Sec   113.86     16.27   171.00     76.17%
  13620 requests in 1.00m, 2.39MB read
  Socket errors: connect 0, read 13620, write 0, timeout 0
Requests/sec:    226.76
Transfer/sec:     40.75KB
```

**Sanic Tests:**
```bash
docker run --rm williamyeh/wrk -t2 -c10 -d60s --timeout 2s http://{IP}:8081/
```
Results:
```
Running 1m test @ http://192.168.10.107:8081/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    22.59ms    9.55ms  94.57ms   70.50%
    Req/Sec   224.05     28.25   383.00     73.89%
  26796 requests in 1.00m, 3.07MB read
Requests/sec:    445.94
Transfer/sec:     52.26KB
```

**WRK Usage**
```
docker run --rm williamyeh/wrk -t2 -c5 -d5s --timeout 2s http://{IP}:{PORT}/
Usage: wrk <options> <url>
  Options:
    -c, --connections <N>  Connections to keep open
    -d, --duration    <T>  Duration of test
    -t, --threads     <N>  Number of threads to use

    -s, --script      <S>  Load Lua script file
    -H, --header      <H>  Add header to request
        --latency          Print latency statistics
        --timeout     <T>  Socket/request timeout
    -v, --version          Print version details
```
