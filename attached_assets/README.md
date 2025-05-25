# 🧮 Calculadora Matemática Avanzada

Una aplicación web interactiva desarrollada con Streamlit para resolver problemas de cálculo integral con visualizaciones gráficas y soluciones paso a paso.

## 🌟 Características Principales

- **Integrales Definidas**: Cálculo paso a paso con visualización gráfica
- **Sumas de Riemann**: Aproximaciones numéricas con diferentes métodos
- **Área Entre Curvas**: Cálculo del área entre dos funciones
- **Escenarios de Ingeniería**: Generación aleatoria de problemas aplicados
- **Soporte Bilingüe**: Español e Inglés completamente traducido
- **Interfaz Intuitiva**: Navegación simplificada sin rutas complejas

## 🚀 Características Técnicas

### Generación Aleatoria
Los escenarios son **completamente aleatorios**:
- Funciones matemáticas generadas dinámicamente
- Límites de integración variables
- Contextos de ingeniería diversos
- Diferentes niveles de complejidad

### Manejo Robusto de Expresiones
- Soporte para constantes matemáticas (`pi`, `e`)
- Funciones trigonométricas (`sin`, `cos`, `tan`)
- Función exponencial (`exp`, `log`, `sqrt`)
- Expresiones complejas como `pi/4`, `2*pi`, etc.

## 📦 Instalación y Configuración

### Dependencias
```bash
pip install streamlit sympy matplotlib plotly numpy
```

### Estructura del Proyecto
```
├── app.py                      # Aplicación principal
├── components/                 # Componentes reutilizables
│   ├── math_input.py          # Entrada de expresiones matemáticas
│   └── solution_display.py    # Visualización de soluciones
├── pages/                     # Páginas de la aplicación
│   ├── definite_integrals.py  # Integrales definidas
│   ├── riemann_sums.py        # Sumas de Riemann
│   ├── area_between_curves.py # Área entre curvas
│   └── software_engineering_scenarios.py # Escenarios aleatorios
├── utils/                     # Utilidades y lógica de cálculo
│   ├── calculator.py          # Motor de cálculo principal
│   ├── plotting.py            # Generación de gráficas
│   ├── riemann_sum.py         # Cálculos de Riemann
│   ├── area_calculator.py     # Área entre curvas
│   └── random_generator.py    # Generador de escenarios
└── assets/                    # Recursos y traducciones
    └── translations.py        # Sistema de traducción
```

## 🎯 Uso de la Aplicación

### 1. Integrales Definidas
- Ingresa una función matemática (ej: `x**2`, `sin(x)`, `exp(x)`)
- Define los límites de integración (ej: `0`, `pi/2`, `2*pi`)
- Obtén la solución paso a paso con gráfica

### 2. Sumas de Riemann
- Aproximación numérica de integrales
- Métodos: punto izquierdo, derecho, punto medio
- Visualización de rectángulos en la gráfica

### 3. Área Entre Curvas
- Calcula el área entre dos funciones
- Encuentra automáticamente puntos de intersección
- Visualización de la región sombreada

### 4. Escenarios de Ingeniería
- **¡Completamente aleatorios!** Cada clic genera:
  - Nueva función matemática
  - Límites diferentes
  - Contexto de ingeniería único
  - Interpretación del resultado

## 🔧 Desarrollo Técnico

### Arquitectura
- **Frontend**: Streamlit para interfaz web responsiva
- **Backend**: SymPy para cálculo simbólico
- **Visualización**: Plotly para gráficas interactivas
- **Idiomas**: Sistema de traducción completo

### Algoritmos Implementados
1. **Parser de Expresiones**: Manejo robusto de constantes matemáticas
2. **Integración Simbólica**: Usando SymPy para soluciones exactas
3. **Aproximación Numérica**: Sumas de Riemann con diferentes métodos
4. **Detección de Intersecciones**: Para área entre curvas
5. **Generación Aleatoria**: Algoritmos para crear escenarios únicos

### Manejo de Errores
- Validación de expresiones matemáticas
- Conversión segura de constantes (`pi/4` → número decimal)
- Manejo de funciones especiales (`exp`, `sin`, `cos`)
- Mensajes de error informativos

## 🌐 Despliegue en Streamlit Cloud

### Configuración para Despliegue
1. **Archivo de configuración** (`.streamlit/config.toml`):
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000
```

2. **Dependencias** (`requirements.txt`):
```
streamlit>=1.28.0
sympy>=1.12
matplotlib>=3.7.0
plotly>=5.15.0
numpy>=1.24.0
```

### Pasos para Desplegar
1. Subir código a repositorio GitHub
2. Conectar con Streamlit Cloud
3. Configurar variables de entorno si es necesario
4. ¡Listo para usar!

## 📈 Características Avanzadas

### Generador de Escenarios Aleatorios
```python
# Tipos de escenarios generados:
- Análisis de Uso de Memoria
- Tiempo de Respuesta del Sistema  
- Consumo de CPU por Proceso
- Throughput de Red
- Carga de Trabajo del Servidor
- Análisis de Latencia
- Consumo de Energía
- Tasa de Errores
```

### Funciones Soportadas
- **Básicas**: `x**2`, `x**3`, polinomios
- **Trigonométricas**: `sin(x)`, `cos(x)`, `tan(x)`
- **Exponenciales**: `exp(x)`, `log(x)`, `sqrt(x)`
- **Combinadas**: `x*sin(x)`, `exp(-x**2)`, etc.

## 🐛 Resolución de Problemas

### Errores Comunes Solucionados
1. ❌ `could not convert string to float: 'pi/4'` → ✅ Manejo robusto de constantes
2. ❌ `module 'sympy' has no attribute 'Exp'` → ✅ Namespace correcto para funciones
3. ❌ `Cannot convert expression to float` → ✅ Evaluación segura con SymPy

### Mejores Prácticas
- Usar `pi` en lugar de `π` para mejor compatibilidad
- Escribir `exp(x)` en lugar de `e^x`
- Usar paréntesis para expresiones complejas: `sin(pi*x)`

## 👥 Contribución

### Estructura de Contribución
1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit cambios (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crear Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

---

**Desarrollado con ❤️ usando Streamlit y SymPy**