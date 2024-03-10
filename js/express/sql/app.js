const express = require("express");
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize("sqlite::memory:")

const app = express();
const router = express.Router();
const port = 8000;


const Crudie = sequelize.define("Crudie", {
	service_key: DataTypes.STRING,
	data: DataTypes.INTEGER,
})


router.use((req, res, next) => {
	console.log(req.method + " " + req.path + " " + req.body);
	next(res);
})


router.post("/create", (req, res) => {
	data = req.body
	const data = Crudie.create({
		service_key: req.body.service_key,
		data: req.body.data,
	})

	res.send(data)
})


app.use('/', router);

app.listen(port, () => {
	console.log("Listening on port " + port)
})
