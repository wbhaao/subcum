const images = ["bg1.jpeg", "bg2.jpeg", "bg3.jpeg"];

const bg_value = images[Math.floor(Math.random() * images.length)]

const bgImage = document.createElement('img');
bgImage.src = `img/${bg_value}`

document.body.appendChild(bgImage)