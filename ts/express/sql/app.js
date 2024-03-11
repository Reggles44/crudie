"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const sequelize_1 = require("sequelize");
const app = (0, express_1.default)();
const router = express_1.default.Router();
const port = 8000;
app.use(express_1.default.json());
app.use(express_1.default.urlencoded());
const sequelize = new sequelize_1.Sequelize(process.env.DATABASE_URL);
const Crudie = sequelize.define("crudie", {
    service_key: sequelize_1.DataTypes.STRING,
    data: sequelize_1.DataTypes.INTEGER,
}, {
    tableName: "crudie",
    createdAt: false,
    updatedAt: false,
});
router.use((err, req, res, next) => {
    console.log(req.method + " " + req.path + " " + req.body);
    console.log(err);
    next(res);
});
router.post("/create", (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const entry = yield Crudie.create({
        service_key: req.body.service_key,
        data: req.body.data
    });
    res.send(entry);
}));
router.get("/read", (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const entry = yield Crudie.findOne({
        where: {
            service_key: req.query.service_key
        }
    });
    res.send(entry);
}));
router.put("/update", (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const entry = yield Crudie.update({
        data: req.body.data
    }, {
        where: {
            service_key: req.body.service_key
        }, returning: true
    });
    res.send(entry[1]);
}));
router.delete("/delete", (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const entry = yield Crudie.findOne({
        where: {
            service_key: req.query.service_key
        }
    });
    entry.destroy();
    res.send(entry);
}));
app.use('/', router);
app.listen(port, () => __awaiter(void 0, void 0, void 0, function* () {
    console.log("Listening on port " + port);
}));
