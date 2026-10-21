<?php

namespace App\Models;


use Illuminate\Database\Eloquent\Model;
use Database\Factories\UserFactory;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Attributes\Hidden;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Relations\HasOne;

// Importación necesaria para utilizar tokens de Sanctum
use Laravel\Sanctum\HasApiTokens;

#[Fillable(['name', 'email', 'password', 'rol_id'])]
#[Hidden(['password', 'remember_token'])]
class User extends Authenticatable
{
    /** @use HasFactory<UserFactory> */
    use HasApiTokens, HasFactory, Notifiable;

    /**
     * Conversión de atributos
     */
    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',
        ];
    }

    /**
     * Un usuario pertenece a un rol
     */
    public function rol(): BelongsTo
    {
        return $this->belongsTo(Rol::class);
    }

    /**
     * Un usuario tiene un carrito
     */
    public function carrito(): HasOne
    {
        return $this->hasOne(Carrito::class, 'usuario_id');
    }

    /**
     * Un usuario puede realizar muchas ventas
     */
    public function ventas(): HasMany
    {
        return $this->hasMany(Venta::class, 'usuario_id');
    }

    /**
     * Un usuario puede tener muchos registros de búsquedas
     */
    public function historialBusquedas(): HasMany
    {
        return $this->hasMany(Historial_Busqueda::class, 'usuario_id');
    }

    /**
     * Un usuario puede tener muchos resultados de tests
     */
    public function resultadosTest(): HasMany
    {
        return $this->hasMany(Resultado::class, 'usuario_id');
    }
}
