<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Carrito extends Model
{
    protected $fillable = [
        'usuario_id',
    ];
    

    //Un carrito pertenece a un usuario 
    public function usuario(): BelongsTo
    {
        return $this->belongsTo(User::class,'usuario_id');
    }


    //Un carrito puede almacenar muchas pinturas
    public function pinturas(): BelongsToMany
    {
      return $this->belongsToMany(
        Pintura:: class,
        'carrito_pinturas',
        'carrito_id',
        'pintura_id'
      )->withPivot('cantidad');
    }

}
