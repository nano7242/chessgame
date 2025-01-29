import { TonConnectUI } from '@tonconnect/ui';

const tonConnectUI = new TonConnectUI({
    manifestUrl: 'https://yourdomain.com/tonconnect-manifest.json'
});

// Инициализация кнопки
tonConnectUI.uiOptions = {
    language: 'en',
    uiPreferences: {
        theme: 'DARK'
    }
};

tonConnectUI.renderButton(document.getElementById('auth-button'), {
    size: 'small',
    cornerRadius: 8
});

// Проверка подключения
tonConnectUI.connectionRestored.then(() => {
    console.log('Connection restored');
});

export async function getWalletAddress() {
    return tonConnectUI.account?.address;
}
