FROM node:alpine as build-stage
WORKDIR /app
COPY buildon/package*.json ./
RUN npm install
COPY buildon/ .
RUN npm run generate

# production stage
FROM nginx:stable-alpine as production-stage
RUN rm /etc/nginx/conf.d/default.conf
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage ./app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]