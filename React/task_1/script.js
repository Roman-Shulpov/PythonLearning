const button = document.getElementById('myButton1');
button.addEventListener('click', function(){
        const newDiv = document.createElement('div');
        newDiv.textContent = 'new block';
        const container = document.querySelector('.task_1');
        newDiv.className = 'block1'
        container.appendChild(newDiv);
    });

