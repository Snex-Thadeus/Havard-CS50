// GetElementById()
const title = document.getElementById('main-heading');

title.style.color = 'white';

// GetElementByClassName()
const listItems = document.getElementsByClassName('list-items');


// GetElementsByTagName()

const listItem = document.getElementsByTagName('li');

// console.log(listItem);

// querySelector() matched the first item that comes across

const container = document.querySelector('div');


// querySelectorAll() returns a NodeList

const containers = document.querySelectorAll('.list-items');

// Styling Elements

// for(i=0; i<containers.length; i++){
//     containers[i].style.fontSize = '2rem';
// }


// Creating Elements

const ul = document.querySelector('ul');
const li = document.createElement('li');

// Adding Elements
ul.append(li);

// Modifying the text

li.innerText = 'X-mex';

// Modifying Elements Attributes & Classes

// li.setAttribute('class', 'list-items');


// li.removeAttribute('class', 'list-items');

// console.log(title.getAttribute('id'));

li.classList.add('list-items'); // li.classList.remove('list-items');

// Remove Elements
li.remove();

// Parent Node Traversal
// let ul1 = document.querySelector('ul');

// console.log(ul1.parentNode.parentNode);
// console.log(ul1.parentElement.parentElement);

// Child Node Traversal
let ul1 = document.querySelector('ul');

// console.log(ul1.childNodes);
// console.log(ul1.firstChild);
// console.log(ul1.lastChild);

console.log(ul1.children);


// Sibling Traversal
console.log(ul1.previousElementSibling);
console.log(ul1.nextSibling);

// Event Listeners