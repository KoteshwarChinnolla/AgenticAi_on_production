let selectedChatbot = "AI Assistant";

function selectChatbot(name) {
    selectedChatbot = name;
    alert("Selected: " + name);
}
let uname="";
function startChat() {
    const username = document.getElementById("username").value.trim();
    if (!username) {
        alert("Please enter your name.");
        return;
    }
    uname=username;

    document.getElementById("overlay").style.display = "none";
    document.querySelector(".container").classList.remove("hidden");

    // Display user's name at the top right
    let userNameDisplay = document.createElement("div");
    userNameDisplay.textContent = username;
    userNameDisplay.style.position = "absolute";
    userNameDisplay.style.top = "10px";
    userNameDisplay.style.right = "10px";
    userNameDisplay.style.background = "#2c3e50";
    userNameDisplay.style.color = "white";
    userNameDisplay.style.padding = "10px";
    userNameDisplay.style.borderRadius = "5px";
    userNameDisplay.style.fontSize = "14px";
    document.body.appendChild(userNameDisplay);
}

function sendMessage() {
    const inputField = document.getElementById("user-input");
    const message = inputField.value.trim();
    if (!message) return;

    const chatWindow = document.getElementById("chat-window");
    chatWindow.innerHTML += `<div style="text-align: right; margin: 10px;"><b>You:</b> ${message}</div>`;
    fetch("https://7us7agqoy0.execute-api.us-east-1.amazonaws.com/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify({
          message: message,
          name:uname
        }),
      })
      .then((response) => response.text())
      .then((data) => {
        console.log("Success:", data);
        setTimeout(() => {
            const botResponse = `<div style="text-align: left; margin: 10px;"><b>${selectedChatbot}:</b> <div style="background:#ddd; padding:20px; border-radius:10px;">${data}</div></div>`;
            chatWindow.innerHTML += botResponse;
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }, 1000);
      })

    // Simulated API response in HTML format
    // setTimeout(() => {
    //     const botResponse = `<div style="text-align: left; margin: 10px;"><b>${selectedChatbot}:</b> <div style="background:#ddd; padding:10px; border-radius:10px;">${data}</div></div>`;
    //     chatWindow.innerHTML += botResponse;
    //     chatWindow.scrollTop = chatWindow.scrollHeight;
    // }, 1000);

    inputField.value = "";
}
