<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('historial_busquedas', function (Blueprint $table) {
        $table->id();


        $table->foreignId('usuario_id')
            ->constrained('users')
            ->restrictOnDelete();

        $table->string('categoria');
        $table->string('subcategoria');

        $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('historial_busquedas');
    }
};
