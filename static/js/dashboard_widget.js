// Calendar + Clock Widget
function updateCalendarClock() {
  const container = document.getElementById('calendar-clock-widget');
  if (!container) return;

  const now = new Date();
  const optionsDate = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  const dateStr = now.toLocaleDateString(undefined, optionsDate);
  const timeStr = now.toLocaleTimeString();

  container.innerHTML = `
    <div class="card p-3 shadow-sm">
      <div><strong>${dateStr}</strong></div>
      <div style="font-size: 1.5em; font-weight: bold;">${timeStr}</div>
    </div>
  `;
}

setInterval(updateCalendarClock, 1000);
updateCalendarClock();
