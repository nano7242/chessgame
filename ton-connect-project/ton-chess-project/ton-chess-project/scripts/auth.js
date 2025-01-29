document.getElementById('connectButton').addEventListener('click', async () => {
    try {
        // Инициализация TON Connect
        const tonConnect = new TonConnectUI({
            dAppMetadata: {
                name: 'TON Chess Game',
                url: 'http://localhost:3000',
            },
        });

        // Ожидание подключения
        await tonConnect.connect();

        // Получение адреса пользователя
        const userAddress = await tonConnect.getAddress();
        console.log('Подключено! Адрес пользователя:', userAddress);

        alert('Подключено! Адрес пользователя: ' + userAddress);
    } catch (error) {
        console.error('Ошибка подключения:', error);
        alert('Произошла ошибка при подключении.');
    }
});
