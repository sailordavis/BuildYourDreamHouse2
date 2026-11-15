
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Build Your Dream House 2.0</title>

    <!-- Bootstrap 5 -->
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >

    <!-- Bootstrap Icons -->
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
        rel="stylesheet"
    >

    
    <!-- CSS y JavaScript específicos del catálogo -->
     @vite([
    'resources/css/catalog/catalog.css',
    'resources/js/catalog/catalog_menu.js'
     ])

     

    <!-- jQuery para las funciones existentes del catálogo -->
    <script
        src="https://code.jquery.com/jquery-3.7.1.min.js"
        integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
        crossorigin="anonymous"
    ></script>

    <!-- Conserva el comportamiento de los elementos ocultos -->
    <style>
        [hidden] {
            display: none !important;
        }
    </style>
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
            <!-- Contestar test -->
              <a href="/test/questionario"
             class="btn btn-outline-primary"
              id="BotonTest"
               title="Contestar test">
                <i class="bi bi-ui-checks"></i>
                 <span>Contestar test</span>
                 </a>
            <!-- Carrito de compra -->
                <a href="/cart" class="btn btn-outline-success" id ="BotonCarrito">
                   <i class="bi bi-cart-dash-fill"></i>
                </a>
                <!-- Cerrar sesion  -->
                <button id="logoutBtn" type="button" class="btn btn-danger">
                    <i class="bi bi-box-arrow-right"></i>
                </button>
            </div>

        </div>
    </nav>

    <!-- Catálogo de pinturas -->
    <main class="container-fluid">

        <section class="text-center mt-3" aria-labelledby="catalogTitle">

            <h1
                id="catalogTitle"
                class="d-flex justify-content-center align-items-center gap-3"
            >
                <i class="bi bi-paint-bucket" aria-hidden="true"></i>

                <span>Catalogo de Pinturas</span>

                <i
                    class="bi bi-paint-bucket"
                    style="transform: scaleX(-1);"
                    aria-hidden="true"
                ></i>
            </h1>

            <a
                class="btn btn-primary"
                data-bs-toggle="offcanvas"
                href="#offcanvasExample"
                role="button"
                aria-controls="offcanvasExample"
            >
                Encuentra tus pinturas ideales
            </a>

        </section>

        <!-- Panel lateral de categorías -->
        <div
            class="offcanvas offcanvas-start"
            tabindex="-1"
            id="offcanvasExample"
            aria-labelledby="offcanvasExampleLabel"
        >
            <div class="offcanvas-header">
                <h2 class="offcanvas-title fs-5" id="offcanvasExampleLabel">
                    Categorias
                </h2>

                <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="offcanvas"
                    aria-label="Cerrar"
                ></button>
            </div>

            <div class="offcanvas-body">

                <p style="margin-top: -22px;">
                    Encuentra todo tipo de pinturas; desde pinturas para
                    todo tipo de superficie hasta pinturas para cualquier
                    estilo decorativo.
                </p>

                <!-- Las opciones se generan con JavaScript -->
                <div id="Opciones"></div>

            </div>
        </div>

        <!-- Aquí se muestra el catálogo dinámico -->
        <section id="Pinturas" aria-label="Pinturas disponibles"></section>

    </main>

    <!-- Bootstrap JavaScript -->
    <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
    ></script>

</body>
</html>



