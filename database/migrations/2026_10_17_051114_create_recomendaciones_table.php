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
        Schema::create('recomendaciones', function (Blueprint $table) {
            $table->id();

            $table->foreignId('resultado_id')
            ->constrained('resultados')
            ->restrictOnDelete();

            $table->foreignId('pintura_id')
           ->constrained('pinturas')
            ->restrictOnDelete();

            $table->decimal('puntuacion', 8, 4);
            $table->integer("posicion");

            $table->timestamps();
            $table->unique(['resultado_id', 'pintura_id']);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('recomendaciones');
    }
};
