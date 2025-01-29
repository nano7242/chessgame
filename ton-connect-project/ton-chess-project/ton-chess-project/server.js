const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Статическая папка для обслуживании HTML и JS файлов
app.use(express.static(path.join(__dirname, 'ton-chess-project')));

// Главная страница
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'ton-chess-project', 'index.html'));
});

app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});

