function runConfetti() {
  const duration = 2000; // longer duration (8 seconds)
  const animationEnd = Date.now() + duration;
  const defaults = {
    startVelocity: 40,
    spread: 360,
    ticks: 100,
    zIndex: 1000,
    colors: ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#6366f1', '#8b5cf6', '#f43f5e']
  };

  function randomInRange(min, max) {
    return Math.random() * (max - min) + min;
  }

  const interval = setInterval(function() {
    const timeLeft = animationEnd - Date.now();

    if (timeLeft <= 0) {
      return clearInterval(interval);
    }

    // Increase particle count when more time left, decrease near end for smooth stop
    const particleCount = 80 * (timeLeft / duration);

    // Fire confetti from left and right sides with random angles
    confetti(Object.assign({}, defaults, {
      particleCount: particleCount,
      origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 },
      angle: randomInRange(55, 125),
      scalar: randomInRange(0.8, 1.2)
    }));

    confetti(Object.assign({}, defaults, {
      particleCount: particleCount,
      origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 },
      angle: randomInRange(235, 305),
      scalar: randomInRange(0.8, 1.2)
    }));

  }, 200);
}
