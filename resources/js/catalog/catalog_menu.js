
import { AppRoutes } from '../core/app_routes.js';
import { ApiConfig } from '../core/api_config.js';
import { HttpClient } from '../core/http_client.js';
import { TokenStorage } from '../core/token_storage.js';

// Cargar menú cuando esté listo el HTML
document.addEventListener('DOMContentLoaded', async () => {

    const guestMenu = document.getElementById('guestMenu');
    const clientMenu = document.getElementById('clientMenu');
    const logoutBtn = document.getElementById('logoutBtn');

    // Mostrar opciones del visitante
    function showGuestMenu() {
        guestMenu.hidden = false;
        clientMenu.hidden = true;
    }

    // Mostrar opciones del cliente
    function showClientMenu() {
        guestMenu.hidden = true;
        clientMenu.hidden = false;
    }

    // Comprobar si existe un token
    if (!TokenStorage.hasToken()) {
        showGuestMenu();
    } else {

        try {
            // Consultar usuario autenticado
            const response = await HttpClient.get(ApiConfig.auth.me);
            const user = response.usuario;

            // Verificar rol de cliente
            if (Number(user.rol_id) === 1) {
                showClientMenu();
            } else if (Number(user.rol_id) === 3) {
                AppRoutes.redirectByRole(user.rol_id);
            } else {
                console.warn('Rol desconocido');
                TokenStorage.removeToken();
                showGuestMenu();
            }

        } catch (error) {
            console.error('Error de autenticación:', error);
            TokenStorage.removeToken();
            showGuestMenu();
        }
    }

    // Cerrar sesión
    logoutBtn.addEventListener('click', async () => {

        try {
            // Solicitar cierre de sesión al backend
            await HttpClient.post(ApiConfig.auth.logout);

            // Eliminar token almacenado
            TokenStorage.removeToken();

            // Regresar al catálogo público
            AppRoutes.navigate(AppRoutes.routes.home);

        } catch (error) {
            console.error('Error al cerrar sesión:', error);
            alert('No se pudo cerrar sesión');
        }
    });

});

//NUEVAS LINEAS DE CODIGO INTEGRADAS

// Variables del catálogo
let paginasAVON = [];
let pinturasClasificadas = [];


//Funcion para cargar el json que clasificara las pinturas 

async function cargarClasificaciones() {

    try {

        const response = await fetch('/json/clasificacion.json');

        if (!response.ok) {
            throw new Error('No se pudo cargar el archivo JSON');
        }

        paginasAVON = await response.json();

        await llamadaAPI();

    } catch (error) {
        console.error('Error al cargar clasificaciones:', error);
    }
}


/*
|--------------------------------------------------------------------------
| Enviar las clasificaciones al backend
|--------------------------------------------------------------------------
*/

async function llamadaAPI() {

    try {
        //await HttpClient.post(ApiConfig.auth.logout);
        const data = await HttpClient.post(ApiConfig.catalog.showProduct,paginasAVON);

        pinturasClasificadas = data;

        console.log('Pinturas clasificadas:', pinturasClasificadas);

        mostrarCatalogo();

    } catch (error) {
        console.error('Error al obtener el catálogo:', error);
    }
}


/*
|--------------------------------------------------------------------------
| Mostrar las categorías en el Offcanvas
|--------------------------------------------------------------------------
*/

function mostrarCatalogo() {

    const contenedor = document.getElementById('Opciones');

    // Limpiar las opciones anteriores
    contenedor.innerHTML = '';

    pinturasClasificadas.forEach((modulo) => {

        // Contenedor del dropdown
        const dropdown = document.createElement('div');
        dropdown.className = 'dropdown mt-3';

        // Botón principal de la clasificación
        const boton = document.createElement('button');
        boton.className = 'btn btn-secondary dropdown-toggle';
        boton.type = 'button';
        boton.setAttribute('data-bs-toggle', 'dropdown');
        boton.textContent = modulo.clasificacion;

        // Lista de subcategorías
        const lista = document.createElement('ul');
        lista.className = 'dropdown-menu';

        modulo.submodulos.forEach((submodulo) => {

            const item = document.createElement('li');

            const opcion = document.createElement('button');
            opcion.className = 'dropdown-item';
            opcion.type = 'button';
            opcion.textContent = submodulo.Nombre;

            // Mostrar las pinturas de la categoría seleccionada
            opcion.addEventListener('click', () => {

                mostrarPinturas(
                    submodulo.pinturas,
                    submodulo.Nombre
                );

                // Cerrar el Offcanvas al seleccionar una categoría
                const offcanvasElement =
                    document.getElementById('offcanvasExample');

                if (offcanvasElement) {
                    const instancia =
                        bootstrap.Offcanvas.getInstance(offcanvasElement);

                    instancia?.hide();
                }

            });

            item.appendChild(opcion);
            lista.appendChild(item);

        });

        // Mantener la estructura original del dropdown
        dropdown.appendChild(boton);
        dropdown.appendChild(lista);

        contenedor.appendChild(dropdown);

    });

}


/*
|--------------------------------------------------------------------------
| Mostrar las pinturas de la categoría seleccionada
|--------------------------------------------------------------------------
*/

function mostrarPinturas(pinturas, titulo) {

    let interfaz = `
   <h1 style ="margin-left: 120px;">${titulo}</h1>
     <div class="container mt-4">
    <div class="row g-4">`;
    pinturas.forEach(element => {

       // La imagen se encuentra dentro de public/imagenesPintura
     const imagen = '/' + element.imagen.replace(/^\/+/, '');
       interfaz += ` 
         <div class="col-md-3">
            <div class="card h-100 shadow" data-stock="${element.stock}" data-id="${element.id}">
                <img src="${imagen}" class="card-img-top" alt="Pintura Recomendada">
                <div class="card-body">
                    <h5 class="card-title">${element.nombre}</h5>
                    <p class="card-text">Color: ${element.color}</p>
                    <p class="card-text">Limite de Compra: ${element.stock}</p>
                    <p class="card-text">${element.descripcion}</p>
                    <p class="card-text">$ ${element.precio}</p>
                    <!-- CONTADOR + BOTON -->
                    <div class="d-flex align-items-center gap-3 mt-3">

                        <!-- Contador -->
                        <div class="d-flex border rounded overflow-hidden" style="width: 130px;">
                            <button class="btn py-2 flex-fill btn-menos"
                                    style="border:none; color:#ff7a00; font-size:20px;">−</button>

                            <div class="cantidad d-flex justify-content-center align-items-center"
                                 style="width:50px; font-size:18px; font-weight:600;">
                                1
                            </div>

                            <button class="btn py-2 flex-fill btn-mas"
                                    style="border:none; color:#ff7a00; font-size:20px;">+</button>
                        </div>

                        <!-- Botón Agregar -->
                        <button class="btn btn-agregar"
                                style="border: 2px solid #c40000; color:#c40000; padding:8px 20px; border-radius:8px;"
                                onclick = "AgregarAlCarrito(${element.id},this)">
                            Agregar
                        </button>

                    </div>

                </div>
            </div>
        </div>
       `;
});
    interfaz += `   </div>
                  </div>`;
      $("#Pinturas").html(interfaz);
}


/*
|--------------------------------------------------------------------------
| Inicialización del catálogo
|--------------------------------------------------------------------------
*/

// Llama a esta función dentro de tu DOMContentLoaded existente,
// si tu archivo ya tiene uno.
cargarClasificaciones();

