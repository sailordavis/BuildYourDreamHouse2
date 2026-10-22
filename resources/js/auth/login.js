import { ApiConfig } from '../core/api_config.js';
import { HttpClient } from '../core/http_client.js';
import { TokenStorage } from '../core/token_storage.js';
import { AppRoutes } from '../core/app_routes.js';

document.addEventListener('DOMContentLoaded', () => {

    const loginForm = document.getElementById('loginForm');
    const loginError = document.getElementById('loginError');

    loginForm.addEventListener('submit', async (event) => {

        event.preventDefault();

        loginError.hidden = true;

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        try {

            // Enviar credenciales a Laravel
            const response = await HttpClient.post(
                ApiConfig.auth.login,
                {
                    email: email,
                    password: password
                }
            );

            // Obtener token y usuario
            const token = response.token;
            const usuario = response.usuario;

            if (!token || !usuario) {
                throw new Error('Respuesta de autenticación incompleta');
            }

            // Guardar token de autenticación
            TokenStorage.saveToken(token);

            // Redirigir según el rol
            AppRoutes.redirectByRole(usuario.rol_id);

        } catch (error) {

            loginError.textContent = error.message;
            loginError.hidden = false;

            console.error('Error al iniciar sesión:', error);
        }

    });

});
