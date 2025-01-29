const express = require('express');
const path = require('path');

const app = express();
const port = 5000;

// Раздача статических файлов
app.use(express.static(path.join(__dirname, 'ton-chess-project')));

// Основной маршрут
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'ton-chess-project', 'index.html'));
});

// Запуск сервера
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
