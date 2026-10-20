<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Respuesta extends Model
{
    protected $table = 'respuestas';

    protected $fillable = [
        'resultado_id',
        'num_pregunta',
        'opcion_value',
    ];
    

    //Una respuesta seleccionada pertenece a un resultado 
    public function resultado(): BelongsTo
    {
        return $this->belongsTo(Resultado:: class);
    }

}
