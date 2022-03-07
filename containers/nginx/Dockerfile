FROM nginx

COPY --from=base /app/public /app/public

COPY containers/nginx/proxy.conf /etc/nginx/conf.d/default.conf

