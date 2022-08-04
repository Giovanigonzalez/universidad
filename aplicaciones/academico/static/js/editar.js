const $name=document.getElementById('name');
const $form=document.getElementById('form');

$form.addEventListener('submit',function(e){
    let nombre=String($name.value).trim();
    if (nombre.length==0){
        noti(document.title,"el nombre de curso esta vacio","warning","ok");
        e.preventDefault();
    }
})
