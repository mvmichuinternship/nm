// script.js
const checkButton = document.getElementById('check-button');
const resultContainer = document.getElementById('result-container');

checkButton.addEventListener('click', async () => {
    const inputText = document.getElementById('input-text').value;

    // Make an HTTP POST request to the Paraphrase Genius API
    const url = 'https://paraphrase-genius.p.rapidapi.com/dev/paraphrase/';
    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-RapidAPI-Key': 'e8e41140e7msh5c7ba67e4cdf74ap1b600bjsn635b84099fab',
            'X-RapidAPI-Host': 'paraphrase-genius.p.rapidapi.com'
        },
        body: JSON.stringify({
            text: inputText,
            result_type: 'multiple'
        })
    };
    
    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error('Request failed with status ' + response.status);
        }
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
});

