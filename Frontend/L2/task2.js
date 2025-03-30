async function fetchData(url) {
    const response = await fetch(url);

    if (!response.ok)
        throw new Error(`Failed to get data from ${url}`)

    return response.text()
}


// Working request
fetchData("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    .then(data => {
        console.log("Data:", data);
    })
    .catch(error => {
        console.error("Error:", error);
    });

// Wrong url
fetchData("https://api.example.com/data")
    .then(data => {
        console.log("Data:", data);
    })
    .catch(error => {
        console.error("Error:", error);
    });

// 403 response status
fetchData("https://api.openai.com/v1/chat/completions")
    .then(data => {
        console.log("Data:", data);
    })
    .catch(error => {
        console.error("Error:", error);
    });