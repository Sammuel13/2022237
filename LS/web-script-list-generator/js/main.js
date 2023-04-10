const listHTML = document.querySelector('.list');
const liNumber = document.querySelector('.quantity');
const button = document.querySelector('button');

function createList(liNumber)
{
    for (let i = 0;i < liNumber; i++)
    {
        listHTML.innerHTML += `
        <li>Item ${i+1}</li>
        `
    }
};

button.addEventListener('click', () => {
    listHTML.innerHTML = ''
    createList(liNumber.value)
});