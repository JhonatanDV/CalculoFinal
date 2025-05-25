# 🧮 Calculadora Matemática Avanzada

Una aplicación completa de cálculo matemático desarrollada con Streamlit que proporciona herramientas avanzadas para integrales definidas, sumas de Riemann, área entre curvas y escenarios de ingeniería.

## ✨ Características Principales

- **📐 Integrales Definidas**: Calcula integrales con solución paso a paso y visualización gráfica
- **📊 Sumas de Riemann**: Aproximación numérica con diferentes métodos (izquierdo, derecho, punto medio)
- **📈 Área Entre Curvas**: Calcula el área entre dos funciones automáticamente
- **🏗️ Escenarios de Ingeniería**: Problemas aplicados con contexto real
- **📚 Plan de Estudios Integrado**: Guías completas con recursos externos
- **🌐 Soporte Multiidioma**: Español e Inglés
- **📖 Documentación Completa**: Guías de instalación y uso detalladas

## 🚀 Instalación Rápida

### Opción 1: Usar en Replit (Recomendado)
1. Haz clic en el botón "Run" en la parte superior
2. Espera a que se instalen las dependencias automáticamente
3. ¡La aplicación estará lista para usar!

### Opción 2: Instalación Local

#### Requisitos Previos
- Python 3.8 o superior
- pip (incluido con Python)
- 4GB RAM mínimo

#### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd calculadora-matematica
   ```

2. **Crear entorno virtual (opcional pero recomendado)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   streamlit run app.py
   ```

5. **Abrir en el navegador**
   - La aplicación estará disponible en: http://localhost:8501

## 📋 Dependencias

```txt
streamlit>=1.28.0
sympy==1.11.1
matplotlib>=3.7.0
plotly>=5.15.0
numpy>=1.24.0
```

## 🎯 Guía de Uso Rápido

### Sintaxis de Funciones
Use notación de Python para las funciones matemáticas:

```python
# Ejemplos correctos
x**2          # x al cuadrado
sin(x)        # función seno
exp(x)        # e^x
log(x)        # logaritmo natural
2*x + 1       # función lineal
sqrt(x)       # raíz cuadrada
pi            # constante pi
```

### Funciones Disponibles

| Tipo | Sintaxis | Ejemplo |
|------|----------|---------|
| Potencias | `x**n` | `x**2`, `x**3` |
| Trigonométricas | `sin(x)`, `cos(x)`, `tan(x)` | `sin(2*x)` |
| Exponencial | `exp(x)` | `exp(-x)` |
| Logaritmo | `log(x)` | `log(x+1)` |
| Raíz cuadrada | `sqrt(x)` | `sqrt(x**2+1)` |
| Constantes | `pi`, `e` | `sin(pi*x)` |

## 📖 Navegación de la Aplicación

1. **📐 Integrales Definidas**
   - Calculadora principal
   - Ejemplos interactivos
   - Plan de estudios completo

2. **📊 Sumas de Riemann**
   - Aproximación numérica
   - Visualización de rectángulos
   - Diferentes métodos

3. **📈 Área Entre Curvas**
   - Cálculo automático de intersecciones
   - Visualización del área
   - Solución paso a paso

4. **🏗️ Escenarios de Ingeniería**
   - Problemas aplicados
   - Contexto real
   - Generador aleatorio

5. **📖 Documentación y Guías**
   - Instrucciones de instalación
   - Guía de uso
   - Preguntas frecuentes
   - Recursos adicionales

## 🛠️ Solución de Problemas

### Error: "Streamlit command not found"
```bash
pip install streamlit
# o
python -m pip install streamlit
```

### Error: "Module not found"
```bash
pip install -r requirements.txt
```

### Error: Función no se calcula
- Verifica la sintaxis: usa `**` para potencias, no `^`
- Asegúrate de usar `*` para multiplicación
- Usa `exp(x)` en lugar de `e^x`

### Error: Puerto ocupado
```bash
streamlit run app.py --server.port 8502
```

## 📚 Recursos de Aprendizaje

### Videos Recomendados
- [Khan Academy - Cálculo Integral](https://www.khanacademy.org/math/integral-calculus)
- [3Blue1Brown - Essence of Calculus](https://www.3blue1brown.com/topics/calculus)
- [Professor Leonard - Cálculo](https://www.youtube.com/user/professorleonard57)

### Cursos Online
- [MIT OpenCourseWare](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)
- [Coursera - Calculus for Engineers](https://www.coursera.org/specializations/calculus-for-engineers)

### Herramientas Complementarias
- [Wolfram Alpha](https://www.wolframalpha.com/) - Verificación de resultados
- [GeoGebra](https://www.geogebra.org/calculator) - Visualización interactiva
- [Desmos](https://www.desmos.com/calculator) - Graficador avanzado

## 🤝 Contribución

¿Quieres mejorar la aplicación? ¡Las contribuciones son bienvenidas!

1. Fork el proyecto
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios
4. Commit (`git commit -am 'Agregar nueva funcionalidad'`)
5. Push a la rama (`git push origin feature/nueva-funcionalidad`)
6. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

¿Necesitas ayuda? Puedes:

1. Revisar la sección **📖 Documentación y Guías** en la aplicación
2. Consultar las **Preguntas Frecuentes**
3. Abrir un issue en el repositorio
4. Contactar al equipo de desarrollo

## 🏆 Características Técnicas

- **Framework**: Streamlit
- **Matemáticas**: SymPy 1.11.1
- **Visualización**: Matplotlib + Plotly
- **Cálculo Numérico**: NumPy
- **Compatible**: Windows, macOS, Linux
- **Navegadores**: Chrome, Firefox, Safari, Edge

## 🌟 ¡Comenzar es Fácil!

1. 🔽 **Instala** siguiendo las instrucciones arriba
2. 🚀 **Ejecuta** `streamlit run app.py`
3. 🌐 **Abre** http://localhost:8501 en tu navegador
4. 🧮 **¡Comienza a calcular!**

---

**¡Disfruta calculando con nuestra herramienta matemática avanzada! 🎉**