<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Carrito_Pintura extends Model
{
    protected $table = 'carrito_pinturas';

    protected $fillable = [
        'carrito_id',
        'pintura_id',
        'cantidad',
    ];

    // Un registro pertenece a un carrito
    public function carrito(): BelongsTo
    {
        return $this->belongsTo(Carrito::class, 'carrito_id');
    }

    // Un registro corresponde a una pintura
    public function pintura(): BelongsTo
    {
        return $this->belongsTo(Pintura::class, 'pintura_id');
    }
}
