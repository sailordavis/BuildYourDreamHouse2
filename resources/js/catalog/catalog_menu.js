
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
