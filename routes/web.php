<?php

use Illuminate\Support\Facades\Route;

// Módulo Auth
Route::prefix('auth')->group(function () {

    Route::view('/login', 'auth.login');
    Route::view('/register', 'auth.register');

});

// Módulo Catalog
Route::prefix('catalog')->group(function () {

    Route::view('/', 'catalog.index');

});

// Módulo Admin
Route::prefix('admin')->group(function () {

    Route::view('/', 'admin.dashboard');

});
