# FROM nginx:alpine

# COPY ./start.sh /start.sh

# RUN chmod +x /start.sh && \
# 	touch /etc/nginx/conf.d/default.conf 

# COPY ./proxy_params /etc/nginx/
# COPY ./default.conf.tpl /etc/nginx/

# ENTRYPOINT [ "sh", "-c", "/start.sh" ]
FROM alpine:latest AS openssl

RUN apk --no-cache add --update openssl

WORKDIR /tmp

RUN openssl req \
  -x509 \
  -nodes \
  -days 365 \
  -newkey rsa:2048 \
  -subj "/C=/ST=/L=/O=/CN=demo" \
  -keyout example.key \
  -out example.crt

FROM nginx:alpine

WORKDIR /etc/nginx

RUN mkdir certs

COPY --from=openssl /tmp/example.* /etc/nginx/certs/
COPY ./start.sh /start.sh
COPY ./proxy_params /etc/nginx/
COPY ./default.conf.tpl /etc/nginx/

RUN chmod +x /start.sh && \
	touch /etc/nginx/conf.d/default.conf

ENTRYPOINT [ "sh", "-c", "/start.sh" ]