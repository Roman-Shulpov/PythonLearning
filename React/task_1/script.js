const button = document.getElementById('myButton1');
button.addEventListener('click', function(){
        const newDiv = document.createElement('div');
        newDiv.textContent = 'new block';
        const container = document.querySelector('.task_1');
        newDiv.className = 'block1';
        container.appendChild(newDiv);
    });
// ... (остальной код до myButton2) ...

document.getElementById('myButton2').addEventListener('click', function(){
    fetch('https://reqres.in/api/users?page=1', {
    headers: {
        'x-api-key': 'reqres_a36ffffd26a140ff8008465ffdca815d' // required on all endpoints
    }
    })
    .then(httpResponse => {
        console.log(httpResponse);
        return httpResponse.json();
    })
    .then(responseData => {
        console.log(responseData);
        for(let i=0; i < responseData.data.length; i++) {
            console.log(`
                email = ${responseData.data[i].email},
                имя = ${responseData.data[i].first_name},
                фамилия = ${responseData.data[i].last_name},
                аватар = ${responseData.data[i].avatar}
            `);
        const newDiv = document.createElement('div');
        const img = document.createElement('img');
        img.setAttribute('src', responseData.data[i].avatar);
        newDiv.textContent = responseData.data[i].email;
        const container = document.querySelector('.task_1');
        newDiv.className = 'block2';
        newDiv.appendChild(img);
        container.appendChild(newDiv);
        }
    });

    console.log('asdasd')
});

