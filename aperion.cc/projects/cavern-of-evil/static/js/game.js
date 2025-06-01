
document.addEventListener('DOMContentLoaded', () => {
    const consoleDiv = document.getElementById('game-console');
    const input = document.getElementById('command-input');

    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const command = input.value;
            input.value = '';
            fetch('/api/command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command })
            })
            .then(res => res.json())
            .then(data => {
                consoleDiv.innerHTML += `<div>> ${command}</div><div>${data.response}</div>`;
                consoleDiv.scrollTop = consoleDiv.scrollHeight;
            });
        }
    });
});
