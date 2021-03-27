var mpri = document.getElementById("primario").textContent.replace(/\s/g, '').split(";");
var msec = document.getElementById("secundario").textContent.replace(/\s/g, '').split(";");
var i ;


for (i = 0; i < mpri.length; i++) {
    var id = "path".concat(mpri[i]);
    document.getElementById(id).setAttribute("style", "fill: #025920");

}

for (i = 0; i < msec.length; i++) {
    var id = "path".concat(msec[i]);
    document.getElementById(id).setAttribute("style", "fill: #7AA61b");

}