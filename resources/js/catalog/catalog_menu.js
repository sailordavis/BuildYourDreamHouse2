
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


/*
|--------------------------------------------------------------------------
| Cargar el JSON de clasificaciones
|--------------------------------------------------------------------------
*/

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

    contenedor.innerHTML = '';

    pinturasClasificadas.forEach((modulo) => {

        const dropdown = document.createElement('div');

        dropdown.className = 'dropdown mt-3';

        const boton = document.createElement('button');

        boton.className = 'btn btn-secondary dropdown-toggle';
        boton.type = 'button';
        boton.setAttribute('data-bs-toggle', 'dropdown');
        boton.textContent = modulo.clasificacion;

        const lista = document.createElement('ul');

        lista.className = 'dropdown-menu';

        modulo.submodulos.forEach((submodulo) => {

            const item = document.createElement('li');
            const opcion = document.createElement('button');

            opcion.className = 'dropdown-item';
            opcion.type = 'button';
            opcion.textContent = submodulo.Nombre;

            opcion.addEventListener('click', () => {

                mostrarPinturas(
                    submodulo.pinturas,
                    submodulo.Nombre
                );

                // Cerrar el Offcanvas al seleccionar una categoría
                const offcanvasElement =
                    document.getElementById('offcanvasCategorias');

                const instancia =
                    bootstrap.Offcanvas.getInstance(offcanvasElement);

                instancia?.hide();

            });

            item.appendChild(opcion);
            lista.appendChild(item);

        });

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

    const contenedor = document.getElementById('Pinturas');

    contenedor.innerHTML = '';

    const encabezado = document.createElement('h2');

    encabezado.className = 'mb-4';
    encabezado.textContent = titulo;

    contenedor.appendChild(encabezado);

    if (pinturas.length === 0) {

        const mensaje = document.createElement('p');

        mensaje.className = 'text-muted';
        mensaje.textContent =
            'No hay pinturas disponibles para esta categoría.';

        contenedor.appendChild(mensaje);

        return;
    }

    const container = document.createElement('div');
    container.className = 'container';

    const row = document.createElement('div');
    row.className = 'row g-4';

    pinturas.forEach((pintura) => {

        const columna = document.createElement('div');
        columna.className = 'col-12 col-sm-6 col-lg-3';

        // La imagen se encuentra dentro de public/imagenesPintura
        const imagen = '/' + pintura.imagen.replace(/^\/+/, '');

        columna.innerHTML = `
            <div class="card h-100 shadow-sm">

                <img
                    src="${imagen}"
                    class="card-img-top"
                    alt="Pintura"
                    style="height:220px; object-fit:contain;"
                >

                <div class="card-body">

                    <h5 class="card-title"></h5>

                    <p class="card-text color"></p>

                    <p class="card-text stock"></p>

                    <p class="card-text descripcion"></p>

                    <p class="card-text precio fw-bold"></p>

                </div>

            </div>
        `;

        columna.querySelector('.card-title').textContent =
            pintura.nombre;

        columna.querySelector('.color').textContent =
            'Color: ' + pintura.color;

        columna.querySelector('.stock').textContent =
            'Límite de compra: ' + pintura.stock;

        columna.querySelector('.descripcion').textContent =
            pintura.descripcion ?? '';

        columna.querySelector('.precio').textContent =
            '$ ' + pintura.precio;

        row.appendChild(columna);

    });

    container.appendChild(row);
    contenedor.appendChild(container);
}


/*
|--------------------------------------------------------------------------
| Inicialización del catálogo
|--------------------------------------------------------------------------
*/

// Llama a esta función dentro de tu DOMContentLoaded existente,
// si tu archivo ya tiene uno.
cargarClasificaciones();

