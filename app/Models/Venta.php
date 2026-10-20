<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Venta extends Model
{
    protected $table = 'ventas';

    protected $fillable = [
        'usuario_id',
        'metodo_pago',
        'total',
    ];
    
    //Una venta es realizada por un usuario 
    public function usuario(): BelongsTo
    {
      return $this->belongsTo(User:: class,
      'usuario_id');
    }

    //Una venta puede albergar muchas pinturas
    public function pinturas(): BelongsToMany
    {
      return $this->belongsToMany(
        Pintura:: class,
        'detalle_ventas',
        'venta_id',
        'pintura_id'
      )->withPivot('cantidad','precio_unitario','subtotal');
    }
}
