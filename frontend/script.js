const sidebar = document.querySelector("#sidebar");
const hide_sidebar = document.querySelector(".hide-sidebar");
const new_chat_button = document.querySelector(".new-chat");

const scrollDiv = document.querySelector(".scroll-div");

hide_sidebar.addEventListener("click", function() {
    sidebar.classList.toggle("hidden");
});

const user_menu = document.querySelector(".user-menu ul");
const show_user_menu = document.querySelector(".user-menu button");

show_user_menu.addEventListener("click", function() {
    if (user_menu.classList.contains("show")) {
        user_menu.classList.toggle("show");
        setTimeout(function() {
            user_menu.classList.toggle("show-animate");
        }, 200);
    } else {
        user_menu.classList.toggle("show-animate");
        setTimeout(function() {
            user_menu.classList.toggle("show");
        }, 50);
    }
});

const models = document.querySelectorAll(".model-selector button");

for (const model of models) {
    model.addEventListener("click", function() {
        document.querySelector(".model-selector button.selected")?.classList.remove("selected");
        model.classList.add("selected");
    });
}

const message_box = document.querySelector("#message");

message_box.addEventListener("keyup", function() {
    message_box.style.height = "auto";
    let height = message_box.scrollHeight + 2;
    if (height > 200) {
        height = 200;
    }
    message_box.style.height = height + "px";
});

function show_view(view_selector) {
    document.querySelectorAll(".view").forEach(view => {
        view.style.display = "none";
    });

    document.querySelector(view_selector).style.display = "flex";
}
//
new_chat_button.addEventListener("click", function() {
    show_view(".new-chat-view");
});

document.querySelectorAll(".conversation-button").forEach(button => {
    button.addEventListener("click", function() {
        show_view(".conversation-view");
    });
});

function toggleDarkMode() {
    document.body.classList.remove("light-mode");
    document.body.classList.add("dark-mode");
}

function toggleLightMode() {
    document.body.classList.remove("dark-mode");
    document.body.classList.add("light-mode");
}

async function sendMessage() {
    const userInput = document.querySelector('#message');
    const message = userInput.value.trim();
    if (message === '') return;

    // Display user input in the bot-answer class
    displayMessage(message, 'user-message');

    // Clear the textarea and reset height
    userInput.value = '';
    userInput.style.height = 'auto';

    // Send message to server
    try {
        const response = await fetch('https://967a-102-89-23-100.ngrok-free.app/webhook', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        });

        if (response.ok) {
            const data = await response.json();
            displayMessage(data.response, 'bot-message');
        } else {
            console.error('Error:', response.statusText);
            displayMessage('Error: Could not reach the server.', 'bot-message');
        }
    } catch (error) {
        console.error('Error:', error);
        displayMessage('Error: Could not reach the server.', 'bot-message');
    }
}

document.querySelector('.send-button').addEventListener('click', sendMessage);

message_box.addEventListener("keyup", function(event) {
    message_box.style.height = "auto";
    let height = message_box.scrollHeight + 2;
    if (height > 200) {
        height = 200;
    }
    message_box.style.height = height + "px";

    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});

// Function to display welcome message
function displayWelcomeMessage() {
    displayMessage('Welcome to Python Teaching Bot, How can I help you today?', 'bot-message');
}

// Call displayWelcomeMessage when the page loads
document.addEventListener('DOMContentLoaded', displayWelcomeMessage);



// JavaScript to toggle dark mode
function toggleLightMode() {
    document.body.classList.remove("dark-mode");
    localStorage.setItem("theme", "light");
}

function toggleDarkMode() {
    document.body.classList.add("dark-mode");
    localStorage.setItem("theme", "dark");
}

// Apply the saved theme on page load
document.addEventListener("DOMContentLoaded", (event) => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
    } else {
        document.body.classList.remove("dark-mode");
    }
});

document.getElementById('refreshing').addEventListener('click', function() {
    window.location.reload();
});


function displayMessage(message, type, fontColor = 'white', borderRadius = '16px', fontSize = '18px', maxWidth = '60%', boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)') {
    const responseWrapper = document.querySelector('.response-wrapper');
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.style.color = fontColor;
    messageDiv.style.borderRadius = borderRadius;
    messageDiv.style.fontSize = fontSize;
    messageDiv.style.maxWidth = maxWidth;
    messageDiv.style.boxShadow = boxShadow;
    messageDiv.style.whiteSpace = 'pre-wrap';
    messageDiv.style.wordWrap = 'break-word';

    if (type === 'user-message') {
        messageDiv.classList.add('user-message');
    } else if (type === 'bot-message') {
        messageDiv.classList.add('bot-message');
    }

    responseWrapper.appendChild(messageDiv);

    // Scroll to the bottom
    const scrollDiv = document.querySelector('.scroll-div');
    scrollDiv.scrollTop = scrollDiv.scrollHeight;

    // If the scroll height exceeds the client height, adjust the scroll position
    if (scrollDiv.scrollHeight > scrollDiv.clientHeight) {
        scrollDiv.scrollTop = scrollDiv.scrollHeight - scrollDiv.clientHeight;
    }
}
