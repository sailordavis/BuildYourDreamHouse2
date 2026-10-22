
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Iniciar sesión - Build Your Dream House 2.0</title>

    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          rel="stylesheet">

    <!-- Estilos del módulo Auth -->
    @vite('resources/css/auth/auth.css')
</head>

<body class="bg-light">

    <div class="container min-vh-100 d-flex justify-content-center align-items-center">

        <div class="card shadow p-4" style="width: 100%; max-width: 420px;">

            <div class="card-body">

                <h3 class="text-center mb-3">
                    Build Your Dream House 2.0
                </h3>

                <h5 class="text-center text-muted mb-4">
                    Iniciar sesión
                </h5>

                <!-- Formulario Login -->
                <form id="loginForm">

                    <div class="mb-3">
                        <label for="email" class="form-label">
                            Correo electrónico
                        </label>

                        <input type="email"
                               class="form-control"
                               id="email"
                               name="email"
                               placeholder="Ingresa tu correo"
                               required>
                    </div>

                    <div class="mb-3">
                        <label for="password" class="form-label">
                            Contraseña
                        </label>

                        <input type="password"
                               class="form-control"
                               id="password"
                               name="password"
                               placeholder="Ingresa tu contraseña"
                               required>
                    </div>

                    <button type="submit" class="btn btn-primary w-100">
                        Iniciar sesión
                    </button>

                </form>

                <hr class="my-4">

                <p class="text-center mb-2">
                    ¿Todavía no tienes una cuenta?
                </p>

                <!-- Navegación al registro -->
                <a href="{{ url('/auth/register') }}"
                   class="btn btn-outline-secondary w-100">
                    Crear cuenta
                </a>

            </div>

        </div>

    </div>

</body>
</html>
