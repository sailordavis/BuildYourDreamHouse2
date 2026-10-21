
<?php

namespace App\Modules\Auth\Controllers;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;

class AuthController extends Controller
{
    // Registro de usuarios
    public function register(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|max:255|unique:users,email',
            'password' => 'required|string|min:8|confirmed',
        ]);

        $usuario = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);

        // Iniciar sesión después del registro
        Auth::login($usuario);

        $request->session()->regenerate();

        return redirect('/inicio');
    }

    // Inicio de sesión
    public function login(Request $request)
    {
        $credenciales = $request->validate([
            'email' => 'required|email',
            'password' => 'required|string',
        ]);

        if (!Auth::attempt($credenciales)) {
            return back()
                ->withErrors([
                    'email' => 'Las credenciales son incorrectas.',
                ])
                ->onlyInput('email');
        }

        // Prevenir la fijación de sesión
        $request->session()->regenerate();

        return redirect()->intended('/inicio');
    }

    // Cierre de sesión
    public function logout(Request $request)
    {
        Auth::logout();

        $request->session()->invalidate();
        $request->session()->regenerateToken();

        return redirect('/login');
    }

    // Consultar al usuario autenticado
    public function me(Request $request)
    {
        return response()->json([
            'usuario' => $request->user(),
        ]);
    }
}
