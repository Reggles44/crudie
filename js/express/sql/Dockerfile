FROM node:alpine as base

WORKDIR /app

COPY package.json ./
RUN rm -rf node_modules && npm install

COPY . .


FROM base as develop

CMD ["node", "./app.js"]
