
import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import { bunny } from 'laravel-vite-plugin/fonts';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
    plugins: [
        laravel({
            input: [
                'resources/css/app.css',
                'resources/js/app.js',

                // Modulo de autenticacion
                'resources/js/auth/login.js',

                // Modulo de catalogo
                'resources/css/catalog/catalog.css',
                'resources/js/catalog/catalog_menu.js',

                // Modulo Test
                'resources/css/test/test.css',
                'resources/js/test/test.js',
            ],
            refresh: true,
            fonts: [
                bunny('Instrument Sans', {
                    weights: [400, 500, 600],
                }),
            ],
        }),
        tailwindcss(),
    ],
    server: {
        watch: {
            ignored: ['**/storage/framework/views/**'],
        },
    },
});
