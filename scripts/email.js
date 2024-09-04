const domains = [
    "1secmail.com",
    "1secmail.org",
    "1secmail.net",
    "vjuum.com",
    "laafd.com",
    "txcct.com",
    "rteet.com",
    "dpptd.com"
];

function getRandomEmail() {
    const username = Math.random().toString(36).substring(2, 10); // 8 character random string
    const domain = domains[Math.floor(Math.random() * domains.length)];
    return `${username}@${domain}`;
}

document.getElementById("generateBtn").addEventListener("click", function() {
    const emailList = document.getElementById("emailList");
    emailList.innerHTML = ""; // Clear previous list

    for (let i = 0; i < 10; i++) {
        const email = getRandomEmail();
        const listItem = document.createElement("li");
        listItem.textContent = email;
        emailList.appendChild(listItem);
    }
});
