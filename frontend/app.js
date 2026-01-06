const API = "http://127.0.0.1:5000";

function login() {
  fetch(API + "/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      username: document.getElementById("username").value,
      password: document.getElementById("password").value
    })
  })
  .then(r => r.json())
  .then(d => {
    if (d.token) {
      localStorage.setItem("token", d.token);
      window.location = "dashboard.html";
    } else {
      document.getElementById("error").innerText = "Login failed";
    }
  });
}

function loadAssets() {
  fetch(API + "/assets", {
    headers: {"Authorization": localStorage.getItem("token")}
  })
  .then(r => r.json())
  .then(data => {
    const table = document.getElementById("assetTable");
    table.innerHTML = "";
    data.forEach(a => {
      table.innerHTML += `
        <tr>
          <td>${a.asset_id}</td>
          <td>${a.name}</td>
          <td>${a.type}</td>
          <td>${a.owner}</td>
          <td>${a.status}</td>
        </tr>`;
    });
  });
}

function createAsset() {
  fetch(API + "/assets", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": localStorage.getItem("token")
    },
    body: JSON.stringify({
      name: document.getElementById("name").value,
      type: document.getElementById("type").value,
      owner: document.getElementById("owner").value
    })
  })
  .then(() => loadAssets());
}
