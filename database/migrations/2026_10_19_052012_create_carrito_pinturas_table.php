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
        Schema::create('carrito_pinturas', function (Blueprint $table) {
            $table->id();

            $table->foreignId('carrito_id')
            ->constrained('carritos')
            ->cascadeOnDelete();

            $table->foreignId('pintura_id')
            ->constrained('pinturas')
            ->restrictOnDelete();

            $table->unsignedInteger('cantidad')->default(1);

            $table->timestamps();

            $table->unique(['carrito_id','pintura_id']);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('carrito_pinturas');
    }
};
