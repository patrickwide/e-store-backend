let url = 'http://127.0.0.1:8000/shops/sign-in/';
const reqOptions = {
    method :'POST',
    headers: {
        'Authorization':'Token 7ecb99cba1cdc2884f366a85f4ae68b299c8d570',
	'Content-Type': 'application/json',
    },
    body: JSON.stringify({ 
		           'username':'patrickwide',  
			   'password': 'police911.4089' 
			})
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));


let url = 'http://127.0.0.1:8000/shops/product-list';
const reqOptions = {
    method :'GET',
    headers: {
        'Authorization':'Token c2e0bb9c78253fae9ed5036be26d4d9bafed294a',
    }
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));
