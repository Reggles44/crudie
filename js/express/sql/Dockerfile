FROM node:alpine as base

WORKDIR /app

COPY package.json ./
RUN rm -rf node_modules && npm install

COPY . .


FROM base as develop

EXPOSE 8000

CMD ["node", "./app.js"]
