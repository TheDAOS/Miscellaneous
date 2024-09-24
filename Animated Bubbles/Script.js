const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particleArray = [];

class Particle {
	constructor(x = 0, y = 0) {
		this.x = x;
		this.y = y;
		this.radius = Math.random() * 20 + 5; // Adjusted for more reasonable sizes
		this.dx = Math.random() * 3 - 1.5; // Random horizontal movement
		this.dy = Math.random() * 5 + 1; // Random vertical movement
		this.hue = Math.random() * 360; // Random hue for color variation
	}

	draw() {
		context.beginPath();
		context.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
		context.strokeStyle = `hsl(${this.hue}, 100%, 50%)`;
		context.stroke();

		const gradient = context.createRadialGradient(
			this.x,
			this.y,
			1,
			this.x + 0.5,
			this.y + 0.5,
			this.radius
		);

		gradient.addColorStop(0, "rgba(255, 255, 255, 0.3)");
		gradient.addColorStop(1, "#e7feff");

		context.fillStyle = gradient;
		context.fill();
	}

	move() {
		this.x += this.dx;
		this.y -= this.dy;

		// Remove particle if it goes off-screen
		if (this.y + this.radius < 0 || this.x + this.radius < 0 || this.x - this.radius > canvas.width) {
			const index = particleArray.indexOf(this);
			if (index > -1) {
				particleArray.splice(index, 1);
			}
		}
	}
}

const handleDrawCircle = (event) => {
	const a = event.pageX;
	const b = event.pageY;

	for (let i = 0; i < 50; i++) {
		const particle = new Particle(a, b);
		particleArray.push(particle);
	}
};

const animate = () => {
	context.clearRect(0, 0, canvas.width, canvas.height);

	particleArray.forEach((particle) => {
		particle.move();
		particle.draw();
	});

	requestAnimationFrame(animate);
};

canvas.addEventListener("click", handleDrawCircle);
canvas.addEventListener("resize", () => {
	canvas.width = window.innerWidth;
	canvas.height = window.innerHeight;
});

animate();