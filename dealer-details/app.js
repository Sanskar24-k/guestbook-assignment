const express = require('express');
const cors = require('cors');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

const dealers = JSON.parse(fs.readFileSync('./dealers.json', 'utf-8'));

app.get('/health', (req, res) => {
  res.json({
    status: 'UP',
    service: 'Dealer Details Microservice',
    version: '1.0.0',
    dealers_count: dealers.length
  });
});

app.get('/dealers', (req, res) => {
  res.json(dealers);
});

app.get('/dealers/:id', (req, res) => {
  const dealer = dealers.find(d => d.id === parseInt(req.params.id));
  if (dealer) {
    res.json(dealer);
  } else {
    res.status(404).json({ error: 'Dealer not found' });
  }
});

app.listen(PORT, () => {
  console.log(`Dealer Details Microservice running on port ${PORT}`);
});
