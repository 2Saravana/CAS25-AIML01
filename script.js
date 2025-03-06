document.addEventListener("DOMContentLoaded", function () {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        // Display user message
        chatBox.innerHTML += `<p class="user-message">${message}</p>`;
        userInput.value = "";

        // Send message to Flask API
        fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            if (data.response) {
                chatBox.innerHTML += `<p class="bot-message">${data.response}</p>`;
            } else {
                chatBox.innerHTML += `<p class="bot-message">Error: Could not get response.</p>`;
            }
        })
        .catch(error => {
            console.error("Error:", error);
            chatBox.innerHTML += `<p class="bot-message">Error: ${error.message}</p>`;
        });
    }
});
