<?php

use Illuminate\Support\Facades\Route;

// Página principal del sistema
Route::redirect('/', '/catalog/menu');

// Modulo Auth
Route::prefix('auth')->group(function () {

    Route::view('/login', 'auth.login');
    Route::view('/register', 'auth.register');

});

// Modulo Catalog
Route::prefix('catalog')->group(function () {

    Route::view('/menu', 'catalog.menu');

});

//Modulo Test
Route::prefix('test')->group(function () {
    Route::view('/questionario', 'test.questionario');
});

// Módulo Admin
Route::prefix('admin')->group(function () {

    Route::view('/', 'admin.dashboard');

});
