const $txtname=document.getElementById('txtname');
const $formulario=document.getElementById('formulario');
const $btneliminar=document.querySelectorAll('.btneliminar');

noti(document.title,"cursos listados correctamente","success","ok");

$formulario.addEventListener('submit',function(e){
    let nombre=String($txtname.value).trim();
    if (nombre.length==0){
        noti(document.title,"el nombre de curso esta vacio","warning","ok");
        e.preventDefault();
    }
});
/*
$btneliminar.forEach(btn => {
    btn.addEventListener('click', function(e){
        let confirma=confirm('decea eliminar este curso')
        if(!confirma){
            e.preventDefault();
        }
    })
});
*/

$btneliminar.forEach((btn)=>{
    btn.addEventListener('click',function(e){
        e.preventDefault();
        Swal.fire({
            title:"desea eliminar este curso",
            showCancelButton:true,
            confirmButtonText:"eliminar",
            confirmButtonColor:"#d33",
            backdrop:true,
            showLoaderOnConfirm:true,
            preConfirm:()=>{
                location.href=e.target.href;
            },
            allowOutsideclick:()=>false,
            allowEscapekey:()=>false,

        })
    });
});


