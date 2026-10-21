<?php

namespace App\Modules\Auth\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\ValidationException;
use App\Models\User;

class AuthController extends Controller
{
    // Inicio de sesión
    public function login(Request $request)
    {
        $request->validate([
            'email' => 'required|email',
            'password' => 'required|string'
        ]);

        $usuario = User::with('rol')
            ->where('email', $request->email)
            ->first();

        if (!$usuario || !Hash::check($request->password, $usuario->password)) {
            throw ValidationException::withMessages([
                'email' => ['Las credenciales son incorrectas.']
            ]);
        }

        // Generar token de autenticación
        $token = $usuario->createToken('auth_token')->plainTextToken;

        return response()->json([
            'mensaje' => 'Inicio de sesión exitoso',
            'token' => $token,
            'usuario' => $usuario
        ], 200);
    }

    // Consultar usuario autenticado
    public function me(Request $request)
    {
        $usuario = $request->user()->load('rol');

        return response()->json([
            'usuario' => $usuario
        ], 200);
    }

    // Cerrar sesión
    public function logout(Request $request)
    {
        // Eliminar el token utilizado
        $request->user()->currentAccessToken()->delete();

        return response()->json([
            'mensaje' => 'Sesión cerrada correctamente'
        ], 200);
    }

    
/**
 * Registro de nuevos usuarios
 */
public function register(Request $request)
{
    // Validación de los datos recibidos
    $request->validate([
        'name' => 'required|string|max:255',
        'email' => 'required|email|unique:users,email',
        'password' => 'required|string|min:8|confirmed'
    ]);

    // Buscar el rol cliente
    // Ajustar el nombre del campo según tu tabla rols
    $rolCliente = \App\Models\Rol::where('nombre', 'cliente')->firstOrFail();

    // Crear el usuario
    $usuario = User::create([
        'name' => $request->name,
        'email' => $request->email,
        'password' => $request->password,
        'rol_id' => $rolCliente->id
    ]);

    

    return response()->json([
        'mensaje' => 'Usuario registrado correctamente',
        'usuario' => $usuario->load('rol')
    ], 201);
}




}

