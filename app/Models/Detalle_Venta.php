<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Detalle_Venta extends Model
{
    protected $table = 'detalle_ventas';

    protected $fillable = [
        'venta_id',
        'pintura_id',
        'cantidad',
        'precio_unitario',
        'subtotal',
    ];

    // Un detalle pertenece a una venta
    public function venta(): BelongsTo
    {
        return $this->belongsTo(Venta::class, 'venta_id');
    }

    // Un detalle corresponde a una pintura
    public function pintura(): BelongsTo
    {
        return $this->belongsTo(Pintura::class, 'pintura_id');
    }
}
