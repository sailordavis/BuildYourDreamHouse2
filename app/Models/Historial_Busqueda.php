<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Historial_Busqueda extends Model
{
    protected $table = 'historial_busquedas';

    protected $fillable = [
        'usuario_id',
        'categoria',
        'subcategoria',
    ];
    
    //Una registro de busqueda pertenece a un usuario 
     public function usuario(): BelongsTo
    {
        return $this->belongsTo(User::class, 'usuario_id');
    }
}
