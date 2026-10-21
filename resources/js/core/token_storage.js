// Archivo encargado de administrar el token de autenticación

export const TokenStorage = {

    // Guardar el token cuando el usuario inicia sesión
    saveToken(token) {
        sessionStorage.setItem('auth_token', token);
    },

    // Obtener el token almacenado
    getToken() {
        return sessionStorage.getItem('auth_token');
    },

    // Eliminar el token cuando el usuario cierra sesión
    removeToken() {
        sessionStorage.removeItem('auth_token');
    },

    // Comprobar si existe un token almacenado
    hasToken() {
        return this.getToken() !== null;
    }

};