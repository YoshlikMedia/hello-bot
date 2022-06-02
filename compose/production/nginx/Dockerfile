#FROM nginx:latest
#RUN apt-get update && apt-get install -y procps
#RUN mkdir -p /home/app/staticfiles
#
#RUN mkdir -p /html && \
#    chmod 755 /html && \
#    touch /etc/nginx/conf.d/default.conf && \
#    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
#

#
FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="saharagate.com"

COPY ./compose/production/nginx/default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./compose/production/nginx/uwsgi_params /etc/nginx/uwsgi_params
COPY ./compose/production/nginx/run.sh /run.sh

#ENV LISTEN_PORT=80
ENV LISTEN_PORT=8001
ENV APP_HOST=django
ENV APP_PORT=8001
#
USER root
#
RUN mkdir -p /html && \
    chmod 755 /html && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

#RUN mkdir -p /vol/static && \
#    chmod 755 /vol/static && \
#    touch /etc/nginx/conf.d/default.conf && \
#    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
#    chmod +x /run.sh
#
##may need to remove this line
#VOLUME /vol/static
#
USER nginx
#
CMD ["/run.sh"]
