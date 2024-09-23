const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const handleDrawCircle = (event) => {
    const x = event.pageX;
    const y = event.pageY;
  
    const particle = new Particle(x, y);
  };
  
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

const animate = () => {
    context.clearRect(0, 0, canvas.width, canvas.height);

    move();
        drawCircle(x,y);

    requestAnimationFrame(animate);
};

//Don't forget to call animate at the bottom 
animate();

class Particle {
    constructor(x = 0, y = 0) {
      this.x = x;
      this.y = y;
      this.radius = Math.random() * 50;
      this.dx = Math.random() * 3;
      this.dy = Math.random() * 7;
      this.color = 'white';
    }
  
    draw() {
      context.beginPath();
      context.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
      context.strokeStyle = this.color;
      context.stroke();
  
      context.fillStyle = this.color;
      context.fill();
    }
  
    move() {
        this.x = this.x + this.dx;
        this.y = this.y - this.dy;
    }
  }  
  