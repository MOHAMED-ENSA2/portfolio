
function changeBackGroungColor(old_proprety , new_property){
    var r = document.querySelector(':root');
    var rs = getComputedStyle(r);
    r.style.setProperty(old_proprety , new_property);

}
//changeBackGroungColor('--mainColor', 'red') old_proprety , new_property
                
               