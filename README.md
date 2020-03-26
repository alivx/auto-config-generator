### auto configuration generator

This repo will including multi-service such as (Jenkins pipeline, Haproxy, Nginx) configuration, for now, I included Nginx only and later I will be including the rest service.

This script based on Jinja2 and python and template file in order to generate the config file.

## To do
1. Add advance nginx config such a caching, security...
2. Add Haproxy config
3. Add Jenkins Pipeline.
4. Dockerize new config as a docker image.
5. Add web interface.

### Usesages:

A. Change the nginx config parameters in `config/nginx_conf.json`
```json
[
    {
        "domain_name": "alivx.com", // server name
        "isADefaultDomain": true, // if this domain is the main one in the server
        "ssl_certificate": "/etc/nginx/ssl/cert.pem", // SSl Cert
        "ssl_certificate_key": "/etc/nginx/ssl/key.pem", // SSL Key
        "access_log": "/var/log/nginx/$server_name.access.log", // Access log
        "error_log": "/var/log/nginx/$server_name.error.log", // Error Log
        "securityHeader": false, // if you want to include the extra securty header
        "backends": [ //Up stream server for the backend
            {
                "name": "api", // Upstream name 
                "host": "127.0.0.1", //backend host 
                "port": 8001, // backend port
                "protocol": "https", //protocol https/https..etc
                "urlLocation": "/" // local "/" or  "/api" for exm: alivx.com/api will redirect to this backend 
            },
            {
                "name": "orders",
                "host": "localhost",
                "port": 8002,
                "protocol": "http",
                "urlLocation": "/orders"
            },
            {
                "name": "doc",
                "host": "localhost",
                "port": 8003,
                "protocol": "http",
                "urlLocation": "/doc"
            }
        ]
    }
]
```
To generate an nginx config file.
`python nginx.py`

the output file will be inside:
`ConfigOutput/alivx.com.conf`
Note: File name based in the domain name in the config file