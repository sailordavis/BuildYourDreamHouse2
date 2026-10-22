<?php

use Illuminate\Support\Facades\Route;

// Página principal del sistema
Route::redirect('/', '/catalog/menu');

// Módulo Auth
Route::prefix('auth')->group(function () {

    Route::view('/login', 'auth.login');
    Route::view('/register', 'auth.register');

});

// Módulo Catalog
Route::prefix('catalog')->group(function () {

    Route::view('/menu', 'catalog.menu');

});

// Módulo Admin
Route::prefix('admin')->group(function () {

    Route::view('/', 'admin.dashboard');

});
