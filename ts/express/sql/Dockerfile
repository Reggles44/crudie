FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY app.ts .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
