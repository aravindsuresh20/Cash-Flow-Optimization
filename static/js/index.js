// static/js/index.js
document.addEventListener('DOMContentLoaded', function() {
    // Interactive cursor effects
    const interactiveElements = document.querySelectorAll('a, button, input, .form-container');
    
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
  
    // Form input focus effects
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
      input.addEventListener('focus', () => {
        input.parentElement.querySelector('label').style.color = 'var(--primary)';
      });
      
      input.addEventListener('blur', () => {
        input.parentElement.querySelector('label').style.color = 'var(--light)';
      });
    });
  });