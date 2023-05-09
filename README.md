# Docker Container to run Selenium-Python (Demo)

**URL to connect with selenium server should contain the conatiner host name**

So, we have to change **`http://localhost:4444/wd/hub`** to **`http://chrome:4444/wd/hub`** --> chrome = container host name

```docker-compose
services:
    chrome:
        image: selenium/standalone-chrome:latest
        hostname: chrome
        container_name: chrome
        privileged: true
        shm_size: 2g
        healthcheck:
            test: curl -f http://localhost:4444
```

## Useful Resources:
- [Selenium Standalone Chrome Docker Image](https://hub.docker.com/r/selenium/standalone-chrome)
- [docker-compose depends_on with condition](https://stackoverflow.com/questions/47710767/what-is-the-alternative-to-condition-form-of-depends-on-in-docker-compose-versio)
