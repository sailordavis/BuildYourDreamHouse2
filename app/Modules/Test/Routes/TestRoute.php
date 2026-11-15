<?php

use Illuminate\Support\Facades\Route;
use App\Modules\Test\Controllers\TestController;

Route::prefix('test')->group(function (){

Route::middleware(['auth:sanctum','role:1'])->group(function () { //Rol cliente
Route::post('/procesarRespuestas', [TestController::class, 'procesarRespuestas']);
        
});



});