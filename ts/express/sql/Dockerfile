FROM node:24-alpine

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
COPY tsconfig.json ./
RUN npm install

COPY app.ts .

RUN npm run build

EXPOSE 3000

CMD ["node", "build/app.js"]
