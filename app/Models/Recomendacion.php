<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Recomendacion extends Model
{
    protected $table = 'recomendaciones';

    protected $fillable = [
        'resultado_id',
        'pintura_id',
        'puntuacion',
        'posicion',
    ];

    // Una recomendación pertenece a un resultado
    public function resultado(): BelongsTo
    {
        return $this->belongsTo(Resultado::class, 'resultado_id');
    }

    // Una recomendación corresponde a una pintura
    public function pintura(): BelongsTo
    {
        return $this->belongsTo(Pintura::class,'pintura_id');
    }
}
