var nameUser = 2, a, c ,b = 10;  // let <=> var
/*
multi
line
comment
*/

var a = 10, b = 2.5, c=NaN, d = -Infinity;  // number
b = 2 + 'a';  // a = NaN (Not a number)

typeof 2; // number

var s = 'Bob', v = "dfbj$@53", l=`Hello ${s}`;  // 'Hello Bob', type string

var t = true, y = false; // boolean

var m = null, u = undefined; 
var q; // undefined

// + - * / % ** 
console.log(a)
// c = 10 + a++ // 20
console.log(a++) // a += 1   10
a = 10
console.log(a)
console.log(++a) // 11
a-- // a -= 1
--a

console.log('Hello')
alert('Hello')

c = 1 + '1'; // 2
c = 2 + 'a'; // NaN
c = '2' + '1'; // 21

// < > <= >= == !=
2 == '2'; // true
2 == 'a'; // false
1 != '3'; // true
2 === '2'; // false
1 !== '3'; // true


// and <=> &&
// or <=> ||
// not <=> ! 

var input = prompt('Enter name', 'Bob');
Number(); // int()
String(); // str()
Boolean(); // bool()
var num = Number(prompt('Enter number'));

if (a > 0) alert('+');

if (a > 0) {
    alert('+');
    console.log('+');
} else if (a < 0) {
    alert('-')
} else {
    alert(0)
}

a = 10

c = (a > 0) ? '+' : '-' // c = '+' if a > 0 else '-'
c = (a > 0) ? '+' : 
    (a < 0) ? '-' : 0

var i = 11;
while (i <= 10){
    i++;
    if (i == 1){
        continue
    }
    if (i == 2) {
        break
    }
    console.log(i);
}

do {
    i++;
    console.log(i);
} while(i <= 10)

outer: for (let t = 0; t < 10; t++){
    console.log(t);
    for (let i = 0; i < 100; i++){
        if (i == 25){
            break outer;
        }
    }
}

let s = 'HEllo';
console.log(s.length); // 5
console.log(s[1]); // E
console.log(s.at(1)); // E
// \n \t
s = `hello
    hello
    hello`
s = 'Hello'
console.log(s.toUpperCase()); // HELLO
console.log(s.toLoverCase()); // hello
console.log(s.indexOf('l'));
s.includes('ll'); // 'll' in 'hello'
s.startsWith('He'); // true
s.endsWith('o'); //true
s.slice(1, 3); // el
s.slice(3, 1); // ''
s.substring(1, 3); // el
s.substring(3, 1); // el
s.substr(1, 2); // el

'a' > 'Z'; // true
'Adam' > 'Bob'; // true
'hello'.replace('l', 'J'); // hejjo

for (let i of s) {
    console.log(i); // h, e, l, l, o
}
// запитати ввести строку, порахувати кількість слів в ній
// прийняти строку типу "12фва34312ыва". Отримати чисте число (видалити символи не цифри) replace()

let m = [1, 2, 'a', true];
m = new Array();
m[2]; // 'a'
m[2] = 3; // [1, 2, 3, true]
m.length; // 4
// FIFO 
m.push(4); // [1, 2, 3, true, 4] 
m.shift(); // [2, 3, true, 4]
m.pop(); // [2, 3, true]
m.unshift(5); // [5, 2, 3, true]

for (let i in m) {
    console.log(i); 
}

let y = [];
y[100] = 1;
y.length; // 101

y = [[1, 2, 3], [4, 5, 6]];
y[1][2]; // 6

y = [1, 2, 3]
String(y); // '1, 2, 3'

[1] + 1; // 11
[1, 2] + 1; // 1,21