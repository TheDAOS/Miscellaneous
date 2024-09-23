const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

canvas.addEventListener('click', handleDrawCircle);

let x, y;

const move = () => {
  const dx = Math.random() * 3;
  const dy = Math.random() * 7;

  x = x + dx;
  y = y - dy;
};

const drawCircle = (x, y) => {
    context.beginPath();
    context.arc(x, y, 50, 0, 2 * Math.PI);
  
    context.strokeStyle = 'white';
    context.stroke();
  };

