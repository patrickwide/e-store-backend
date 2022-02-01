let url = 'http://127.0.0.1:8000/shops/product-detail/1/';
const reqOptions = {
    method :'GET',
    headers: {
        'Authorization':'Token c2e0bb9c78253fae9ed5036be26d4d9bafed294a',
	'Content-Type': 'application/json',
    },
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));




let url = 'http://127.0.0.1:8000/shops/product-delete/2/';
const reqOptions = {
    method :'DELETE',
    headers: {
        'Authorization':'Token c2e0bb9c78253fae9ed5036be26d4d9bafed294a',
	'Content-Type': 'application/json',
    },
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));











let url = 'http://127.0.0.1:8000/shops/product-create/';
const reqOptions = {
    method :'POST',
    headers: {
        'Authorization':'Token c2e0bb9c78253fae9ed5036be26d4d9bafed294a',
	'Content-Type': 'application/json',
    },
    body: JSON.stringify({ 
			   'shop','1',
		           'productName':'create test', 
		           'productPrice':1000, 
		           'productCategory':3, 
		           'productDescription':'this is a test desc', 
			})
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));




















let url = 'http://127.0.0.1:8000/shops/product-create/';
const reqOptions = {
    method :'POST',
    headers: {
        'Authorization':'Token c2e0bb9c78253fae9ed5036be26d4d9bafed294a',
	'Content-Type': 'application/json',
    },
    body: JSON.stringify({ 
                   	   'shop':1,
		           'productName':'create test', 
		           'productPrice':1000, 
		           'ProductCategory':1, 
		           'productDescription':'this is a test create desc' 
			})
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));



{
	"shopName","test shop",
	"shopProfile","test shop",
	"shopBio","test shop",
	"shopLocation","test shop",
}









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




















let url = 'http://127.0.0.1:8000/shops/shop-list';
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
























let url = 'http://127.0.0.1:8000/shops/shop-detail/1';
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
