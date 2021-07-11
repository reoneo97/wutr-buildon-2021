FROM node:alpine as build-stage
WORKDIR /app
COPY build-on/package*.json ./
RUN npm install
COPY build-on/ .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]