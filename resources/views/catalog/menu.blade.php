
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Build Your Dream House 2.0</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        [hidden] {
            display: none !important;
        }
    </style>

    <!-- JavaScript con Vite -->
    @vite('resources/js/catalog/catalog_menu.js')

</head>
<body>

    <nav class="navbar bg-light shadow-sm">
        <div class="container">

            <a class="navbar-brand" href="/catalog/menu">
                Build Your Dream House 2.0
            </a>

            <!-- Opciones de visitante -->
            <div id="guestMenu" class="d-flex gap-2" hidden>

                <a href="/auth/login" class="btn btn-outline-primary">
                    Iniciar sesión
                </a>

                <a href="/auth/register" class="btn btn-primary">
                    Registrarse
                </a>

            </div>

            <!-- Opciones de cliente -->
            <div id="clientMenu" class="d-flex gap-2" hidden>

                <a href="/cart" class="btn btn-outline-success">
                    Mi carrito
                </a>

                <button id="logoutBtn" class="btn btn-danger">
                    Cerrar sesión
                </button>

            </div>

        </div>
    </nav>

    <main class="container mt-5">
        <h2>Catálogo de pinturas</h2>
        <p>Encuentra la pintura ideal para tu hogar.</p>
    </main>

</body>
</html>

