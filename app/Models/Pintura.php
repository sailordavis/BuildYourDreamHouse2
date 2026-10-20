<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Pintura extends Model
{
    protected $table = 'pinturas';

    protected $fillable = [
        'nombre',
        'tipo',
        'color',
        'marca',
        'presentacion',
        'precio',
        'stock',
        'descripcion',
        'imagen',
    ];

    //Un producto puede estar agregado en muchos carritos 
    public function carritos(): BelongsToMany
    {
      return $this->belongsToMany(
        Carrito:: class,
        'carrito_pinturas',
        'pintura_id',
        'carrito_id'
      )->withPivot('cantidad');
    }
    

    //Un producto puede ser parte de muchas compras
    public function ventas(): BelongsToMany
    {
      return $this->belongsToMany(
        Venta:: class,
        'detalle_ventas',
        'pintura_id',
        'venta_id'
      )->withPivot('cantidad','precio_unitario','subtotal');
    }
    
    //Un producto puede ser parte de muchos resultados
    public function resultados(): BelongsToMany
    {
      return $this->belongsToMany(
        Resultado::class,
        'recomendaciones',
        'pintura_id',
        'resultado_id'
      )->withPivot('puntuacion','posicion');
    }
}
