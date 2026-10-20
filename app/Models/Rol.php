<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Rol extends Model
{
     protected $table = 'rols';

    protected $fillable = [
        'nombre'
    ];

    /**
     * Un rol tiene muchos usuarios asignado a ese rol
     */
    public function usuarios(): HasMany
    {
        return $this->hasMany(User::class);
    }
}
