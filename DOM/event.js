// Event Listeners

// element.addEventListener("click", function);

const button = document.querySelector('.button');

function alertBtn() {
    alert('I Love Python');
};

button.addEventListener("click", alertBtn);

// MouseOver
const newBackgroundColor = document.querySelector('#btn3');

function changeColor(){
    newBackgroundColor.style.backgroundColor = 'blue';
};

newBackgroundColor.addEventListener("mouseover", changeColor);