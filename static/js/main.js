const slider= document.querySelector("#slider");
let sliderText= null;
let slides = null;
let slidesText = null;

if( slider) {
    sliderText = document.querySelector("#sliderText");
    slides = slider.getElementsByTagName('img');
    slidesText = sliderText.getElementsByTagName('div');

}
let index = 0;

function nextSlide(forward_backward){
    slides[index].classList.remove('active');
    slidesText[index].classList.remove('active');
    index = (index+forward_backward) % slides.length;
    if (index < 0){
        index = slides.length-1;
    }
    slides[index].classList.add('active');
    slidesText[index].classList.add('active');
}

function menuToggle(){
    const nav = document.querySelector('#navbar');
    document.querySelector("#nav_ul").style.transition = "ease-in-out 2s";
    nav.classList.toggle('active');
    
}

const project_tab = document.querySelector('.content_products')

if (project_tab){

    function elapsedTime(){
        const countDownDate = new Date('2020-03-01 12:00:00').getTime();
        const now = new Date().getTime();
        const gap = countDownDate - now;

        const second = 1000;
        const minute = 60*second;
        const hour = 60*minute;
        const day = 24*hour;

        const d_dif = Math.floor(gap/day);
        const h_dif = Math.floor((gap%day)/hour);
        const m_dif = Math.floor((gap%hour)/minute);
        const s_dif = Math.floor((gap%minute)/second);

        document.querySelector('#day').innerHTML = d_dif;
        document.querySelector('#hour').innerHTML = h_dif;
        document.querySelector('#minute').innerHTML = m_dif;
        document.querySelector('#second').innerHTML = s_dif;
    }
    elapsedTime()
    
    setInterval(function(){
        elapsedTime();
    },1000);

}