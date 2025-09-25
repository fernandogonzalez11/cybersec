token = localStorage.getItem("userToken");
console.log("Loaded token:", token);

async function fetchWelcomeMessage(token) {
    try {
        const response = await fetch("/api/message", {
            method: "GET",
            headers: {
                "x-token": token
            }
        });

        const data = await response.json();

        if (response.ok) {
            const welcomeMessageDiv = document.getElementById("welcomeMessage");
            if (welcomeMessageDiv) {
                welcomeMessageDiv.innerText = data.message;
            }
        } else {
            alert("Failed to fetch welcome message.");
        }
    } catch (error) {
        console.error("Error fetching message:", error);
        alert("Error fetching message.");
    }
}

fetchWelcomeMessage(token);