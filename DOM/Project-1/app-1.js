// Variables

let btn = document.querySelector('#new-quote');
let quote = document.querySelector('.quote');
let person = document.querySelector('.person');

const quotes =[
    {
      quote: "`Be the change that you wish to see in the world.`",
      person: `Mahatma Gandhi`
    },
    {
      quote: "`The only way to do great work is to love what you do.`",
      person: `Steve Jobs`
    },
    {
      quote: "`Success is not final, failure is not fatal: it is the courage to continue that counts.`",
      person: `Winston Churchill`
    },
    {
      quote: "`Education is the most powerful weapon which you can use to change the world.`",
      person: `Nelson Mandela`
    },
    {
      quote: "`Happiness is not something ready made. It comes from your own actions.`",
      person: `Dalai Lama`
    },
    {
      quote: "`Believe you can and you're halfway there.`",
      person: `Theodore Roosevelt`
    },
    {
      quote: "`In the end, we will remember not the words of our enemies, but the silence of our friends.`",
      person: `Martin Luther King Jr.`
    },
    {
      quote: "`I have not failed. I've just found 10,000 ways that won't work.`",
      person: `Thomas Edison`
    },
    {
      quote: "`You miss 100% of the shots you don't take.`",
      person: `Wayne Gretzky`
    },
    {
      quote: "`Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.`",
      person: `Albert Einstein`
    },
  ];

  btn.addEventListener('click', function(){

    let random = Math.floor(Math.random() * quotes.length);

    quote.innerText = quotes[random].quote;
    person.innerText = quotes[random].person;
  })
  
