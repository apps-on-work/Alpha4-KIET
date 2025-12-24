const eventsData = [
    {
        title: "Innotech",
        type: "hackathon",
        desc: "24-hour national level hackathon at the Auditorium.",
        date: "Jan 15, 2026",
        location: "Auditorium"
    },
    {
        title: "WebDev Bootcamp",
        type: "bootcamp",
        desc: "Master Next.js and Firebase in Lab 4.",
        date: "Jan 20, 2026",
        location: "Lab-4"
    },
    {
        title: "GDG Recruitment",
        type: "recruitment",
        desc: "First year students recruitment.",
        date: "Jan 22, 2026",
        location: "E-302"
    },
    {
        title: "AI Open Session",
        type: "open-session",
        desc: "Discussion on Gemini in the Conference Room.",
        date: "Oct 26, 2026",
        location: "Conference-Room"
    }
];

function displayEvents(filter = "all") {
    const grid = document.getElementById("eventsGrid");
    grid.innerHTML = "";

    const filtered = filter === "all" 
        ? eventsData 
        : eventsData.filter(e => e.type === filter);

    filtered.forEach(event => {
        const card = document.createElement("div");
        card.className = "event-card";
        card.innerHTML = `
            <div style="flex-grow: 1;">
                <span style="color: violet; font-size: 0.8rem; font-weight: bold; text-transform: uppercase;">${event.type}</span>
                <h3 style="margin: 10px 0;">${event.title}</h3>
                <p style="color: #bdbdbd; font-size: 0.9rem;">${event.desc}</p>
                <p style="font-size: 0.8rem; margin-top: 10px;">📅 ${event.date} | 📍 ${event.location}</p>
            </div>
            <div class="card-actions">
                <a href="map.html" class="btn-nav">Navigate</a>
                <a href="#" class="button btn-reg">Register</a>
            </div>
        `;
        grid.appendChild(card);
    });
}

function filterEvents(category) {
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
        if(btn.textContent.toLowerCase().includes(category.replace('-', ' '))) {
            btn.classList.add('active');
        } else if (category === 'all' && btn.textContent === 'All') {
            btn.classList.add('active');
        }
    });
    displayEvents(category);
}

window.addEventListener("DOMContentLoaded", () => displayEvents());

