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
        Schema::table('pinturas', function (Blueprint $table) {
            $table->string('acabado', 20)->nullable();

            $table->string('gama_color', 20)->nullable();

            $table->string('superficie', 40)->nullable();

            $table->string('eficiencia', 100)->nullable();

            $table->string('estilo_decorativo', 50)->nullable();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('pinturas', function (Blueprint $table) {
             $table->dropColumn([
                'acabado',
                'gama_color',
                'superficie',
                'eficiencia',
                'estilo_decorativo'
            ]);
        });
    }
};
