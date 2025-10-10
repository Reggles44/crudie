import express, { Request, Response } from 'express';
import { Sequelize, Model, CreationOptional, DataTypes } from 'sequelize';

const port: number = 8888;
const DB_URL: string = process.env.DATABASE_URL || '';

const app: express.Application = express();
const sequelize = new Sequelize(DB_URL);


app.use(express.json());


class FooBar extends Model {
  declare id: CreationOptional<number>;
  declare foo: string;
  declare bar: number
}

FooBar.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    foo: { type: DataTypes.STRING },
    bar: { type: DataTypes.INTEGER },
  },
  { sequelize },
)

interface FooBarSchema {
  foo: string
  bar: number
}

app.get("/", async (_, resp) => {
  console.log("GET /")
  resp.writeHead(200);
  resp.send()
});

app.post("/create", async (req: Request<{}, {}, FooBarSchema>, resp: Response) => {
  console.log("POST /create", req.body)

  try {
    const foobar = await FooBar.create({ foo: req.body.foo, bar: req.body.bar });
    // const foobar = await FooBar.create(req.body);
    resp.status(200).json(foobar).send()
  } catch (error) {
    console.error('An error occurred:', (error as Error).message);
    resp.status(500).json({ error: `failed to create foobar` }).send()
  }
});

app.get("/read/:id", async (req: Request, resp: Response) => {
  console.log(`GET /read/${req.params.id}`)

  try {
    const foobar = await FooBar.findByPk(req.params.id);
    resp.status(200).json(foobar)
  } catch (error) {
    resp.status(500).json({ error: `failed to read foobar` })
  }
});

app.patch("/update/:id", async (req: Request<{id: string}, {}, FooBarSchema>, resp: Response) => {
  console.log(`PATCH /update/${req.params.id}`)

  try {
    const foobar = await FooBar.findByPk(req.params.id);
    await foobar?.update(req.body)
    resp.status(200).json(foobar)
  } catch (error) {
    resp.status(500).json({ error: `failed to read foobar` })
  }
});

app.delete("/delete/:id", async (req, resp) => {
  console.log(`DELETE /delete/${req.params.id}`)

  try {
    const foobar = await FooBar.findByPk(req.params.id);
    await foobar?.destroy(req.body)
    resp.status(200).json(foobar)
  } catch (error) {
    resp.status(500).json({ error: `failed to read foobar` })
  }
});

app.listen(port, async () => {
  try {
    await sequelize.authenticate();
    await sequelize.sync();
    console.log('Database connection has been established successfully.');
    console.log(`Server is running on port ${port}`);
  } catch (error) {
    console.error('Unable to connect to the database:', error);
  }
});
