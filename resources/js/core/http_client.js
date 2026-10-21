
import { ApiConfig } from './api_config.js';
import { TokenStorage } from './token_storage.js';

export const HttpClient = {

    // Función principal para realizar peticiones HTTP
    async request(method, endpoint, body = null) {

        const token = TokenStorage.getToken();

        const headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        };

        // Agregar token si existe
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        // Configuración de la petición
        const options = {
            method: method,
            headers: headers
        };

        // Agregar datos para POST, PUT y PATCH
        if (body !== null) {
            options.body = JSON.stringify(body);
        }

        // Realizar petición al backend
        const response = await fetch(
            ApiConfig.baseUrl + endpoint,
            options
        );

        // Convertir respuesta a JSON, si existe
        const contentType = response.headers.get('content-type') || '';

        const data = contentType.includes('application/json')
            ? await response.json()
            : null;

        // Manejar errores HTTP
        if (!response.ok) {

            if (response.status === 401) {
                console.warn('Usuario no autenticado o token inválido');
            }

            if (response.status === 403) {
                console.warn('No tienes permisos para esta operación');
            }

            if (response.status === 422) {
                console.warn('Error de validación', data?.errors);
            }

            throw new Error(
                data?.message || `Error HTTP ${response.status}`
            );
        }

        return data;
    },

    // GET: Consultar información
    get(endpoint) {
        return this.request('GET', endpoint);
    },

    // POST: Enviar información
    post(endpoint, body) {
        return this.request('POST', endpoint, body);
    },

    // PUT: Actualizar información
    put(endpoint, body) {
        return this.request('PUT', endpoint, body);
    },

    // PATCH: Actualizar parcialmente
    patch(endpoint, body) {
        return this.request('PATCH', endpoint, body);
    },

    // DELETE: Eliminar información
    delete(endpoint) {
        return this.request('DELETE', endpoint);
    }

};
