
<!-- product-create (X) -->

let url = 'http://127.0.0.1:8000/shops/product-create/';
const reqOptions = {
    method :'POST',
    headers: {
        'Authorization':'Token ee8674d8b38144e915555d23e23a60e6fca1e2e6',
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




<!-- sign-in (X) -->

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





<!-- product-detail (#) -->
let url = 'http://127.0.0.1:8000/shops/product-detail/shop/1/product/1';
const reqOptions = {
    method :'GET',
    headers: {
        'Authorization':'Token ee8674d8b38144e915555d23e23a60e6fca1e2e6',
    }
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));




<!-- product-list (#) -->
let url = 'http://127.0.0.1:8000/shops/product-list/shop/1';
const reqOptions = {
    method :'GET',
    headers: {
        'Authorization':'Token ee8674d8b38144e915555d23e23a60e6fca1e2e6',
    }
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));





<!-- shop-list (#) -->
let url = 'http://127.0.0.1:8000/shops/shop-list';
const reqOptions = {
    method :'GET',
    headers: {
        'Authorization':'Token ee8674d8b38144e915555d23e23a60e6fca1e2e6',
    }
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));






<!-- shop-detail (#) -->
let url = 'http://127.0.0.1:8000/shops/shop-detail/1';
const reqOptions = {
    method :'GET',
    headers: {
        'Authorization':'Token ee8674d8b38144e915555d23e23a60e6fca1e2e6',
    }
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));



<!-- shop-update (X) -->
let url = 'http://127.0.0.1:8000/shops/shop-update/2/';
const reqOptions = {
    method :'PUT',
    headers: {
        'Authorization':'Token ee8674d8b38144e915555d23e23a60e6fca1e2e6',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(
        { 
            'shopBio':'testing',
        }
    )
};

fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));


<!-- product-delete (#) -->
let url = 'http://127.0.0.1:8000/shops/product-delete/2/';
const reqOptions = {
    method :'DELETE',
    headers: {
        'Authorization':'Token ee8674d8b38144e915555d23e23a60e6fca1e2e6',
	'Content-Type': 'application/json',
    },
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));



<!-- product-delete (#) -->
let url = 'http://127.0.0.1:8000/shops/shop-delete/1/';
const reqOptions = {
    method :'DELETE',
    headers: {
        'Authorization':'Token ee8674d8b38144e915555d23e23a60e6fca1e2e6',
    'Content-Type': 'application/json',
    },
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));





<!-- 16681 -->