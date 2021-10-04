function init()
{
    var h1tags = document.getElementsByTagName("h1");
    h1tags[0].onclick = changeColor;
}

function changeColor()
{
    this.innerHTML = "Click Again";
    var randColor = '#'+Math.floor(Math.random()*16777215).toString(16);
    this.style.color = randColor;
}

function toggleImg(){
    var img = document.getElementsByTagName("img")[0];
    var isVisible = img.style.visibility != "visible";
    img.style.visibility = isVisible ? "visible" : "hidden";
}

onload = init;