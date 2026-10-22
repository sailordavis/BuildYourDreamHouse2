
export const AppRoutes = {

    // Direcciones de las interfaces
    routes: {
        //Modulo de Autenticacion
        auth: {
            login: '/auth/login',
            register: '/auth/register'
        },
        //Modulo de Catalogo
        catalog: {
            index: '/catalog'
        },

        admin: {
            dashboard: '/admin'
        }
    },

    // Navegar hacia una interfaz
    navigate(route) {
        window.location.href = route;
    },

    // Redirigir según el rol del usuario
    redirectByRole(role) {

        // Administrador
        if (Number(role) === 3) {
            this.navigate(this.routes.admin);
        }

        // Cliente
        else if (Number(role) === 1) {
            this.navigate(this.routes.catalog);
        }

        // Rol desconocido
        else {
            console.warn('Rol de usuario no reconocido');
            this.navigate(this.routes.login);
        }
    },

    // Regresar al inicio de sesión
    goToLogin() {
        this.navigate(this.routes.login);
    }

};
