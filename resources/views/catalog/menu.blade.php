
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Build Your Dream House 2.0</title>

    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">

    <style>
        [hidden] {
            display: none !important;
        }
    </style>
    <!-- CSS con Vite -->
    @vite('resources/css/catalog/catalog.css'),
    <!-- JavaScript con Vite -->
    @vite('resources/js/catalog/catalog_menu.js')

</head>
<body>

    <!-- Barra de navegación -->
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


    <!-- Catálogo de pinturas -->
    <main class="container mt-5">

        <div class="text-center">

            <h1 class="d-flex justify-content-center align-items-center gap-3">

                <i class="bi bi-paint-bucket"></i>

                Catálogo de Pinturas

                <i class="bi bi-paint-bucket"
                   style="transform: scaleX(-1);"></i>

            </h1>

            <p class="mt-3">
                Encuentra la pintura ideal para tu hogar.
            </p>

            <!-- Botón de clasificación -->
            <button class="btn btn-primary mt-2"
                    type="button"
                    data-bs-toggle="offcanvas"
                    data-bs-target="#offcanvasCategorias">

                Encuentra tus pinturas ideales

            </button>

        </div>

        <!-- Contenedor de pinturas -->
        <div id="Pinturas" class="mt-5">

            <!-- Aquí JavaScript mostrará las pinturas -->

        </div>

    </main>


    <!-- Offcanvas de categorías -->
    <div class="offcanvas offcanvas-start"
         tabindex="-1"
         id="offcanvasCategorias"
         aria-labelledby="offcanvasCategoriasLabel">

        <div class="offcanvas-header">

            <h5 class="offcanvas-title"
                id="offcanvasCategoriasLabel">

                Categorías

            </h5>

            <button type="button"
                    class="btn-close"
                    data-bs-dismiss="offcanvas"
                    aria-label="Cerrar">
            </button>

        </div>

        <div class="offcanvas-body">

            <p>
                Encuentra todo tipo de pinturas,
                desde pinturas para diferentes superficies
                hasta pinturas para cualquier estilo decorativo.
            </p>

            <!-- Contenedor de categorías y submódulos -->
            <div id="Opciones">

                <!-- Aquí JavaScript generará las categorías -->

            </div>

        </div>

    </div>


    <!-- Bootstrap JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>


