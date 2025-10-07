import express from 'express';
import { Sequelize, Model, CreationOptional }  from 'sequelize';

const port: number = 8888;
const DB_URL: string = process.env.DATABASE_URL || '';

const app: express.Application = express();
const sequelize = new Sequelize(DB_URL);


class FooBar extends Model {
  declare id: CreationOptional<number>;
  declare foo: string;
  declare bar: number
}

app.get("/", async (_, resp) => {
  resp.writeHead(200);
});

app.post("/create", async (req, resp) => {
  try {
    const foobar = await FooBar.create(req.body);
    resp.status(200).json(foobar)
  } catch (error) {
    resp.status(500).json({ error: `failed to create foobar` })
  }
});

app.get("/read/:id", async (req, resp) => {
  try {
    const foobar = await FooBar.findByPk(req.params.id);
    resp.status(200).json(foobar)
  } catch (error) {
    resp.status(500).json({ error: `failed to read foobar` })
  }
});

app.put("/update/:id", async (req, resp) => {
  try {
    const foobar = await FooBar.findByPk(req.params.id);
    await foobar?.update(req.body)
    resp.status(200).json(foobar)
  } catch (error) {
    resp.status(500).json({ error: `failed to read foobar` })
  }
});

app.delete("/delete/:id", async (req, resp) => {
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
