
const flow = document.getElementById('flow')
const icon = document.getElementById('fo')
function displayIcon(){
    
    // document.querySelector('.fa-heart').innerHTML = "<i class=\"fa-solid fa-heart\"></i>"
    // icon.setAttribute('class', 'fa-hearts')
    flow.classList.toggle('fo')
    let status = flow.classList.contains('fo')
    if(status == true){
        icon.style.color = "red"
    }
    else{
        icon.style.color = null
    }
}


////////////////////////

const follow = document.getElementById('follow')
const flo = document.getElementById('fl')

function switcdarkhMode(){
    follow.classList.toggle('fl')
    let status = follow.classList.contains('fl')
    if(status == true){
        flo.innerText = "Following"
        flo.style.color = "black"
    }
    else{
        flo.innerText = "Follow"
        flo.style.color = null

    }
}
///////////
const follow1 = document.getElementById('follow1')
const fl1 = document.getElementById('fl1')

function switcdarkhMode1(){
    follow1.classList.toggle('fl1')
    let status = follow1.classList.contains('fl1')
    if(status == true){
        fl1.innerText = "Following"
        fl1.style.color = "black"
    }
    else{
        fl1.innerText = "Follow"
        fl1.style.color = null

    }
}
//////////////

const follow2 = document.getElementById('follow2')
const fl2 = document.getElementById('fl2')

function switcdarkhMode2(){
    follow2.classList.toggle('fl2')
    let status = follow2.classList.contains('fl2')
    if(status == true){
        fl2.innerText = "Following"
        fl2.style.color = "black"
    }
    else{
        fl2.innerText = "Follow"
        fl2.style.color = null

    }
}
/////////////
const follow3 = document.getElementById('follow3')
const fl3 = document.getElementById('fl3')

function switcdarkhMode3(){
    follow3.classList.toggle('fl3')
    let status = follow3.classList.contains('fl3')
    if(status == true){
        fl3.innerText = "Following"
        fl3.style.color = "black"
    }
    else{
        fl3.innerText = "Follow"
        fl3.style.color = null

    }
}
////////////////
const follow4 = document.getElementById('follow4')
const fl4 = document.getElementById('fl4')

function switcdarkhMode4(){
    follow4.classList.toggle('fl4')
    let status = follow4.classList.contains('fl4')
    if(status == true){
        fl4.innerText = "Following"
        fl4.style.color = "black"
    }
    else{
        fl4.innerText = "Follow"
        fl4.style.color = null

    }
}