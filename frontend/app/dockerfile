FROM node:22 as front 

WORKDIR /app

COPY app/ /app/

RUN npm install && npm run build

FROM nginx 

COPY --from=front /app/dist/ /usr/share/nginx/html/