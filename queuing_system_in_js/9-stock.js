import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Data
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Data access
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

// Redis client
const client = redis.createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Promisify Redis get
const getAsync = promisify(client.get).bind(client);

// Reserve stock by id
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

// Get current reserved stock by id
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

// Express server
const app = express();
const PORT = 1245;

// GET /list_products - return all products
app.get('/list_products', (req, res) => {
  const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(products);
});

// GET /list_products/:itemId - return product detail with current stock
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = reservedStock !== null
    ? product.stock - parseInt(reservedStock, 10)
    : product.stock;

  return res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

// GET /reserve_product/:itemId - reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentReserved = reservedStock !== null ? parseInt(reservedStock, 10) : 0;
  const availableStock = product.stock - currentReserved;

  if (availableStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  reserveStockById(itemId, currentReserved + 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
