import streamlit as st

# Language configuration
LANGUAGES = {
    "es": "Español",
    "en": "English"
}

# Translation dictionary
TRANSLATIONS = {
    # App structure and navigation
    "app_title": {
        "es": "Calculadora Matemática Avanzada",
        "en": "Advanced Mathematical Calculator"
    },
    "app_description": {
        "es": """
        Esta aplicación permite realizar cálculos de integrales definidas, sumas de Riemann, 
        área entre curvas y resolver problemas aplicados de ingeniería de software.
        """,
        "en": """
        This application allows you to perform definite integral calculations, Riemann sums,
        area between curves, and solve applied software engineering problems.
        """
    },
    "language_selector": {
        "es": "Selector de Idioma",
        "en": "Language Selector"
    },
    "select_language": {
        "es": "Seleccionar idioma",
        "en": "Select language"
    },
    "navigation": {
        "es": "Navegación",
        "en": "Navigation"
    },
    "select_page": {
        "es": "Seleccionar página",
        "en": "Select page"
    },
    "footer_info": {
        "es": "Calculadora Matemática v2.0 - Desarrollada con Streamlit",
        "en": "Mathematical Calculator v2.0 - Built with Streamlit"
    },
    
    # Page titles
    "definite_integrals": {
        "es": "Integrales Definidas",
        "en": "Definite Integrals"
    },
    "riemann_sums": {
        "es": "Sumas de Riemann",
        "en": "Riemann Sums"
    },
    "area_between_curves": {
        "es": "Área Entre Curvas",
        "en": "Area Between Curves"
    },
    "engineering_scenarios": {
        "es": "Escenarios de Ingeniería",
        "en": "Engineering Scenarios"
    },
    
    # Definite Integrals page
    "definite_integrals_calculator": {
        "es": "Calculadora de Integrales Definidas",
        "en": "Definite Integrals Calculator"
    },
    "definite_integrals_description": {
        "es": """
        Las integrales definidas calculan el valor acumulado de una función sobre un intervalo, 
        a menudo representando el área bajo una curva.
        
        Esta calculadora te permite:
        - Evaluar integrales definidas y ver soluciones paso a paso
        - Visualizar el área bajo la curva
        - Explorar diferentes tipos de funciones e intervalos
        """,
        "en": """
        Definite integrals calculate the accumulated value of a function over an interval,
        often representing area under a curve.
        
        This calculator allows you to:
        - Evaluate definite integrals and see step-by-step solutions
        - Visualize the area under the curve
        - Explore different types of functions and intervals
        """
    },
    
    # Riemann Sums page
    "riemann_sums_calculator": {
        "es": "Calculadora de Sumas de Riemann",
        "en": "Riemann Sums Calculator"
    },
    "riemann_sums_description": {
        "es": """
        Las sumas de Riemann se utilizan para aproximar la integral definida (área bajo una curva) 
        dividiendo el área en rectángulos.
        
        Esta calculadora te permite:
        - Calcular sumas de Riemann usando métodos de punto izquierdo, derecho o punto medio
        - Visualizar los rectángulos utilizados en la aproximación
        - Ver soluciones paso a paso
        """,
        "en": """
        Riemann sums are used to approximate the definite integral (area under a curve)
        by dividing the area into rectangles.
        
        This calculator allows you to:
        - Calculate Riemann sums using left, right, or midpoint methods
        - Visualize the rectangles used in the approximation
        - See step-by-step solutions
        """
    },
    
    # Area Between Curves page
    "area_between_curves_calculator": {
        "es": "Calculadora de Área Entre Curvas",
        "en": "Area Between Curves Calculator"
    },
    "area_between_curves_description": {
        "es": """
        Esta calculadora encuentra el área encerrada entre dos curvas sobre un intervalo especificado.
        
        Puedes:
        - Calcular el área entre cualquier dos funciones
        - Visualizar la región encerrada
        - Ver soluciones paso a paso
        - Encontrar puntos de intersección automáticamente
        """,
        "en": """
        This calculator finds the area enclosed between two curves over a specified interval.
        
        You can:
        - Calculate the area between any two functions
        - Visualize the enclosed region
        - See step-by-step solutions
        - Find intersection points automatically
        """
    },
    
    # Engineering Scenarios page
    "engineering_scenarios_description": {
        "es": """
        Explora problemas del mundo real de ingeniería de software usando integrales definidas.
        Cada escenario presenta un contexto realista donde las matemáticas resuelven problemas prácticos.
        """,
        "en": """
        Explore real-world software engineering problems using definite integrals.
        Each scenario presents a realistic context where mathematics solves practical problems.
        """
    },
    
    # Common UI elements
    "function_and_interval": {
        "es": "Función e Intervalo",
        "en": "Function and Interval"
    },
    "functions_and_interval": {
        "es": "Funciones e Intervalo",
        "en": "Functions and Interval"
    },
    "function_fx": {
        "es": "Función f(x)",
        "en": "Function f(x)"
    },
    "first_function_f1": {
        "es": "Primera Función f₁(x)",
        "en": "First Function f₁(x)"
    },
    "second_function_f2": {
        "es": "Segunda Función f₂(x)",
        "en": "Second Function f₂(x)"
    },
    "lower_bound_a": {
        "es": "Límite Inferior (a)",
        "en": "Lower Bound (a)"
    },
    "upper_bound_b": {
        "es": "Límite Superior (b)",
        "en": "Upper Bound (b)"
    },
    "lower_limit_a": {
        "es": "Límite Inferior (a)",
        "en": "Lower Limit (a)"
    },
    "upper_limit_b": {
        "es": "Límite Superior (b)",
        "en": "Upper Limit (b)"
    },
    "lower_limit": {
        "es": "Límite Inferior",
        "en": "Lower Limit"
    },
    "upper_limit": {
        "es": "Límite Superior",
        "en": "Upper Limit"
    },
    "lower_bound": {
        "es": "Límite Inferior",
        "en": "Lower Bound"
    },
    "upper_bound": {
        "es": "Límite Superior",
        "en": "Upper Bound"
    },
    "variable": {
        "es": "Variable",
        "en": "Variable"
    },
    "number_subdivisions_n": {
        "es": "Número de Subdivisiones (n)",
        "en": "Number of Subdivisions (n)"
    },
    "sampling_method": {
        "es": "Método de Muestreo",
        "en": "Sampling Method"
    },
    
    # Methods
    "method_left": {
        "es": "Punto Izquierdo",
        "en": "Left Endpoint"
    },
    "method_right": {
        "es": "Punto Derecho",
        "en": "Right Endpoint"
    },
    "method_midpoint": {
        "es": "Punto Medio",
        "en": "Midpoint"
    },
    
    # Examples
    "example_problems": {
        "es": "Problemas de Ejemplo",
        "en": "Example Problems"
    },
    "select_example": {
        "es": "Selecciona un ejemplo de los materiales del curso:",
        "en": "Select an example from the course materials:"
    },
    "load_example": {
        "es": "Cargar Ejemplo",
        "en": "Load Example"
    },
    
    # Calculations
    "calculate_integral": {
        "es": "Calcular Integral",
        "en": "Calculate Integral"
    },
    "calculate_riemann_sum": {
        "es": "Calcular Suma de Riemann",
        "en": "Calculate Riemann Sum"
    },
    "calculate_area": {
        "es": "Calcular Área",
        "en": "Calculate Area"
    },
    "calculate_area_between_curves": {
        "es": "Calcular Área Entre Curvas",
        "en": "Calculate Area Between Curves"
    },
    "calculating": {
        "es": "Calculando...",
        "en": "Calculating..."
    },
    
    # Results and solutions
    "solution": {
        "es": "Solución",
        "en": "Solution"
    },
    "result": {
        "es": "Resultado",
        "en": "Result"
    },
    "evaluating": {
        "es": "Evaluando",
        "en": "Evaluating"
    },
    "step_by_step_solution": {
        "es": "Solución Paso a Paso",
        "en": "Step-by-Step Solution"
    },
    "show_solution_steps": {
        "es": "Mostrar Pasos de la Solución",
        "en": "Show Solution Steps"
    },
    "download_solution": {
        "es": "Descargar Solución",
        "en": "Download Solution"
    },
    
    # Steps and calculations
    "step": {
        "es": "Paso",
        "en": "Step"
    },
    "find_antiderivative": {
        "es": "Encontrar la antiderivada",
        "en": "Find the antiderivative"
    },
    "apply_fundamental_theorem": {
        "es": "Aplicar el Teorema Fundamental del Cálculo",
        "en": "Apply the Fundamental Theorem of Calculus"
    },
    "evaluate_at_bounds": {
        "es": "Evaluar en los límites",
        "en": "Evaluate at the bounds"
    },
    "final_calculation": {
        "es": "Cálculo final",
        "en": "Final calculation"
    },
    "calculate_delta_x": {
        "es": "Calcular Δx",
        "en": "Calculate Δx"
    },
    "identify_sample_points": {
        "es": "Identificar puntos de muestra",
        "en": "Identify sample points"
    },
    "using_method": {
        "es": "Usando método",
        "en": "Using method"
    },
    "sample_points": {
        "es": "Puntos de muestra",
        "en": "Sample points"
    },
    "evaluate_function": {
        "es": "Evaluar la función",
        "en": "Evaluate the function"
    },
    "calculate_riemann_formula": {
        "es": "Calcular usando la fórmula de Riemann",
        "en": "Calculate using Riemann formula"
    },
    
    # Intersection points
    "find_intersections_automatically": {
        "es": "Encontrar puntos de intersección automáticamente",
        "en": "Find intersection points automatically"
    },
    "find_intersection_points": {
        "es": "Encontrar Puntos de Intersección",
        "en": "Find Intersection Points"
    },
    "finding_intersections": {
        "es": "Encontrando intersecciones...",
        "en": "Finding intersections..."
    },
    "found_intersections": {
        "es": "Se encontraron intersecciones",
        "en": "Found intersections"
    },
    "intersection_points": {
        "es": "Puntos de intersección",
        "en": "Intersection points"
    },
    "suggested_bounds": {
        "es": "Límites sugeridos",
        "en": "Suggested bounds"
    },
    "from": {
        "es": "desde",
        "en": "from"
    },
    "to": {
        "es": "hasta",
        "en": "to"
    },
    "use_first_interval": {
        "es": "Usar Primer Intervalo",
        "en": "Use First Interval"
    },
    "no_intersections_found": {
        "es": "No se encontraron intersecciones en el dominio",
        "en": "No intersection points found in the domain"
    },
    
    # Visualization
    "visualization": {
        "es": "Visualización",
        "en": "Visualization"
    },
    "graph_of": {
        "es": "Gráfica de",
        "en": "Graph of"
    },
    "area_under_curve": {
        "es": "Área bajo la curva",
        "en": "Area under curve"
    },
    "definite_integral": {
        "es": "Integral definida",
        "en": "Definite integral"
    },
    "riemann_sum": {
        "es": "Suma de Riemann",
        "en": "Riemann sum"
    },
    "sample_point": {
        "es": "Punto de muestra",
        "en": "Sample point"
    },
    "area_between_curves": {
        "es": "Área entre curvas",
        "en": "Area between curves"
    },
    
    # Method comparison
    "method_comparison": {
        "es": "Comparación de Métodos",
        "en": "Method Comparison"
    },
    "compare_methods": {
        "es": "Comparar Métodos",
        "en": "Compare Methods"
    },
    "comparing_methods": {
        "es": "Comparando métodos...",
        "en": "Comparing methods..."
    },
    "exact_value": {
        "es": "Valor exacto",
        "en": "Exact value"
    },
    "most_accurate_method": {
        "es": "Método más preciso",
        "en": "Most accurate method"
    },
    "error": {
        "es": "Error",
        "en": "Error"
    },
    
    # Additional tools
    "additional_tools": {
        "es": "Herramientas Adicionales",
        "en": "Additional Tools"
    },
    "swap_functions": {
        "es": "Intercambiar Funciones",
        "en": "Swap Functions"
    },
    "clear_functions": {
        "es": "Limpiar Funciones",
        "en": "Clear Functions"
    },
    
    # Theory sections
    "learn_about_definite_integrals": {
        "es": "Aprende sobre Integrales Definidas",
        "en": "Learn about Definite Integrals"
    },
    "learn_about_riemann_sums": {
        "es": "Aprende sobre las Sumas de Riemann",
        "en": "Learn about Riemann Sums"
    },
    "learn_about_area_between_curves": {
        "es": "Aprende sobre el Área Entre Curvas",
        "en": "Learn about Area Between Curves"
    },
    
    # Theory content
    "what_is_definite_integral": {
        "es": "¿Qué es una Integral Definida?",
        "en": "What is a Definite Integral?"
    },
    "definite_integral_explanation": {
        "es": """
        Una integral definida representa el área neta bajo una curva entre dos puntos específicos.
        Matemáticamente, es el límite de las sumas de Riemann cuando el número de subdivisiones tiende al infinito.
        """,
        "en": """
        A definite integral represents the net area under a curve between two specific points.
        Mathematically, it is the limit of Riemann sums as the number of subdivisions approaches infinity.
        """
    },
    "fundamental_theorem": {
        "es": "Teorema Fundamental del Cálculo",
        "en": "Fundamental Theorem of Calculus"
    },
    "fundamental_theorem_explanation": {
        "es": """
        El Teorema Fundamental del Cálculo conecta la diferenciación y la integración.
        Establece que la integral definida de una función continua se puede evaluar usando su antiderivada.
        """,
        "en": """
        The Fundamental Theorem of Calculus connects differentiation and integration.
        It states that the definite integral of a continuous function can be evaluated using its antiderivative.
        """
    },
    "where_f_is_antiderivative": {
        "es": "donde F(x) es la antiderivada de f(x)",
        "en": "where F(x) is the antiderivative of f(x)"
    },
    "properties_definite_integrals": {
        "es": "Propiedades de las Integrales Definidas",
        "en": "Properties of Definite Integrals"
    },
    
    # Riemann Sums theory
    "what_is_riemann_sum": {
        "es": "¿Qué es una Suma de Riemann?",
        "en": "What is a Riemann Sum?"
    },
    "riemann_sum_explanation": {
        "es": """
        Una suma de Riemann es un método para aproximar la integral definida dividiendo el área bajo una curva
        en rectángulos y sumando sus áreas.
        """,
        "en": """
        A Riemann sum is a method for approximating the definite integral by dividing the area under a curve
        into rectangles and summing their areas.
        """
    },
    "types_riemann_sums": {
        "es": "Tipos de Sumas de Riemann",
        "en": "Types of Riemann Sums"
    },
    "left_method_explanation": {
        "es": "Usa el extremo izquierdo de cada subintervalo para determinar la altura del rectángulo",
        "en": "Uses the left endpoint of each subinterval to determine the height of the rectangle"
    },
    "right_method_explanation": {
        "es": "Usa el extremo derecho de cada subintervalo para determinar la altura del rectángulo",
        "en": "Uses the right endpoint of each subinterval to determine the height of the rectangle"
    },
    "midpoint_method_explanation": {
        "es": "Usa el punto medio de cada subintervalo para determinar la altura del rectángulo",
        "en": "Uses the midpoint of each subinterval to determine the height of the rectangle"
    },
    "the_formula": {
        "es": "La Fórmula",
        "en": "The Formula"
    },
    "riemann_formula_explanation": {
        "es": "La suma de Riemann se calcula usando la siguiente fórmula:",
        "en": "The Riemann sum is calculated using the following formula:"
    },
    "where_explanation": {
        "es": "donde Δx es el ancho de cada subdivisión y x_i* es el punto de muestra en cada subintervalo.",
        "en": "where Δx is the width of each subdivision and x_i* is the sample point in each subinterval."
    },
    "connection_definite_integrals": {
        "es": "Conexión con Integrales Definidas",
        "en": "Connection to Definite Integrals"
    },
    "convergence_explanation": {
        "es": """
        Cuando el número de subdivisiones n tiende al infinito, la suma de Riemann converge a la integral definida:
        """,
        "en": """
        As the number of subdivisions n approaches infinity, the Riemann sum converges to the definite integral:
        """
    },
    "fundamental_connection": {
        "es": "Esta es la conexión fundamental entre las sumas de Riemann y las integrales definidas.",
        "en": "This is the fundamental connection between Riemann sums and definite integrals."
    },
    
    # Area between curves theory
    "what_is_area_between_curves": {
        "es": "¿Qué es el Área Entre Curvas?",
        "en": "What is Area Between Curves?"
    },
    "area_between_curves_explanation": {
        "es": """
        El área entre curvas es la región encerrada por dos o más funciones en un intervalo dado.
        Se calcula como la integral de la diferencia absoluta entre las funciones.
        """,
        "en": """
        The area between curves is the region enclosed by two or more functions over a given interval.
        It is calculated as the integral of the absolute difference between the functions.
        """
    },
    "when_functions_intersect": {
        "es": "Cuando las Funciones se Intersectan",
        "en": "When Functions Intersect"
    },
    "intersection_handling_explanation": {
        "es": """
        Cuando las funciones se intersectan dentro del intervalo, debemos dividir la integral en subintervalos
        donde una función está consistentemente por encima de la otra.
        """,
        "en": """
        When functions intersect within the interval, we must split the integral into subintervals
        where one function is consistently above the other.
        """
    },
    "applications": {
        "es": "Aplicaciones",
        "en": "Applications"
    },
    
    # Input helpers
    "function_input_help": {
        "es": "Ingresa una función matemática usando x como variable. Ejemplos: x^2, sin(x), exp(x)",
        "en": "Enter a mathematical function using x as the variable. Examples: x^2, sin(x), exp(x)"
    },
    "bound_help": {
        "es": "Ingresa un número o expresión matemática como pi, e, pi/2",
        "en": "Enter a number or mathematical expression like pi, e, pi/2"
    },
    "variable_help": {
        "es": "Variable de integración (usualmente x, t, o n)",
        "en": "Integration variable (usually x, t, or n)"
    },
    
    # Math input
    "math_input_help": {
        "es": "Usa notación matemática estándar: ^para exponentes, *para multiplicación",
        "en": "Use standard mathematical notation: ^ for exponents, * for multiplication"
    },
    "preview": {
        "es": "Vista Previa",
        "en": "Preview"
    },
    "valid_expression": {
        "es": "Expresión válida",
        "en": "Valid expression"
    },
    "invalid_expression": {
        "es": "Expresión inválida",
        "en": "Invalid expression"
    },
    "expression_warning": {
        "es": "Advertencia de expresión",
        "en": "Expression warning"
    },
    
    # Math keyboard
    "math_keyboard": {
        "es": "Teclado Matemático",
        "en": "Math Keyboard"
    },
    "basic_operations": {
        "es": "Operaciones Básicas",
        "en": "Basic Operations"
    },
    "powers_roots": {
        "es": "Potencias y Raíces",
        "en": "Powers and Roots"
    },
    "trigonometric": {
        "es": "Trigonométricas",
        "en": "Trigonometric"
    },
    "constants": {
        "es": "Constantes",
        "en": "Constants"
    },
    
    # Function examples
    "function_examples": {
        "es": "Ejemplos de Funciones",
        "en": "Function Examples"
    },
    "polynomial_functions": {
        "es": "Funciones Polinómicas",
        "en": "Polynomial Functions"
    },
    "trigonometric_functions": {
        "es": "Funciones Trigonométricas",
        "en": "Trigonometric Functions"
    },
    "exponential_functions": {
        "es": "Funciones Exponenciales",
        "en": "Exponential Functions"
    },
    "logarithmic_functions": {
        "es": "Funciones Logarítmicas",
        "en": "Logarithmic Functions"
    },
    "other_functions": {
        "es": "Otras Funciones",
        "en": "Other Functions"
    },
    
    # Error messages
    "empty_function": {
        "es": "La función no puede estar vacía",
        "en": "Function cannot be empty"
    },
    "empty_bounds": {
        "es": "Los límites no pueden estar vacíos",
        "en": "Bounds cannot be empty"
    },
    "invalid_interval": {
        "es": "Intervalo inválido: el límite inferior debe ser menor que el superior",
        "en": "Invalid interval: lower bound must be less than upper bound"
    },
    "invalid_subdivisions": {
        "es": "Número de subdivisiones inválido",
        "en": "Invalid number of subdivisions"
    },
    "calculation_error": {
        "es": "Error de cálculo",
        "en": "Calculation error"
    },
    "unexpected_error": {
        "es": "Error inesperado",
        "en": "Unexpected error"
    },
    "comparison_error": {
        "es": "Error en la comparación",
        "en": "Comparison error"
    },
    "fill_all_fields": {
        "es": "Por favor completa todos los campos",
        "en": "Please fill all fields"
    },
    "enter_both_functions": {
        "es": "Por favor ingresa ambas funciones",
        "en": "Please enter both functions"
    },
    
    # Error details and suggestions
    "error_details": {
        "es": "Detalles del Error",
        "en": "Error Details"
    },
    "suggestions": {
        "es": "Sugerencias",
        "en": "Suggestions"
    },
    "check_syntax": {
        "es": "Verifica la sintaxis de la función",
        "en": "Check the function syntax"
    },
    "use_star_multiplication": {
        "es": "Usa * para multiplicación (ej: 2*x en lugar de 2x)",
        "en": "Use * for multiplication (e.g., 2*x instead of 2x)"
    },
    "check_parentheses": {
        "es": "Verifica que los paréntesis estén balanceados",
        "en": "Check that parentheses are balanced"
    },
    "use_valid_functions": {
        "es": "Usa funciones válidas: sin, cos, exp, log, sqrt",
        "en": "Use valid functions: sin, cos, exp, log, sqrt"
    },
    "check_exp_function": {
        "es": "Usa 'exp' en lugar de 'Exp' para la función exponencial",
        "en": "Use 'exp' instead of 'Exp' for the exponential function"
    },
    "check_bounds_numeric": {
        "es": "Verifica que los límites sean numéricos o expresiones válidas",
        "en": "Check that bounds are numeric or valid expressions"
    },
    "use_pi_for_pi": {
        "es": "Usa 'pi' para π y 'e' para el número de Euler",
        "en": "Use 'pi' for π and 'e' for Euler's number"
    },
    "use_e_for_e": {
        "es": "Usa 'e' para el número de Euler (≈2.718)",
        "en": "Use 'e' for Euler's number (≈2.718)"
    },
    "use_decimal_format": {
        "es": "Usa formato decimal (ej: 3.14159 en lugar de fracciones)",
        "en": "Use decimal format (e.g., 3.14159 instead of fractions)"
    },
    "check_domain": {
        "es": "Verifica que la función esté definida en el dominio dado",
        "en": "Check that the function is defined over the given domain"
    },
    "avoid_division_zero": {
        "es": "Evita la división por cero en el intervalo",
        "en": "Avoid division by zero in the interval"
    },
    "check_complex_results": {
        "es": "Verifica que el resultado no sea un número complejo",
        "en": "Check that the result is not a complex number"
    },
    "verify_function_bounds": {
        "es": "Verifica que la función sea válida en los límites dados",
        "en": "Verify that the function is valid at the given bounds"
    },
    "general_suggestions": {
        "es": "Sugerencias Generales",
        "en": "General Suggestions"
    },
    "check_all_inputs": {
        "es": "Verifica todos los campos de entrada",
        "en": "Check all input fields"
    },
    "try_simpler_function": {
        "es": "Intenta con una función más simple",
        "en": "Try a simpler function"
    },
    "contact_support": {
        "es": "Contacta soporte si el problema persiste",
        "en": "Contact support if the problem persists"
    },
    
    # Solution display
    "riemann_sum_solution": {
        "es": "Solución de la Suma de Riemann",
        "en": "Riemann Sum Solution"
    },
    "calculating_riemann_sum": {
        "es": "Calculando suma de Riemann",
        "en": "Calculating Riemann sum"
    },
    "for": {
        "es": "para",
        "en": "for"
    },
    "on": {
        "es": "en",
        "en": "on"
    },
    "with": {
        "es": "con",
        "en": "with"
    },
    "what_riemann_represents": {
        "es": "¿Qué Representa la Suma de Riemann?",
        "en": "What Does the Riemann Sum Represent?"
    },
    "riemann_explanation": {
        "es": "Explicación de la Suma de Riemann",
        "en": "Riemann Sum Explanation"
    },
    "riemann_approximates": {
        "es": "La suma de Riemann aproxima el área bajo la curva de",
        "en": "The Riemann sum approximates the area under the curve of"
    },
    "by_dividing_into": {
        "es": "dividiéndola en",
        "en": "by dividing it into"
    },
    "equal_subintervals": {
        "es": "subintervalos iguales",
        "en": "equal subintervals"
    },
    "method_explanation": {
        "es": "El método seleccionado determina dónde se evalúa la función en cada subintervalo.",
        "en": "The selected method determines where the function is evaluated in each subinterval."
    },
    "left_endpoint_explanation": {
        "es": "Punto izquierdo: evalúa la función en el extremo izquierdo de cada subintervalo",
        "en": "Left endpoint: evaluates the function at the left end of each subinterval"
    },
    "right_endpoint_explanation": {
        "es": "Punto derecho: evalúa la función en el extremo derecho de cada subintervalo",
        "en": "Right endpoint: evaluates the function at the right end of each subinterval"
    },
    "midpoint_explanation": {
        "es": "Punto medio: evalúa la función en el punto medio de cada subintervalo",
        "en": "Midpoint: evaluates the function at the midpoint of each subinterval"
    },
    
    # Area between curves solution
    "area_between_curves_solution": {
        "es": "Solución del Área Entre Curvas",
        "en": "Area Between Curves Solution"
    },
    "calculating_area_between": {
        "es": "Calculando el área entre",
        "en": "Calculating area between"
    },
    "and": {
        "es": "y",
        "en": "and"
    },
    "square_units": {
        "es": "unidades cuadradas",
        "en": "square units"
    },
    "what_area_represents": {
        "es": "¿Qué Representa el Área?",
        "en": "What Does the Area Represent?"
    },
    "area_explanation": {
        "es": "Explicación del Área",
        "en": "Area Explanation"
    },
    "area_between_explanation": {
        "es": "El área calculada representa la región encerrada entre",
        "en": "The calculated area represents the region enclosed between"
    },
    "area_formula": {
        "es": "Fórmula del Área",
        "en": "Area Formula"
    },
    "area_practice": {
        "es": "En la práctica, calculamos",
        "en": "In practice, we calculate"
    },
    "upper_function": {
        "es": "función superior",
        "en": "upper function"
    },
    "lower_function": {
        "es": "función inferior",
        "en": "lower function"
    },
    "area": {
        "es": "Área",
        "en": "Area"
    },
    
    # Additional solution content
    "additional_info": {
        "es": "Información Adicional",
        "en": "Additional Information"
    },
    "interpretation": {
        "es": "Interpretación",
        "en": "Interpretation"
    },
    "integral_interpretation": {
        "es": "La integral definida representa el área neta bajo la curva. Si es positiva, hay más área por encima del eje x que por debajo.",
        "en": "The definite integral represents the net area under the curve. If positive, there is more area above the x-axis than below."
    },
    "positive_result_meaning": {
        "es": "El resultado positivo indica que el área neta está por encima del eje x",
        "en": "The positive result indicates that the net area is above the x-axis"
    },
    "negative_result_meaning": {
        "es": "El resultado negativo indica que hay más área por debajo del eje x",
        "en": "The negative result indicates that there is more area below the x-axis"
    },
    "function_complexity": {
        "es": "Complejidad de la Función",
        "en": "Function Complexity"
    },
    
    # Download and summary
    "integral_calculation": {
        "es": "Cálculo de integral",
        "en": "Integral calculation"
    },
    "riemann_sum_calculation": {
        "es": "Cálculo de suma de Riemann",
        "en": "Riemann sum calculation"
    },
    "area_between_curves_calculation": {
        "es": "Cálculo de área entre curvas",
        "en": "Area between curves calculation"
    },
    "method": {
        "es": "Método",
        "en": "Method"
    },
    "calculation_summary": {
        "es": "Resumen del Cálculo",
        "en": "Calculation Summary"
    },
    "calculation_type": {
        "es": "Tipo de Cálculo",
        "en": "Calculation Type"
    },
    "final_result": {
        "es": "Resultado Final",
        "en": "Final Result"
    },
    "result_near_zero": {
        "es": "El resultado está muy cerca de cero",
        "en": "The result is very close to zero"
    },
    "result_positive": {
        "es": "El resultado es positivo",
        "en": "The result is positive"
    },
    "result_negative": {
        "es": "El resultado es negativo",
        "en": "The result is negative"
    },
    "large_result_note": {
        "es": "Resultado grande: verifica las unidades de medida",
        "en": "Large result: check the units of measurement"
    },
    "small_result_note": {
        "es": "Resultado pequeño: considera usar más decimales",
        "en": "Small result: consider using more decimal places"
    },
    
    # Accuracy analysis
    "accuracy_analysis": {
        "es": "Análisis de Precisión",
        "en": "Accuracy Analysis"
    },
    "exact_integral": {
        "es": "Integral exacta",
        "en": "Exact integral"
    },
    "absolute_error": {
        "es": "Error absoluto",
        "en": "Absolute error"
    },
    "relative_error": {
        "es": "Error relativo",
        "en": "Relative error"
    },
    "excellent_approximation": {
        "es": "Excelente aproximación (error < 1%)",
        "en": "Excellent approximation (error < 1%)"
    },
    "good_approximation": {
        "es": "Buena aproximación (error < 5%)",
        "en": "Good approximation (error < 5%)"
    },
    "poor_approximation": {
        "es": "Aproximación pobre (error > 5%)",
        "en": "Poor approximation (error > 5%)"
    },
    "exact_comparison_unavailable": {
        "es": "Comparación exacta no disponible",
        "en": "Exact comparison unavailable"
    },
    
    # Function analysis
    "function_analysis": {
        "es": "Análisis de Funciones",
        "en": "Function Analysis"
    },
    "intersection_points_found": {
        "es": "Puntos de intersección encontrados",
        "en": "Intersection points found"
    },
    "no_intersections_in_range": {
        "es": "No hay intersecciones en el rango dado",
        "en": "No intersections in the given range"
    },
    "intersection_analysis_unavailable": {
        "es": "Análisis de intersecciones no disponible",
        "en": "Intersection analysis unavailable"
    },
    
    # Applications
    "physics_applications": {
        "es": "Aplicaciones en física: trabajo, momentum, energía",
        "en": "Physics applications: work, momentum, energy"
    },
    "economics_applications": {
        "es": "Aplicaciones en economía: excedente del consumidor, beneficio total",
        "en": "Economics applications: consumer surplus, total profit"
    },
    "engineering_applications": {
        "es": "Aplicaciones en ingeniería: análisis de señales, sistemas de control",
        "en": "Engineering applications: signal analysis, control systems"
    },
    "probability_applications": {
        "es": "Aplicaciones en probabilidad: distribuciones continuas",
        "en": "Probability applications: continuous distributions"
    },
    "optimization_applications": {
        "es": "Aplicaciones en optimización: minimización de costos",
        "en": "Optimization applications: cost minimization"
    },
    "physical_applications": {
        "es": "Aplicaciones físicas (trabajo, distancia, volumen)",
        "en": "Physical applications (work, distance, volume)"
    },
    "economic_applications": {
        "es": "Aplicaciones económicas (excedente, ganancias)",
        "en": "Economic applications (surplus, profits)"
    },
    "volume_solids": {
        "es": "Volumen de sólidos de revolución",
        "en": "Volume of solids of revolution"
    },
    "arc_length": {
        "es": "Longitud de arco",
        "en": "Arc length"
    },
    "work_by_force": {
        "es": "Trabajo realizado por una fuerza",
        "en": "Work done by a force"
    },
    "probability_distributions": {
        "es": "Distribuciones de probabilidad",
        "en": "Probability distributions"
    },
    "center_of_mass": {
        "es": "Centro de masa",
        "en": "Center of mass"
    },
    
    # Tips and guidance
    "tips_for_success": {
        "es": "Consejos para el Éxito",
        "en": "Tips for Success"
    },
    "identify_intersection_points": {
        "es": "Identifica los puntos de intersección antes de calcular",
        "en": "Identify intersection points before calculating"
    },
    "determine_which_function_top": {
        "es": "Determina cuál función está arriba en cada intervalo",
        "en": "Determine which function is on top in each interval"
    },
    "split_intervals_if_needed": {
        "es": "Divide los intervalos si las funciones se cruzan",
        "en": "Split intervals if functions cross"
    },
    "always_positive_area": {
        "es": "El área siempre debe ser positiva",
        "en": "Area should always be positive"
    },
    "check_work_with_graph": {
        "es": "Verifica tu trabajo con la gráfica",
        "en": "Check your work with the graph"
    },
    
    # Intersection analysis
    "intersection_analysis": {
        "es": "Análisis de Intersecciones",
        "en": "Intersection Analysis"
    },
    
    # Engineering scenarios specific terms
    "random_scenario": {
        "es": "Escenario Aleatorio",
        "en": "Random Scenario"
    },
    "scenario_gallery": {
        "es": "Galería de Escenarios",
        "en": "Scenario Gallery"
    },
    "custom_scenario": {
        "es": "Escenario Personalizado",
        "en": "Custom Scenario"
    },
    "generate_random_scenario": {
        "es": "Generar Escenario Aleatorio",
        "en": "Generate Random Scenario"
    },
    "random_scenario_info": {
        "es": "Genera un escenario de ingeniería completamente aleatorio con función y límites únicos",
        "en": "Generate a completely random engineering scenario with unique function and bounds"
    },
    "scenario_generation_error": {
        "es": "Error al generar escenario",
        "en": "Scenario generation error"
    },
    "initialization_error": {
        "es": "Error de inicialización",
        "en": "Initialization error"
    },
    "engineering_scenario_gallery": {
        "es": "Galería de Escenarios de Ingeniería",
        "en": "Engineering Scenario Gallery"
    },
    "gallery_description": {
        "es": "Explora múltiples escenarios de ingeniería de software generados automáticamente.",
        "en": "Explore multiple automatically generated software engineering scenarios."
    },
    "refresh_gallery": {
        "es": "Actualizar Galería",
        "en": "Refresh Gallery"
    },
    "generating_scenarios": {
        "es": "Generando escenarios...",
        "en": "Generating scenarios..."
    },
    "no_valid_scenarios_generated": {
        "es": "No se pudieron generar escenarios válidos",
        "en": "Could not generate valid scenarios"
    },
    "loading_scenarios": {
        "es": "Cargando escenarios...",
        "en": "Loading scenarios..."
    },
    "function": {
        "es": "Función",
        "en": "Function"
    },
    "complexity": {
        "es": "Complejidad",
        "en": "Complexity"
    },
    "context": {
        "es": "Contexto",
        "en": "Context"
    },
    "select_scenario": {
        "es": "Seleccionar Escenario",
        "en": "Select Scenario"
    },
    "selected_scenario": {
        "es": "Escenario Seleccionado",
        "en": "Selected Scenario"
    },
    "no_scenarios_available": {
        "es": "No hay escenarios disponibles",
        "en": "No scenarios available"
    },
    "create_custom_scenario": {
        "es": "Crear Escenario Personalizado",
        "en": "Create Custom Scenario"
    },
    "custom_scenario_description": {
        "es": "Diseña tu propio escenario de ingeniería con parámetros personalizados.",
        "en": "Design your own engineering scenario with custom parameters."
    },
    "scenario_title": {
        "es": "Título del Escenario",
        "en": "Scenario Title"
    },
    "mathematical_function": {
        "es": "Función Matemática",
        "en": "Mathematical Function"
    },
    "engineering_context": {
        "es": "Contexto de Ingeniería",
        "en": "Engineering Context"
    },
    "measurement_unit": {
        "es": "Unidad de Medida",
        "en": "Measurement Unit"
    },
    "scenario_description": {
        "es": "Descripción del Escenario",
        "en": "Scenario Description"
    },
    "custom_scenario_created": {
        "es": "Escenario personalizado creado exitosamente",
        "en": "Custom scenario created successfully"
    },
    "validation_error": {
        "es": "Error de validación",
        "en": "Validation error"
    },
    "your_custom_scenario": {
        "es": "Tu Escenario Personalizado",
        "en": "Your Custom Scenario"
    },
    "integration_bounds": {
        "es": "Límites de Integración",
        "en": "Integration Bounds"
    },
    "lower": {
        "es": "Inferior",
        "en": "Lower"
    },
    "upper": {
        "es": "Superior",
        "en": "Upper"
    },
    "result_interpretation": {
        "es": "Interpretación del Resultado",
        "en": "Result Interpretation"
    },
    "area_under_curve_represents": {
        "es": "El área bajo la curva representa",
        "en": "The area under the curve represents"
    },
    "total_accumulated_value": {
        "es": "Este valor indica la cantidad total acumulada durante el período analizado",
        "en": "This value indicates the total accumulated quantity during the analyzed period"
    },
    "engineering_insights": {
        "es": "Perspectivas de Ingeniería",
        "en": "Engineering Insights"
    },
    "practical_meaning": {
        "es": "Significado Práctico",
        "en": "Practical Meaning"
    },
    "positive_accumulated_value": {
        "es": "El valor acumulado positivo indica crecimiento o ganancia neta",
        "en": "Positive accumulated value indicates growth or net gain"
    },
    "negative_accumulated_value": {
        "es": "El valor acumulado negativo indica decrecimiento o pérdida neta",
        "en": "Negative accumulated value indicates decrease or net loss"
    },
    "memory_usage_insight": {
        "es": "En sistemas de memoria, esto representa la utilización total de recursos",
        "en": "In memory systems, this represents total resource utilization"
    },
    "cpu_usage_insight": {
        "es": "En sistemas de CPU, esto representa el tiempo total de procesamiento",
        "en": "In CPU systems, this represents total processing time"
    },
    "user_load_insight": {
        "es": "En sistemas de usuarios, esto representa la carga acumulada total",
        "en": "In user systems, this represents total accumulated load"
    },
    "general_performance_insight": {
        "es": "En análisis de rendimiento, esto representa el comportamiento acumulado del sistema",
        "en": "In performance analysis, this represents accumulated system behavior"
    },
    "try_different_scenario": {
        "es": "Intenta generar un nuevo escenario si persiste el error",
        "en": "Try generating a new scenario if the error persists"
    },
    
    # Results comparison
    "results_comparison": {
        "es": "Comparación de Resultados",
        "en": "Results Comparison"
    },
    
    # Validation messages
    "valid_interval": {
        "es": "Intervalo válido",
        "en": "Valid interval"
    },
    "valid_variable": {
        "es": "Variable válida",
        "en": "Valid variable"
    },
    "variable_warning": {
        "es": "La variable debe ser una sola letra",
        "en": "Variable should be a single letter"
    },
    "good_subdivisions": {
        "es": "Buen número de subdivisiones",
        "en": "Good number of subdivisions"
    },
    "low_subdivisions_warning": {
        "es": "Pocas subdivisiones pueden dar resultados imprecisos",
        "en": "Few subdivisions may give imprecise results"
    },
    "high_subdivisions_warning": {
        "es": "Muchas subdivisiones pueden ralentizar el cálculo",
        "en": "Many subdivisions may slow down calculation"
    },
    "subdivisions_help": {
        "es": "Número de rectángulos para la aproximación de Riemann",
        "en": "Number of rectangles for Riemann approximation"
    }
}

def get_text(key: str, **kwargs) -> str:
    """
    Get translated text for the current language.
    
    Args:
        key (str): Translation key
        **kwargs: Optional parameters for string formatting
    
    Returns:
        str: Translated text
    """
    # Get current language from session state, default to Spanish
    current_language = st.session_state.get("language", "es")
    
    # Get translation, fallback to key if not found
    if key in TRANSLATIONS:
        translation = TRANSLATIONS[key].get(current_language, TRANSLATIONS[key].get("es", key))
    else:
        translation = key
    
    # Apply formatting if kwargs provided
    if kwargs:
        try:
            translation = translation.format(**kwargs)
        except (KeyError, ValueError):
            # If formatting fails, return original translation
            pass
    
    return translation

def get_available_languages() -> dict:
    """
    Get available languages.
    
    Returns:
        dict: Available languages
    """
    return LANGUAGES

def set_language(language_code: str):
    """
    Set the current language.
    
    Args:
        language_code (str): Language code (es, en)
    """
    if language_code in LANGUAGES:
        st.session_state.language = language_code
    else:
        st.session_state.language = "es"  # Default to Spanish
