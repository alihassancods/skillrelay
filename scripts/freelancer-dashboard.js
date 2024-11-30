const notificationCount1 = document.querySelector(".inbox-btn .notification-count");
  const notificationCount2 = document.querySelector(".notification-btn .notification-count");
  
  // Example: Dynamic notification updates
  let count = 99;
  setInterval(() => {
    count++;
    const newCount = count > 99 ? "99+" : count;
    notificationCount1.textContent = newCount;
    notificationCount2.textContent = newCount;
  }, 5000); // Update every 5 seconds