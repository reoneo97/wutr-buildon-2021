FROM node:14-alpine

RUN mkdir -p /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app
COPY buildon/package*.json ./
RUN npm install
COPY buildon/ ./
RUN npm run build

EXPOSE 3000
ENV HOST=0.0.0.0
ENV PORT=3000
CMD ["npm","run","start"]

