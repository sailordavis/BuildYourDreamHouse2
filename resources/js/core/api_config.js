// Configuracion  general de la API

export const ApiConfig = {

//Direccion base de la API
baseUrl: 'http://localhost:8000/api',

//Modulo de autenticacion
auth:{
    register: '/auth/register',
    login: '/auth/login',
    logout: '/auth/logout',
    me: '/auth/me'
}

};