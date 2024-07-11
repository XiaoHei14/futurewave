document.getElementById('wol-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const mac = document.getElementById('mac').value;
    const ip = document.getElementById('ip').value;

    const response = await fetch('/wake', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ mac, ip })
    });

    const result = await response.json();
    alert(result.message);
});
