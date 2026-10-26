<?php

use Illuminate\Support\Facades\Route;
use App\Modules\Catalog\Controllers\CatalogController;

Route::prefix('catalog')->group(function () {

    // Rutas públicas
    Route::post('/showProduct', [CatalogController::class, 'showProduct']);

});