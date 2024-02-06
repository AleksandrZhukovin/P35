function func(a, b=12){
    return a + b;
}

func(12);

var a = func;

setTimeout(function(){ }, 1000)

let f = function (){

}

function calculator(){
    let num1 = Number(prompt('Enter first number'));
    let num2 = Number(prompt('Enter second number'));
    let oper = prompt('Enter operation you want to do');
    document.getElementById('num1').innerHTML += num1;
    document.getElementById('num2').innerHTML += num2;
    document.getElementById('oper').innerHTML += oper;

    if (oper == '+'){
         document.getElementById('res').innerHTML = `${num1} + ${num2} = ${num1 + num2}`;
    } else if (oper == '-'){
        document.getElementById('res').innerHTML = `${num1} - ${num2} = ${num1 - num2}`;
    }
}

window.onload = calculator;


document.detElementsByClassName('class')  // array
document.detElementsByTagName('h3')
document.detElementsByName('h3')

document.body // document.head

//document.getElementById('num1').className = 'new class';
document.getElementById('num1').classList.add('class3'); // class1 class2 class3
document.getElementById('num1').classList.remove('class2'); // class1 class3

// створити дів і змінювати його колір таким який введе користувач
document.getElementById('num1').style.backgroundColor = 'red';

function changeColor(){

}

var img = document.getElementById('pic');
var count = 0;

setTimeout(function(){
    if (count == 0){
        img.src = '';
        count += 1
    } else if (count == 1){
        img.src = '';
        count += 1
    }else if (count == 2){
        img.src = '';
        count = 0
    }
}, 10000)

