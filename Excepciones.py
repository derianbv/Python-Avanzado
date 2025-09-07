############################################ Manejo de excepciones ############################################################3
#Es como decirle a python que si llega a haber un error de ejecución que lo pase, solo maneja errores de lógica y no de sintasis. 

def divir_por_cero(a,b): 
  return a/b #perfectamente escrito

divir_por_cero(1/0) 

'''
Me suelta el error:  

Traceback (most recent call last):
  File "/tmp/main.py", line 2, in <module>
    import user_code
  File "/tmp/user_code.py", line 4, in <module>
    divir_por_cero(1/0) 
                   ~^~
ZeroDivisionError: division by zero

'''
#Ahora, esperando algun error de ejecución lo puedo pasar con uno o varios except: 

def division(a,b): ES COMO PONER ALERTAS O GRITOS EN EL CIELO (EN LA FUNCION LLAMADA) Y TENER ACCOUNTABILITY DE QUE ALGO PUEDE SALIR MAL, PARA MANEJARLO EN LA FUNCION LAMADORA.
  try: 
    return a/b 
  except ZeroDivisionError: #Como hay error hace este bloque y no el de arriba, esta es una de los errores predeterminados de python, si pongo uno que no existe habrá error de suntaxis en el código 
    print('Eso está mal')
    return (ZeroDivisionError) 
  finally: #este es un codigo que le digo, hazte sí o si siempre con finally, así el except tenga un return 
    print('yo no me ecutaré porque el except me saca de la función')

division(1,0) #Así este mal por logica, el código va a hacer una excepsion, pueden ser más de una. 


print("El codigo finalizo sin errores que me detuvieran")

'''
Eso está mal
yo no me ecutaré porque el except me saca de la función
El codigo finalizo sin errores que me detuvieran

[Execution complete with exit code 0]
'''

################################ Raise y Clase Exception #######################################################################################


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero, this is imposible")  # El raise sirve para prever errores de logica creando mi codigo, acá le setee, si alguien trata de poner un cero que el programa raise un error de una 
    return a / b


############### Puedo ponerle un error personalizado al crearlo en la clase: -----------------------------------------------



#Acá hago una clase que herede de Exception: 

class DivisionPorCeroError(Exception):
    """Excepción personalizada para manejar la división por cero."""
    def __init__(self, message="El divisor no puede ser cero"):
        self.message = message
        super().__init__(self.message)

# Función que utiliza la excepción personalizada
def division(a, b): 
    if b == 0:  # Verificamos el divisor
        raise DivisionPorCeroError("¡Intentaste dividir entre cero!")  # Lanzamos el error personalizado
    return a / b


# 🚨 Tutorial Completo: Manejo de Excepciones en Python y Java -------------------------------------------------------------------------------------------------------

## 🎯 ¿Qué vas a aprender?
Este tutorial te enseñará desde lo más básico hasta técnicas avanzadas para manejar situaciones inesperadas en tu código como un programador profesional. Empezaremos con conceptos simples y construiremos hacia casos más complejos.

---

## 📚 PARTE 1: ¿Qué es una Excepción?

### 🤔 Concepto Fundamental
Una excepción es como una señal de alarma que tu programa envía cuando algo inesperado sucede. Es la manera civilizada de decir "¡Houston, tenemos un problema!" en lugar de que tu programa simplemente explote sin explicación.

**Piensa en esto:** Es como cuando tu auto detecta un problema y prende una luz específica en el tablero. No se detiene inmediatamente, pero te avisa exactamente qué está mal para que puedas decidir qué hacer.

### 🔥 El problema con ignorar situaciones inesperadas:
```python
# ❌ MAL: Ignorar problemas
def dividir_mal(a, b):
    return a / b  # ¿Qué pasa si b es 0?

resultado = dividir_mal(10, 0)  # ¡BOOM! 💥 ZeroDivisionError
```

### ✅ La solución profesional:
```python
# ✅ BIEN: Manejar el problema adecuadamente
def dividir_bien(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

try:
    resultado = dividir_bien(10, 0)
except ValueError as error:
    print(f"Situación controlada: {error}")
    resultado = None
```

---

## 🛑 PARTE 2: ¿Qué hace REALMENTE `raise`? (¡La Pregunta Clave!)

### 🚨 SÍ, `raise` funciona exactamente como `return` en términos de flujo

Esta es una comprensión fundamental que muchos tutoriales no explican claramente: **`raise` detiene la ejecución de la función inmediatamente**, tal como lo hace `return`. La diferencia es QUÉ envía de vuelta al código que llamó la función.

```python
def ejemplo_flujo_raise():
    print("🚀 Inicio de la función")
    
    edad = -5
    if edad < 0:
        print("⚠️ Problema detectado, preparando raise...")
        raise ValueError("Edad no puede ser negativa")  # ⬅️ ¡AQUÍ SE DETIENE TODO!
        
    # ❌ ESTAS LÍNEAS NUNCA SE EJECUTAN
    print("✅ Edad validada correctamente")
    return "Usuario creado exitosamente"

# Llamamos la función
try:
    resultado = ejemplo_flujo_raise()
    print(f"Resultado: {resultado}")  # Esto tampoco se ejecuta
except ValueError as problema:
    print(f"🛑 Función se detuvo por: {problema}")

# Salida:
# 🚀 Inicio de la función  
# ⚠️ Problema detectado, preparando raise...
# 🛑 Función se detuvo por: Edad no puede ser negativa
```

### 🔄 Comparación Directa: `return` vs `raise`

```python
def funcion_con_return():
    print("Ejecutando línea 1")
    if True:
        print("Ejecutando línea 2")
        return "Todo salió bien"  # ⬅️ DETIENE aquí y envía un valor
        
    # ❌ Esta línea nunca se ejecuta
    print("Esta línea nunca se ejecuta")

def funcion_con_raise():
    print("Ejecutando línea 1") 
    if True:
        print("Ejecutando línea 2")
        raise ValueError("Algo salió mal")  # ⬅️ DETIENE aquí y envía una excepción
        
    # ❌ Esta línea nunca se ejecuta
    print("Esta línea nunca se ejecuta")

# Ambas funciones se comportan igual en términos de flujo:
# - Ejecutan hasta el punto de return/raise
# - Se detienen inmediatamente
# - Envían algo de vuelta (valor vs excepción)
```

### 🎯 La Diferencia Clave en el Destino

La diferencia no está en CUÁNDO se detiene la función (ambos lo hacen inmediatamente), sino en ADÓNDE va lo que envían:

```python
def procesar_usuario(edad):
    if edad < 0:
        # raise envía la excepción al bloque except más cercano
        raise ValueError(f"Edad {edad} es inválida")
        
    # return envía el valor directamente a quien llamó la función    
    return f"Usuario con {edad} años procesado"

# El código que llama decide dónde va cada cosa:
try:
    # Si la función hace return, el valor va aquí ⬇️
    resultado = procesar_usuario(25)
    print(f"Éxito: {resultado}")
    
except ValueError as problema:
    # Si la función hace raise, la excepción va aquí ⬇️
    print(f"Problema manejado: {problema}")
```

---

## 🐍 PARTE 3: Python - Manejo de Excepciones

### 🏗️ Estructura Básica: Tu Red de Seguridad
```python
try:
    # Código que podría lanzar una excepción
    operacion_peligrosa()
    print("✅ Operación completada sin problemas")
    
except TipoDeExcepcion as variable_excepcion:
    # Se ejecuta SOLO si se lanzó ese tipo específico de excepción
    print(f"🛠️ Manejando problema específico: {variable_excepcion}")
    
else:
    # Se ejecuta SOLO si NO se lanzó ninguna excepción
    print("🎉 Todo salió perfectamente")
    
finally:
    # Se ejecuta SIEMPRE, haya excepción o no
    print("🔄 Limpiando recursos...")
```

### 📝 Ejemplo Paso a Paso: Viendo el Flujo en Acción
```python
def procesar_edad_detallado():
    print("🔍 Iniciando procesamiento de edad...")
    
    try:
        edad_texto = input("Ingresa tu edad: ")
        print(f"📝 Recibido: '{edad_texto}'")
        
        # Esta línea puede lanzar ValueError si no es un número
        edad = int(edad_texto)  
        print(f"🔢 Convertido a número: {edad}")
        
        # Estas validaciones pueden lanzar ValueError con nuestros mensajes
        if edad < 0:
            print("⚠️ Detectada edad negativa, lanzando excepción...")
            raise ValueError("La edad no puede ser negativa")
            # ⬅️ Si llega aquí, la función se DETIENE inmediatamente
            
        if edad > 120:
            print("⚠️ Detectada edad excesiva, lanzando excepción...")
            raise ValueError("¿En serio tienes más de 120 años? 🤨")
            # ⬅️ Si llega aquí, la función se DETIENE inmediatamente
            
    except ValueError as problema:
        # Llegamos aquí si cualquier raise ValueError fue ejecutado
        print(f"🛑 Excepción capturada: {problema}")
        
        if "invalid literal" in str(problema):
            print("💡 Consejo: Asegúrate de ingresar solo números")
        else:
            print("💡 Consejo: Verifica que la edad sea realista")
            
        return None  # Terminamos la función devolviendo None
        
    else:
        # Solo llegamos aquí si NO se lanzó ninguna excepción
        print(f"✅ Edad válida procesada: {edad}")
        return edad
        
    finally:
        # Siempre llegamos aquí, haya excepción o no
        print("🏁 Procesamiento finalizado")

# Probemos diferentes casos para ver el flujo:
print("=== Caso 1: Edad válida ===")
resultado1 = procesar_edad_detallado()  # Ingresa: 25
print(f"Resultado: {resultado1}")

print("\n=== Caso 2: Edad inválida ===") 
resultado2 = procesar_edad_detallado()  # Ingresa: -5
print(f"Resultado: {resultado2}")
```

### 🎯 Capturar Múltiples Tipos de Problemas
```python
def leer_archivo_inteligente(nombre_archivo):
    """
    Esta función demuestra cómo manejar diferentes tipos de problemas
    que pueden ocurrir al trabajar con archivos
    """
    print(f"📁 Intentando leer archivo: {nombre_archivo}")
    
    try:
        # Cada una de estas operaciones puede fallar de manera diferente
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print("✅ Archivo leído exitosamente")
            
            # Intentamos procesar como JSON
            import json
            datos = json.loads(contenido)
            print("✅ JSON procesado exitosamente")
            return datos
            
    except FileNotFoundError:
        # Se lanza cuando el archivo no existe
        print(f"❌ El archivo '{nombre_archivo}' no fue encontrado")
        print("💡 Verifica que el nombre y la ruta sean correctos")
        return None
        
    except PermissionError:
        # Se lanza cuando no tenemos permisos para leer el archivo
        print(f"🔒 No tienes permisos para leer '{nombre_archivo}'")
        print("💡 Contacta al administrador del sistema")
        return None
        
    except json.JSONDecodeError as error_json:
        # Se lanza cuando el archivo existe pero no es JSON válido
        print(f"📄 El archivo no contiene JSON válido")
        print(f"🔍 Error específico: {error_json}")
        print("💡 Verifica el formato del archivo")
        return None
        
    except UnicodeDecodeError:
        # Se lanza cuando el archivo tiene codificación incompatible
        print(f"🔤 Problema de codificación en el archivo")
        print("💡 El archivo podría estar en una codificación diferente")
        return None
        
    except Exception as error_inesperado:
        # Captura cualquier otro problema que no anticipamos
        print(f"💥 Ocurrió un problema inesperado: {error_inesperado}")
        print("💡 Por favor reporta este error")
        return None

# Ejemplos de uso
datos = leer_archivo_inteligente("configuracion.json")
if datos:
    print("🎉 Datos cargados correctamente:", datos)
else:
    print("😔 No se pudieron cargar los datos")
```

### 🚀 Crear Tus Propias Excepciones Personalizadas

```python
# Definimos nuestras excepciones personalizadas para comunicar problemas específicos
class ExcepcionValidacion(Exception):
    """Clase base para todas nuestras excepciones de validación"""
    def __init__(self, mensaje, valor_problematico=None):
        super().__init__(mensaje)
        self.valor_problematico = valor_problematico

class EdadNegativaException(ExcepcionValidacion):
    """Se lanza cuando detectamos una edad negativa"""
    def __init__(self, edad):
        mensaje = f"La edad {edad} es negativa, lo cual es imposible"
        super().__init__(mensaje, edad)
        self.edad = edad

class EdadExcesivaException(ExcepcionValidacion):  
    """Se lanza cuando detectamos una edad irrealmente alta"""
    def __init__(self, edad):
        mensaje = f"La edad {edad} parece irreal (mayor a 120 años)"
        super().__init__(mensaje, edad)
        self.edad = edad

def validar_edad_profesional(edad):
    """
    Valida edad y lanza excepciones específicas según el problema detectado.
    Nota: Esta función se DETIENE inmediatamente cuando hace raise.
    """
    print(f"🔍 Validando edad: {edad}")
    
    # Verificar tipo de dato
    if not isinstance(edad, int):
        print(f"❌ Tipo incorrecto detectado: {type(edad)}")
        # La función se DETIENE aquí si el tipo está mal
        raise TypeError(f"La edad debe ser un número entero, no {type(edad)}")
    
    # Verificar rango negativo
    if edad < 0:
        print(f"❌ Edad negativa detectada: {edad}")
        # La función se DETIENE aquí si la edad es negativa  
        raise EdadNegativaException(edad)
    
    # Verificar rango excesivo
    if edad > 120:
        print(f"❌ Edad excesiva detectada: {edad}")
        # La función se DETIENE aquí si la edad es muy alta
        raise EdadExcesivaException(edad)
    
    # Si llegamos hasta aquí, significa que todas las validaciones pasaron
    print(f"✅ Edad {edad} es válida")
    return True

def registrar_usuario_completo(nombre, edad):
    """
    Demuestra cómo el código que llama puede manejar diferentes tipos de problemas
    que se comunican desde las funciones de validación
    """
    print(f"👤 Intentando registrar usuario: {nombre}, {edad} años")
    
    try:
        # Intentamos validar la edad
        validar_edad_profesional(edad)
        
        # Si llegamos aquí, la validación fue exitosa
        print(f"🎉 Usuario {nombre} registrado exitosamente")
        return {"exito": True, "usuario": nombre, "edad": edad}
        
    except EdadNegativaException as problema_negativo:
        print(f"🔧 Manejando edad negativa: {problema_negativo}")
        print("💡 Sugerencia: ¿Olvidaste el signo menos?")
        return {"exito": False, "razon": "edad_negativa", "sugerencia": "Revisa el signo"}
        
    except EdadExcesivaException as problema_excesivo:
        print(f"🔧 Manejando edad excesiva: {problema_excesivo}")
        print("💡 Sugerencia: Verifica que la edad sea correcta")
        return {"exito": False, "razon": "edad_excesiva", "sugerencia": "Verifica la edad"}
        
    except TypeError as problema_tipo:
        print(f"🔧 Manejando tipo incorrecto: {problema_tipo}")
        print("💡 Sugerencia: Asegúrate de usar un número entero")
        return {"exito": False, "razon": "tipo_incorrecto", "sugerencia": "Usa números enteros"}

# Ejemplos que demuestran el flujo completo
print("=== Prueba 1: Caso exitoso ===")
resultado1 = registrar_usuario_completo("Ana", 25)
print(f"Resultado: {resultado1}\n")

print("=== Prueba 2: Edad negativa ===")
resultado2 = registrar_usuario_completo("Luis", -30)
print(f"Resultado: {resultado2}\n")

print("=== Prueba 3: Edad excesiva ===")
resultado3 = registrar_usuario_completo("Carmen", 150)
print(f"Resultado: {resultado3}\n")

print("=== Prueba 4: Tipo incorrecto ===")
resultado4 = registrar_usuario_completo("Pedro", "treinta")
print(f"Resultado: {resultado4}")
```

---

## ☕ PARTE 4: Java - La Misma Lógica, Sintaxis Diferente

### 🏗️ Estructura Básica en Java
```java
public class ManejoExcepciones {
    
    public static void ejemploBasico() {
        try {
            // Código que puede lanzar excepciones
            operacionPeligrosa();
            System.out.println("✅ Operación completada exitosamente");
            
        } catch (TipoDeExcepcion e) {
            // Se ejecuta SOLO si se lanza ese tipo específico
            System.out.println("🛠️ Manejando problema: " + e.getMessage());
            
        } catch (OtroTipoDeExcepcion e) {
            // Puedes tener múltiples catch para diferentes tipos
            System.out.println("🔧 Manejando otro tipo de problema: " + e.getMessage());
            
        } finally {
            // Se ejecuta SIEMPRE, haya excepción o no
            System.out.println("🔄 Limpiando recursos...");
        }
    }
}
```

### 📝 Ejemplo Detallado: Validación de Edad en Java

```java
public class ValidadorEdad {
    
    // Excepción personalizada para problemas de edad
    public static class EdadInvalidaException extends Exception {
        private int edadProblematica;
        
        public EdadInvalidaException(String mensaje, int edad) {
            super(mensaje);
            this.edadProblematica = edad;
        }
        
        public int getEdadProblematica() {
            return edadProblematica;
        }
    }
    
    /**
     * Valida una edad y lanza excepciones específicas.
     * IMPORTANTE: Esta función se DETIENE inmediatamente cuando hace throw.
     */
    public static boolean validarEdad(int edad) throws EdadInvalidaException {
        System.out.println("🔍 Validando edad: " + edad);
        
        if (edad < 0) {
            System.out.println("❌ Edad negativa detectada: " + edad);
            // La función se DETIENE aquí si la edad es negativa
            throw new EdadInvalidaException("La edad no puede ser negativa", edad);
        }
        
        if (edad > 120) {
            System.out.println("❌ Edad excesiva detectada: " + edad);
            // La función se DETIENE aquí si la edad es muy alta
            throw new EdadInvalidaException("La edad no puede ser mayor a 120 años", edad);
        }
        
        // Si llegamos hasta aquí, la edad es válida
        System.out.println("✅ Edad " + edad + " es válida");
        return true;
    }
    
    /**
     * Registra un usuario manejando diferentes tipos de problemas
     */
    public static String registrarUsuario(String nombre, int edad) {
        System.out.println("👤 Intentando registrar usuario: " + nombre + ", " + edad + " años");
        
        try {
            // Intentamos validar la edad
            validarEdad(edad);
            
            // Si llegamos aquí, la validación fue exitosa
            System.out.println("🎉 Usuario " + nombre + " registrado exitosamente");
            return "Usuario registrado: " + nombre;
            
        } catch (EdadInvalidaException problema) {
            System.out.println("🛑 Excepción capturada: " + problema.getMessage());
            
            if (problema.getEdadProblematica() < 0) {
                System.out.println("💡 Sugerencia: Verifica que no haya un signo negativo");
                return "Error: Edad negativa - " + problema.getMessage();
            } else {
                System.out.println("💡 Sugerencia: Verifica que la edad sea realista");
                return "Error: Edad excesiva - " + problema.getMessage();
            }
        }
    }
    
    public static void main(String[] args) {
        System.out.println("=== Prueba 1: Caso exitoso ===");
        String resultado1 = registrarUsuario("Ana", 25);
        System.out.println("Resultado: " + resultado1 + "\n");
        
        System.out.println("=== Prueba 2: Edad negativa ===");
        String resultado2 = registrarUsuario("Luis", -30);
        System.out.println("Resultado: " + resultado2 + "\n");
        
        System.out.println("=== Prueba 3: Edad excesiva ===");
        String resultado3 = registrarUsuario("Carmen", 150);
        System.out.println("Resultado: " + resultado3 + "\n");
    }
}
```

### 🔄 Comparación Directa Python vs Java

```python
# PYTHON: raise Exception()
if problema_detectado:
    print("🛑 Problema detectado, función se detiene aquí")
    raise ValueError("Descripción del problema")
    # ⬅️ Todo lo que esté después de esta línea NO se ejecuta

# JAVA: throw new Exception()
if (problemaDetectado) {
    System.out.println("🛑 Problema detectado, función se detiene aquí");
    throw new IllegalArgumentException("Descripción del problema");
    // ⬅️ Todo lo que esté después de esta línea NO se ejecuta
}
```

---

## 🎯 PARTE 5: Cuándo y Cómo Usar Excepciones

### ✅ USA `raise/throw` cuando:

```python
def retirar_dinero(cuenta, monto):
    """
    Función que puede encontrarse con situaciones que no puede resolver por sí misma
    """
    print(f"💰 Intentando retirar ${monto} de cuenta con saldo ${cuenta.saldo}")
    
    # Situación 1: Valor ilógico - la función no puede "arreglarlo"
    if monto <= 0:
        print("❌ Monto inválido detectado, deteniendo función")
        raise ValueError("No puedes retirar una cantidad negativa o cero")
        # ⬅️ Función se detiene aquí, no puede continuar
    
    # Situación 2: Fondos insuficientes - la función no puede crear dinero
    if monto > cuenta.saldo:
        print("❌ Fondos insuficientes detectados, deteniendo función")  
        raise ValueError("Fondos insuficientes")
        # ⬅️ Función se detiene aquí, no puede continuar
    
    # Si llegamos aquí, todo está bien y podemos proceder
    cuenta.saldo -= monto
    print(f"✅ Retiro exitoso, nuevo saldo: ${cuenta.saldo}")
    return cuenta.saldo

# El código que usa esta función decide qué hacer con los problemas
class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

def procesar_retiro_inteligente(cuenta, monto):
    try:
        nuevo_saldo = retirar_dinero(cuenta, monto)
        print(f"🎉 Retiro procesado, saldo actual: ${nuevo_saldo}")
        
    except ValueError as problema:
        if "negativa" in str(problema):
            print("💡 El sistema corrigió automáticamente el monto a positivo")
            # Podríamos intentar con el valor absoluto
            return procesar_retiro_inteligente(cuenta, abs(monto))
        elif "insuficientes" in str(problema):
            print(f"💳 Ofreciendo retirar todo el saldo disponible: ${cuenta.saldo}")
            return procesar_retiro_inteligente(cuenta, cuenta.saldo)

# Ejemplo de uso
mi_cuenta = Cuenta(100)
procesar_retiro_inteligente(mi_cuenta, -50)  # Sistema lo corrige automáticamente
```

### ❌ NO uses `raise/throw` para control de flujo normal:

```python
# ❌ MAL: Usar excepciones para flujo normal
def buscar_usuario_mal(usuarios, nombre):
    for usuario in usuarios:
        if usuario.nombre == nombre:
            return usuario
    # Esto NO es una situación excepcional, es un resultado normal posible
    raise ValueError("Usuario no encontrado")  # ¡Malo!

# ✅ MEJOR: Retornar None o un valor especial para casos normales
def buscar_usuario_bien(usuarios, nombre):
    for usuario in usuarios:
        if usuario.nombre == nombre:
            return usuario
    # Es normal que a veces un usuario no exista
    return None  # Resultado normal, no excepcional

# Uso correcto
usuario = buscar_usuario_bien(lista_usuarios, "Ana")
if usuario is None:
    print("Usuario no encontrado - situación normal")
else:
    print(f"Usuario encontrado: {usuario.nombre}")
```

---

## 🧩 PARTE 6: El Patrón Mental Correcto

### 🤔 Preguntas que Debes Hacerte

Cuando escribas código, pregúntate:

**1. "¿Qué situaciones inesperadas pueden ocurrir en esta función?"**
```python
def calcular_promedio(numeros):
    # Situación inesperada: lista vacía
    if len(numeros) == 0:
        raise ValueError("No se puede calcular promedio de lista vacía")
    
    return sum(numeros) / len(numeros)
```

**2. "¿Mi función puede hacer algo útil si esta situación ocurre?"**
```python
def leer_configuracion(archivo):
    # Mi función NO puede crear el archivo de configuración
    # Esa decisión debe tomarla el código que me llama
    if not os.path.exists(archivo):
        raise FileNotFoundError(f"Archivo de configuración {archivo} no existe")
    
    # Mi función SÍ puede leer el archivo si existe
    with open(archivo) as f:
        return f.read()
```

**3. "¿El código que va a usar mi función tiene mejor contexto para decidir qué hacer?"**
```python
def validar_contraseña(password):
    # Yo solo valido, no decido qué hacer si falla
    if len(password) < 8:
        raise ValueError("Contraseña debe tener al menos 8 caracteres")
    
    if not any(c.isupper() for c in password):
        raise ValueError("Contraseña debe tener al menos una mayúscula")
    
    return True

def crear_cuenta_usuario(email, password):
    # YO decido qué hacer cuando la validación falla
    try:
        validar_contraseña(password)
        # Crear cuenta...
        
    except ValueError as problema_password:
        # Puedo ofrecer generar una contraseña automática
        print(f"Problema con contraseña: {problema_password}")
        password_sugerido = generar_contraseña_segura()
        print(f"¿Quieres usar esta contraseña generada? {password_sugerido}")
```

### 🎪 Ejemplo Final: Integrando Todo

```python
class SistemaBanco:
    def __init__(self):
        self.cuentas = {}
    
    def validar_numero_cuenta(self, numero):
        """
        Solo valida formato, no decide qué hacer si está mal
        Se DETIENE inmediatamente si encuentra un problema
        """
        if not isinstance(numero, str):
            raise TypeError("Número de cuenta debe ser texto")
            # ⬅️ Función se detiene aquí si no es string
            
        if len(numero) != 10:
            raise ValueError("Número de cuenta debe tener 10 dígitos")
            # ⬅️ Función se detiene aquí si longitud es incorrecta
            
        if not numero.isdigit():
            raise ValueError("Número de cuenta solo debe contener números")
            # ⬅️ Función se detiene aquí si contiene caracteres no numéricos
        
        return True
    
    def buscar_cuenta(self, numero):
        """
        Busca cuenta y comunica específicamente si no existe
        Se DETIENE inmediatamente si no encuentra la cuenta
        """
        self.validar_numero_cuenta(numero)  # Puede detenerse aquí
        
        if numero not in self.cuentas:
            raise KeyError(f"Cuenta {numero} no existe en el sistema")
            # ⬅️ Función se detiene aquí si cuenta no existe
            
        return self.cuentas[numero]
    
    def transferir_dinero(self, cuenta_origen, cuenta_destino, monto):
        """
        Maneja las situaciones excepcionales y decide qué hacer con cada una
        """
        print(f"🔄 Iniciando transferencia de ${monto}")
        
        try:
            # Cada una de estas operaciones puede detenerse por diferentes razones
            cuenta1 = self.buscar_cuenta(cuenta_origen)
            print(f"✅ Cuenta origen encontrada")
            
            cuenta2 = self.buscar_cuenta(cuenta_destino)  
            print(f"✅ Cuenta destino encontrada")
            
            if cuenta1.saldo < monto:
                raise ValueError(f"Saldo insuficiente: ${cuenta1.saldo} < ${monto}")
                # ⬅️ Se detiene aquí si no hay fondos
            
            # Si llegamos aquí, todo está validado
            cuenta1.saldo -= monto
            cuenta2.saldo += monto
            return f"Transferencia exitosa: ${monto} transferidos"
            
        except TypeError as problema_tipo:
            return f"❌ Error de formato: {problema_tipo}"
            
        except ValueError as problema_validacion:
            if "dígitos" in str(problema_validacion):
                return f"❌ Formato de cuenta incorrecto: {problema_validacion}"
            else:
                return f"❌ Problema con el monto: {problema_validacion}"
                
        except KeyError as problema_cuenta:
            return f"❌ Cuenta no encontrada: {problema_cuenta}"

# Ejemplo de uso completo
class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

# Crear sistema y cuentas
banco = SistemaBanco()
banco.cuentas["1234567890"] = Cuenta("1234567890", 1000)
banco.cuentas["0987654321"] = Cuenta("0987654321", 500)

# Probar diferentes escenarios
print("=== Caso 1: Transferencia exitosa ===")
resultado1 =
