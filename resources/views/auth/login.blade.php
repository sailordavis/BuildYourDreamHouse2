
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iniciar sesión</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

    @vite('resources/js/auth/login.js')
</head>
<body>

    <div class="container mt-5">
        <div class="card shadow mx-auto" style="max-width: 400px;">
            <div class="card-body">

                <h3 class="text-center mb-4">Iniciar sesión</h3>

                <form id="loginForm">

                    <div class="mb-3">
                        <label class="form-label">Correo electrónico</label>
                        <input type="email" id="email"
                               class="form-control" required>
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Contraseña</label>
                        <input type="password" id="password"
                               class="form-control" required>
                    </div>

                    <button type="submit" class="btn btn-primary w-100">
                        Iniciar sesión
                    </button>

                </form>

                <p id="loginError" class="text-danger mt-3" hidden></p>

                <a href="/catalog/menu" class="d-block text-center mt-3">
                    Regresar al catálogo
                </a>

            </div>
        </div>
    </div>

</body>
</html>

