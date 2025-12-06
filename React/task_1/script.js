const button = document.getElementById('myButton1');
button.addEventListener('click', function(){
        const newDiv = document.createElement('div');
        newDiv.textContent = 'new block';
        const container = document.querySelector('.task_1');
        newDiv.className = 'block1'
        container.appendChild(newDiv);
    });
const spots = document2.getElementById('myButton2');
spots.addEventListener('click', function(){
    fetch('http://test.spotic.ru/api/spot/list/for-map', {
        method: 'POST', headers: {
        }
    })
    });