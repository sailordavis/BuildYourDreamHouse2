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
        Schema::create('pinturas', function (Blueprint $table) {
            $table->id();
            $table->string("nombre");
            $table->string("tipo");
            $table->string("color");
            $table->string("marca");
            $table->string("presentacion");
            $table->float("precio");
            $table->integer("stock");
            $table->text("descripcion");
            $table->string("imagen");
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('pinturas');
    }
};
