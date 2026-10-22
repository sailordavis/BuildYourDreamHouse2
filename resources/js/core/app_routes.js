export const AppRoutes = {

    // Direcciones de las interfaces
    routes: {

        // Página principal
        home: '/catalog/menu',

        // Módulo de Autenticación
        auth: {
            login: '/auth/login',
            register: '/auth/register'
        },

        // Módulo de Catálogo
        catalog: {
            menu: '/catalog/menu'
        },

        // Módulo Administrador
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
            this.navigate(this.routes.admin.dashboard);
        }

        // Cliente
        else if (Number(role) === 1) {
            this.navigate(this.routes.catalog.menu);
        }

        // Rol desconocido
        else {
            console.warn('Rol de usuario no reconocido');
            this.navigate(this.routes.auth.login);
        }
    },

    // Regresar al inicio de sesión
    goToLogin() {
        this.navigate(this.routes.auth.login);
    }

};
