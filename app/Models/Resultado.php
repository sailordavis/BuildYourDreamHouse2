<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Resultado extends Model
{
    protected $table = 'resultados';

    protected $fillable = [
        'usuario_id',
    ];

    // Un resultado pertenece a un usuario
    public function usuario(): BelongsTo
    {
        return $this->belongsTo(User::class, 'usuario_id');
    }

    // Un resultado puede recomendar muchas pinturas
    public function pinturas(): BelongsToMany
    {
        return $this->belongsToMany(
            Pintura::class,
            'recomendaciones',
            'resultado_id',
            'pintura_id'
        )->withPivot('puntuacion', 'posicion');
    }
    
    //Un resultado alberga muchas respuestas seleccionadas
    public function respuestas(): HasMany
    {
      return $this->hasMany(Respuesta:: class);
    }
}
