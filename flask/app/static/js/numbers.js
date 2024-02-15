window.onload = function(){
    var num1 = prompt('Enter number 1'), num2 = prompt('Enter number 2'), oper=prompt('Enter operation');
    document.getElementById('data').href += `num=${num1}&number=${num2}&oper=%{oper}`;
}