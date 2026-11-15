
import { ApiConfig } from '../core/api_config.js';
import { HttpClient } from '../core/http_client.js';
import { TokenStorage } from '../core/token_storage.js';
import { AppRoutes } from '../core/app_routes.js';

// Estado del test
let preguntas = [];
let datosRecopilados = [];
let preguntaActual = null;
let datosGuia = null;

// Inicializar el test cuando cargue el HTML
document.addEventListener('DOMContentLoaded', async () => {
    await cargarPreguntas();
});

// Cargar las preguntas desde public
async function cargarPreguntas() {
    try {
        const response = await fetch('/json/dato.json');

        if (!response.ok) {
            throw new Error('No se pudo cargar el JSON de preguntas');
        }

        preguntas = await response.json();

        // Mostrar la primera pregunta
        mostrarPregunta(1);

    } catch (error) {
        console.error('Error al cargar las preguntas:', error);
    }
}

// Mostrar una pregunta por su ID
function mostrarPregunta(idPregunta) {
    const pregunta = preguntas.find(
        p => Number(p.id) === Number(idPregunta)
    );

    if (!pregunta) {
        console.error('No se encontró la pregunta:', idPregunta);
        return;
    }

    preguntaActual = pregunta;

    const contenedor = document.getElementById('Preguntas');

    if (!contenedor) {
        console.error('No existe el contenedor #Preguntas');
        return;
    }

    // Insertar el contenido HTML de la pregunta
    contenedor.innerHTML = pregunta.contenido;
}

// Manejar las selecciones y el botón de regreso.
// Se registra una sola vez para evitar eventos duplicados.
document.addEventListener('change', event => {
    const input = event.target;

    if (
        !input.matches('#Preguntas input[type="radio"]') ||
        !preguntaActual
    ) {
        return;
    }

    const valorSeleccionado = input.value;
    const pregunta = preguntaActual;

    // Guardar o actualizar la respuesta seleccionada
    recopilarDatos(pregunta.id, valorSeleccionado);

    const opcion = pregunta.opciones.find(
        o => String(o.value) === String(valorSeleccionado)
    );

    if (!opcion) {
        console.error('No se encontró la opción seleccionada');
        return;
    }

    // Comprobar si el test ha finalizado
    if (Number(opcion.siguiente) === 117) {
        mostrarAvisoFinal();
        return;
    }

    if (opcion.siguiente != null) {
        // Registrar la pregunta anterior para poder regresar
        asignarPadre(opcion.siguiente, pregunta.id);

        // Mostrar la siguiente pregunta
        mostrarPregunta(opcion.siguiente);
    } else {
        console.error('La opción no tiene una pregunta siguiente');
    }
});

// Navegación hacia atrás mediante delegación de eventos
document.addEventListener('click', event => {
    const botonRegreso = event.target.closest('#botonRegreso');

    if (!botonRegreso || !preguntaActual) {
        return;
    }

    const idAnterior = preguntaActual.anterior;

    if (idAnterior == null) {
        return;
    }

    // Eliminar la respuesta de la pregunta que se abandona
    eliminarRespuesta(preguntaActual.id);

    mostrarPregunta(idAnterior);
});

// Asignar la pregunta anterior
function asignarPadre(idActual, idAnterior) {
    const pregunta = preguntas.find(
        p => Number(p.id) === Number(idActual)
    );

    if (pregunta) {
        pregunta.anterior = idAnterior;
    }
}

// Recopilar las respuestas necesarias para el servicio
function recopilarDatos(idPregunta, opcion) {
    // Mantener la exclusión de las preguntas originales
    switch (Number(idPregunta)) {
        case 1:
        case 4:
        case 5:
        case 6:
            return;
    }

    // Actualizar si la pregunta ya tenía una respuesta
    const indice = datosRecopilados.findIndex(
        dato => Number(dato.id) === Number(idPregunta)
    );

    const respuesta = {
        id: Number(idPregunta),
        opcion: opcion
    };

    if (indice !== -1) {
        datosRecopilados[indice] = respuesta;
    } else {
        datosRecopilados.push(respuesta);
    }
}

// Eliminar la respuesta de una pregunta al retroceder
function eliminarRespuesta(idPregunta) {
    datosRecopilados = datosRecopilados.filter(
        dato => Number(dato.id) !== Number(idPregunta)
    );
}

// Mostrar el aviso de finalización
function mostrarAvisoFinal() {
    // Compatible con el modal de Bootstrap 5
    const modalElemento = document.getElementById('aviso_final');

    if (modalElemento && window.bootstrap?.Modal) {
        window.bootstrap.Modal
            .getOrCreateInstance(modalElemento)
            .show();
    } else {
        // Alternativa si el aviso no utiliza un modal de Bootstrap
        console.warn('No se encontró el modal o Bootstrap Modal');
    }
}

// Enviar las respuestas a Laravel
async function mostrarResultados() {


    // Verificar si existe un token de autenticación
    if (!TokenStorage.hasToken()) {
        alert('Debes iniciar sesión para contestar el test.');
        AppRoutes.navigate(AppRoutes.routes.home);
        return;
    }

    if (datosRecopilados.length === 0) {
        alert('No hay respuestas para enviar.');
        return;
    }

    try {
        console.log('Respuestas enviadas:', datosRecopilados);

        // ApiConfig.test.respuestas debe apuntar al endpoint Laravel
        const respuesta = await HttpClient.post(
            ApiConfig.test.procesarRespuestas,
            {
                datos: datosRecopilados
            }
        );
      
        datosGuia = respuesta;

        // Cerrar el modal de finalización
        const modalElemento = document.getElementById('aviso_final');

        if (modalElemento && window.bootstrap?.Modal) {
            window.bootstrap.Modal
                .getOrCreateInstance(modalElemento)
                .hide();
        }

        // Mostrar los datos recibidos del servicio
        console.log('VariablesEntrada:', datosGuia);

        // Todavía no se generan recomendaciones.
        // Aquí podrás conectar posteriormente la interfaz de resultados.

    } catch (error) {
        console.error('Error al enviar las respuestas:', error);
        alert('No fue posible procesar las respuestas del test.');
        console.error('Detalle del error:', error.message);
    }
}

//Funcion que se activa al presionar el boton continuar
//Elimina el ultimo dato recopilado
function eliminarUltimoDato() {
    datosRecopilados.pop();
}

// Permitir que los botones HTML existentes invoquen estas funciones
window.MostrarResultados = mostrarResultados;
window.EliminarUltimoDato = eliminarUltimoDato;
