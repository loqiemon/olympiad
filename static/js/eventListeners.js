const listItems = document.querySelectorAll('.goals__list-item');
const cardTitle = document.querySelector('.goals__card-title');
const cardDescription = document.querySelector('.goals__card-description');


function updateCard(goal) {
    switch (goal) {
        case 'creative':
            cardTitle.textContent = 'Творческие способности';
            cardDescription.textContent = 'Выявление и развитие у учащихся, осваивающих общеобразовательные программы основного общего и среднего общего образования, творческих способностей и интереса к научно-исследовательской деятельности';
            break;
        case 'talented':
            cardTitle.textContent = 'Одаренные дети';
            cardDescription.textContent = 'Описание пункта';
            break;
        case 'scientific':
            cardTitle.textContent = 'Научные знания';
            cardDescription.textContent = 'Описание пункта';
            break;
        case 'career':
            cardTitle.textContent = 'Профессиональная ориентация';
            cardDescription.textContent = 'Описание пункта';
            break;
        case 'youth':
            cardTitle.textContent = 'Талантливая молодежь';
            cardDescription.textContent = 'Описание пункта';
            break;
        default:
            break;
    }
}

listItems.forEach(item => {
    item.addEventListener('click', () => {
        const goal = item.getAttribute('data-goal');
        updateCard(goal);
    });
});


updateCard('creative');
