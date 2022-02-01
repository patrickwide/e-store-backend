// get all products
let url = 'http://127.0.0.1:8000/users/product-list/';
const reqOptions = {
    method :'GET',
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));


// get product details
let url = 'http://127.0.0.1:8000/users/product-detail/1';
const reqOptions = {
    method :'GET',
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));

// query with category
let url = 'http://127.0.0.1:8000/users/productQuery-category/1';
const reqOptions = {
    method :'GET',
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));


// query with shop
let url = 'http://127.0.0.1:8000/users/productQuery-shop/1';
const reqOptions = {
    method :'GET',
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));

// shoppingCache-list
let url = 'http://127.0.0.1:8000/users/shoppingCache-list';
const reqOptions = {
    method :'GET',
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));

// purchase-list
let url = 'http://127.0.0.1:8000/users/purchase-list';
const reqOptions = {
    method :'GET',
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err));

// purchase-create
let url = 'http://127.0.0.1:8000/users/purchase-create/';
const reqOptions ={
    method:'POST',
    headers:{ 'Content-Type': 'application/json' },
    body:JSON.stringify({"product":2,"note":"api testing"})
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err))



// register
let url = 'http://127.0.0.1:8000/users/accounts/register/';
const reqOptions ={
    method:'POST',
    headers:{ 'Content-Type': 'application/json' },
    body:JSON.stringify({username:'testing',email:'testing@gmail.com',password:'police911.4089',password_confirm:'police911.4089'})
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err))

// login
let url = 'http://127.0.0.1:8000/users/accounts/login/';
const reqOptions ={
    method:'POST',
    headers:{ 'Content-Type': 'application/json' },
    body:JSON.stringify({login:'patrickwide',password:'police911.4089'})
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err))

// profile
let url = 'http://127.0.0.1:8000/users/accounts/profile/';
const reqOptions ={
    method:'GET',
    headers:{ 'Content-Type': 'application/json' },
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err))

// change-password
let url = 'http://127.0.0.1:8000/users/accounts/change-password/';
const reqOptions ={
    method:'POST',
    headers:{ 'Content-Type': 'application/json' },
    body:JSON.stringify({oldPassword:'police911.4089',password:'newpassword.4089'})
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err))



// logout
let url = 'http://127.0.0.1:8000/users/accounts/logout/';
const reqOptions ={
    method:'POST',
    headers:{ 'Content-Type': 'application/json' },
    body:JSON.stringify({})
};
fetch(url,reqOptions)
    .then(res => res.json())
    .then(data => console.log(data))
.catch(err => console.log(err))

for (var i = 0; i < 50; i++) {
    (()=>{
        // get all products
        var url = 'http://127.0.0.1:8000/users/product-list/';
        var reqOptions = {
            method :'GET',
        };
        fetch(url,reqOptions)
            .then(res => res.json())
            .then(data => console.log(data))
        .catch(err => console.log(err));


        // get product details
        var url = 'http://127.0.0.1:8000/users/product-detail/1';
        var reqOptions = {
            method :'GET',
        };
        fetch(url,reqOptions)
            .then(res => res.json())
            .then(data => console.log(data))
        .catch(err => console.log(err));

        // query with category
        var url = 'http://127.0.0.1:8000/users/productQuery-category/1';
        var reqOptions = {
            method :'GET',
        };
        fetch(url,reqOptions)
            .then(res => res.json())
            .then(data => console.log(data))
        .catch(err => console.log(err));


        // query with shop
        var url = 'http://127.0.0.1:8000/users/productQuery-shop/1';
        var reqOptions = {
            method :'GET',
        };
        fetch(url,reqOptions)
            .then(res => res.json())
            .then(data => console.log(data))
        .catch(err => console.log(err));

        // shoppingCache-list
        var url = 'http://127.0.0.1:8000/users/shoppingCache-list';
        var reqOptions = {
            method :'GET',
        };
        fetch(url,reqOptions)
            .then(res => res.json())
            .then(data => console.log(data))
        .catch(err => console.log(err));

        // purchase-list
        var url = 'http://127.0.0.1:8000/users/purchase-list';
        var reqOptions = {
            method :'GET',
        };
        fetch(url,reqOptions)
            .then(res => res.json())
            .then(data => console.log(data))
        .catch(err => console.log(err));

    })();

    console.log("i")
}