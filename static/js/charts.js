// static/js/charts.js
document.addEventListener('DOMContentLoaded', function() {
    // Interactive cursor effects
    const interactiveElements = document.querySelectorAll('a, .chart-container, .chart-img');
    
    interactiveElements.forEach(el => {
      el.addEventListener('mouseenter', () => {
        document.querySelector('.cursor').style.transform = 'translate(-50%, -50%) scale(1.5)';
        document.querySelector('.cursor-follower').style.transform = 'translate(-50%, -50%) scale(0.5)';
        document.querySelector('.cursor-follower').style.borderColor = 'var(--primary)';
      });
      
      el.addEventListener('mouseleave', () => {
        document.querySelector('.cursor').style.transform = 'translate(-50%, -50%) scale(1)';
        document.querySelector('.cursor-follower').style.transform = 'translate(-50%, -50%) scale(1)';
        document.querySelector('.cursor-follower').style.borderColor = 'var(--primary)';
      });
    });
  });