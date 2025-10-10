const express = require("express");
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize(process.env.DATABASE_URL)

const app = express();
const router = express.Router();
const port = 8000;

app.use(express.json())
app.use(express.urlencoded())

const Crudie = sequelize.define("crudie", {
	service_key: DataTypes.STRING,
	data: DataTypes.INTEGER,
}, {
	tableName: "crudie",
	createdAt: false,
	updatedAt: false,
})


router.use((err, req, res, next) => {
	console.log(req.method + " " + req.path + " " + req.body);
	console.log(err)
	next(res);
})


router.post("/create", async (req, res) => {
	const entry = await Crudie.create({ service_key: req.body.service_key, data: req.body.data })
	res.send(entry)
})


router.get("/read", async (req, res) => {
	const entry = await Crudie.findOne({ where: { service_key: req.query.service_key } })
	res.send(entry)
})


router.put("/update", async (req, res) => {
	const entry = await Crudie.update({ data: req.body.data }, { where: { service_key: req.body.service_key }, returning: true, plain: true })
	res.send(entry[1])
})


router.delete("/delete", async (req, res) => {
	const entry = await Crudie.findOne({ where: { service_key: req.query.service_key } })
	entry.destroy()
	res.send(entry)
})


app.use('/', router);

app.listen(port, async () => {
	console.log("Listening on port " + port)
})
