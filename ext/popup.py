// Obtener el resultado desde el almacenamiento local
chrome.storage.local.get('result', function(data) {
    const result = data.result;

    // Verificar que 'result' tiene valor
    if (!result) {
        alert('Error al obtener el resultado.');
        return;
    }

    // Mostrar la alerta con el resultado
    if (result === 'seguro') {
        alert('¡La página es segura!');
    } else if (result === 'no seguro') {
        alert('¡Cuidado! La página no es segura.');
    } else {
        alert('Error al analizar');
    }
});
