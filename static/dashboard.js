function formatBytes(bytes) {
    if (!bytes) return "0 B";

    const units = ["B", "KB", "MB", "GB", "TB"];
    let index = 0;
    let value = Number(bytes);

    while (value >= 1024 && index < units.length - 1) {
        value /= 1024;
        index++;
    }

    return `${value.toFixed(2)} ${units[index]}`;
}


function formatSpeed(bytes) {
    return `${formatBytes(bytes)}/s`;
}


function formatUptime(seconds) {
    const days = Math.floor(seconds / 86400);
    seconds %= 86400;

    const hours = Math.floor(seconds / 3600);
    seconds %= 3600;

    const minutes = Math.floor(seconds / 60);

    return `${days}d ${hours}h ${minutes}m`;
}


async function updateSystem() {
    const response = await fetch("/api/system");
    const data = await response.json();

    document.getElementById("cpu").textContent =
        `${data.cpu_percent}%`;

    document.getElementById("memory").textContent =
        `${data.memory_percent}%`;

    document.getElementById("disk").textContent =
        `${data.disk_percent}%`;

    document.getElementById("upload").textContent =
        formatSpeed(data.upload_speed);

    document.getElementById("download").textContent =
        formatSpeed(data.download_speed);

    document.getElementById("ip").textContent =
        data.local_ip;

    document.getElementById("hostname").textContent =
        data.hostname;

    document.getElementById("platform").textContent =
        data.platform;

    document.getElementById("cores").textContent =
        data.cpu_count;

    document.getElementById("uptime").textContent =
        formatUptime(data.uptime_seconds);

    document.getElementById("status").textContent =
        "Online";
}


async function updateProcesses() {
    const response = await fetch("/api/processes");
    const data = await response.json();

    const table = document.getElementById("processes");

    table.innerHTML = "";

    data.processes.forEach(process => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${process.pid}</td>
            <td>${process.name}</td>
            <td>${process.cpu_percent}%</td>
            <td>${process.memory_percent}%</td>
        `;

        table.appendChild(row);
    });
}


async function updateConnections() {
    const response = await fetch("/api/network");
    const data = await response.json();

    const table = document.getElementById("connections");

    table.innerHTML = "";

    data.connections.forEach(connection => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${connection.local}</td>
            <td>${connection.remote}</td>
            <td>${connection.status}</td>
            <td>${connection.pid ?? "N/A"}</td>
        `;

        table.appendChild(row);
    });
}


async function refreshDashboard() {
    try {
        await Promise.all([
            updateSystem(),
            updateProcesses(),
            updateConnections()
        ]);
    } catch (error) {
        document.getElementById("status").textContent =
            "Connection Error";

        console.error(error);
    }
}


refreshDashboard();

setInterval(refreshDashboard, 5000);
