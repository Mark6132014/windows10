console.log("%cSTOP!\nIf something is wrong, you can debug it using the Inspect element.\nWebsite: %o", "color: red; background: white", "https://itzgametime-vip.w3spaces.com");
setInterval(() => {
    document.querySelector('.taskbar .time').innerHTML = new Date().getHours() + ':' + new Date().getMinutes() + ':' + new Date().getSeconds() + '<br>' + new Date().getMonth() + '/' + new Date().getDay() + '/' + new Date().getFullYear();
}, 1000);
var taskbar = {
    startSearch: function() {
        document.querySelector(".start").style.display = "block";
    }
}
var startbuttons = [
    document.querySelector(".taskbar .startNow"),
    document.querySelector(".taskbar .search")
];
for (var i = 0; i < startbuttons.length; i++) {
    startbuttons[i].addEventListener("click", () => {
        taskbar.startSearch();
    });
    startbuttons[i].addEventListener("input", () => {
        taskbar.startSearch();
    });
}
setTimeout(() => {
    document.querySelector(".startup #start").style.display = "block";
}, 3000);