upstream app {
    server ${APP_HOST}:${APP_PORT};
}

server {
    listen ${LISTEN_PORT} ssl;
    http2 on;

    ssl_certificate /etc/nginx/certs/example.crt;
    ssl_certificate_key /etc/nginx/certs/example.key;

    location /static {
        alias /vol/static;
    }

    location /media {
        alias /vol/media;
    }

    location / {
        proxy_pass http://app;
        include /etc/nginx/proxy_params;
        http2_push_preload on;
    }
}