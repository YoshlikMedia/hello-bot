server {
    listen ${LISTEN_PORT};
    client_max_body_size    14M;
    root /etc/nginx/html;

#    location /html {
#        alias /etc/nginx/html;
#    }

    location /django {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
#        client_max_body_size    14M;
    }
}
