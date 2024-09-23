const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

canvas.addEventListener('click', handleDrawCircle);

//We are adding x and y here because we will need it later.
let x, y
const handleDrawCircle = (event) => {
  x = event.pageX;
  y = event.pageY;

  // Draw a bubble!
  drawCircle(x, y);
};

const drawCircle = (x, y) => {
    context.beginPath();
    context.arc(x, y, 50, 0, 2 * Math.PI);
  
    context.strokeStyle = 'white';
    context.stroke();
  };
  