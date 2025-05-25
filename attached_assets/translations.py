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
        Una integral definida calcula el área con signo entre una función y el eje x sobre un intervalo especificado.
        
        La integral definida de una función f(x) de a a b se escribe como:
        """,
        "en": """
        A definite integral calculates the signed area between a function and the x-axis over a specified interval.
        
        The definite integral of a function f(x) from a to b is written as:
        """
    },
    "fundamental_theorem": {
        "es": "El Teorema Fundamental del Cálculo",
        "en": "The Fundamental Theorem of Calculus"
    },
    "fundamental_theorem_explanation": {
        "es": "La integral definida puede calcularse usando antiderivadas:",
        "en": "The definite integral can be calculated using antiderivatives:"
    },
    "where_f_is_antiderivative": {
        "es": "donde F(x) es una antiderivada de f(x), es decir, F'(x) = f(x).",
        "en": "where F(x) is an antiderivative of f(x), meaning F'(x) = f(x)."
    },
    "properties_definite_integrals": {
        "es": "Propiedades de las Integrales Definidas",
        "en": "Properties of Definite Integrals"
    },
    "applications": {
        "es": "Aplicaciones",
        "en": "Applications"
    },
    "area_under_curve": {
        "es": "Área bajo una curva",
        "en": "Area under a curve"
    },
    "volume_solids": {
        "es": "Volumen de sólidos",
        "en": "Volume of solids"
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
    
    # Riemann sum theory
    "what_is_riemann_sum": {
        "es": "¿Qué es una Suma de Riemann?",
        "en": "What is a Riemann Sum?"
    },
    "riemann_sum_explanation": {
        "es": """
        Una suma de Riemann es un método para aproximar la integral definida (o área bajo una curva) 
        dividiendo el área en formas más simples (rectángulos) cuyas áreas son fáciles de calcular.
        """,
        "en": """
        A Riemann sum is a method for approximating the definite integral (or area under a curve)
        by dividing the area into simpler shapes (rectangles) whose areas are easy to calculate.
        """
    },
    "types_riemann_sums": {
        "es": "Tipos de Sumas de Riemann",
        "en": "Types of Riemann Sums"
    },
    "left_method_explanation": {
        "es": "Utiliza el valor de la función en el extremo izquierdo de cada subintervalo.",
        "en": "Uses the function value at the left endpoint of each subinterval."
    },
    "right_method_explanation": {
        "es": "Utiliza el valor de la función en el extremo derecho de cada subintervalo.",
        "en": "Uses the function value at the right endpoint of each subinterval."
    },
    "midpoint_method_explanation": {
        "es": "Utiliza el valor de la función en el punto medio de cada subintervalo.",
        "en": "Uses the function value at the midpoint of each subinterval."
    },
    "the_formula": {
        "es": "La Fórmula",
        "en": "The Formula"
    },
    "riemann_formula_explanation": {
        "es": """
        Para una función f(x) en un intervalo [a, b] dividido en n subintervalos iguales, 
        la suma de Riemann es:
        """,
        "en": """
        For a function f(x) on an interval [a, b] divided into n equal subintervals,
        the Riemann sum is:
        """
    },
    "where_explanation": {
        "es": """
        donde:
        - Δx = (b-a)/n es el ancho de cada subintervalo
        - x*ᵢ es el punto de muestra en el i-ésimo subintervalo
        """,
        "en": """
        where:
        - Δx = (b-a)/n is the width of each subinterval
        - x*ᵢ is the sample point in the i-th subinterval
        """
    },
    "connection_definite_integrals": {
        "es": "Conexión con Integrales Definidas",
        "en": "Connection with Definite Integrals"
    },
    "convergence_explanation": {
        "es": """
        A medida que aumenta el número de subintervalos, la suma de Riemann se aproxima a la integral definida:
        """,
        "en": """
        As the number of subintervals increases, the Riemann sum approaches the definite integral:
        """
    },
    "fundamental_connection": {
        "es": "Esta es la conexión fundamental entre las sumas de Riemann y las integrales definidas.",
        "en": "This is the fundamental connection between Riemann sums and definite integrals."
    },
    
    # Area between curves theory
    "area_between_curves_calculation": {
        "es": "Cálculo del Área Entre Curvas",
        "en": "Area Between Curves Calculation"
    },
    "area_between_curves_theory": {
        "es": """
        Para encontrar el área entre dos curvas y = f(x) y y = g(x) de x = a a x = b, 
        usamos la fórmula:
        """,
        "en": """
        To find the area between two curves y = f(x) and y = g(x) from x = a to x = b,
        we use the formula:
        """
    },
    "practice_determination": {
        "es": """
        En la práctica, necesitamos determinar qué función tiene valores mayores en el intervalo dado. 
        Si f(x) ≥ g(x) para toda x en [a, b], entonces:
        """,
        "en": """
        In practice, we need to determine which function has greater values in the given interval.
        If f(x) ≥ g(x) for all x in [a, b], then:
        """
    },
    "when_curves_intersect": {
        "es": "Cuando las Curvas se Intersectan",
        "en": "When Curves Intersect"
    },
    "intersection_procedure": {
        "es": """
        Si las curvas se intersectan dentro del intervalo [a, b], necesitamos:
        
        1. Encontrar los puntos de intersección
        2. Dividir la integral en estos puntos
        3. Asegurar que siempre restamos la curva inferior de la superior
        """,
        "en": """
        If the curves intersect within the interval [a, b], we need to:
        
        1. Find the intersection points
        2. Split the integral at these points
        3. Ensure we're always subtracting the lower curve from the upper curve
        """
    },
    "important_considerations": {
        "es": "Consideraciones Importantes",
        "en": "Important Considerations"
    },
    "area_always_positive": {
        "es": "El área entre curvas siempre es positiva",
        "en": "The area between curves is always positive"
    },
    "y_axis_integration": {
        "es": "Al encontrar el área con respecto al eje y, usar ∫[c,d] |f⁻¹(y) - g⁻¹(y)| dy",
        "en": "When finding area with respect to y-axis, use ∫[c,d] |f⁻¹(y) - g⁻¹(y)| dy"
    },
    "complex_regions_advice": {
        "es": "Para regiones complejas, dividir el problema en partes más simples",
        "en": "For complex regions, break the problem into simpler parts"
    },
    "practical_applications": {
        "es": "Aplicaciones Prácticas",
        "en": "Practical Applications"
    },
    "physics_applications": {
        "es": "Aplicaciones en física: trabajo, energía, flujo",
        "en": "Physics applications: work, energy, flow"
    },
    "economics_applications": {
        "es": "Aplicaciones en economía: excedente del consumidor y productor",
        "en": "Economics applications: consumer and producer surplus"
    },
    "engineering_applications_detailed": {
        "es": "Aplicaciones en ingeniería: análisis de materiales, distribución de carga",
        "en": "Engineering applications: material analysis, load distribution"
    },
    "geometry_applications": {
        "es": "Aplicaciones en geometría: áreas irregulares, centroides",
        "en": "Geometry applications: irregular areas, centroids"
    },
    
    # Software Engineering Scenarios
    "engineering_scenario_generator": {
        "es": "Generador de Escenarios de Ingeniería de Software",
        "en": "Software Engineering Scenario Generator"
    },
    "scenario_generator_description": {
        "es": """
        Esta sección genera automáticamente problemas de cálculo integral aplicados a situaciones reales 
        de ingeniería de software. Estos problemas representan casos prácticos donde el cálculo integral 
        es útil para modelar y resolver desafíos comunes en el desarrollo y operación de software.
        """,
        "en": """
        This section automatically generates integral calculus problems applied to real situations
        in software engineering. These problems represent practical cases where integral calculus
        is useful for modeling and solving common challenges in software development and operation.
        """
    },
    "generate_new_scenario": {
        "es": "Generar Nuevo Escenario",
        "en": "Generate New Scenario"
    },
    "problem_description": {
        "es": "Descripción del Problema",
        "en": "Problem Description"
    },
    "solve_problem": {
        "es": "Resolver el Problema",
        "en": "Solve the Problem"
    },
    "function_to_integrate": {
        "es": "Función a integrar",
        "en": "Function to integrate"
    },
    "first_function": {
        "es": "Primera función",
        "en": "First function"
    },
    "second_function": {
        "es": "Segunda función",
        "en": "Second function"
    },
    "software_engineering_interpretation": {
        "es": "Interpretación en Ingeniería de Software",
        "en": "Software Engineering Interpretation"
    },
    "specific_result": {
        "es": "Resultado Específico",
        "en": "Specific Result"
    },
    "calculated_value": {
        "es": "Valor calculado",
        "en": "Calculated value"
    },
    "for_problem": {
        "es": "Para el problema",
        "en": "For the problem"
    },
    "in_interval": {
        "es": "en el intervalo",
        "en": "in the interval"
    },
    "of": {
        "es": "de",
        "en": "of"
    },
    "scenario_info": {
        "es": "Información del Escenario",
        "en": "Scenario Info"
    },
    "calculation_type": {
        "es": "Tipo de cálculo",
        "en": "Calculation type"
    },
    "domain": {
        "es": "Dominio",
        "en": "Domain"
    },
    "function": {
        "es": "Función",
        "en": "Function"
    },
    "resolution_tips": {
        "es": "Consejos para la Resolución",
        "en": "Resolution Tips"
    },
    "software_engineering_context": {
        "es": "Contexto de Ingeniería de Software",
        "en": "Software Engineering Context"
    },
    "why_calculus_in_software": {
        "es": "¿Por qué Cálculo en Software?",
        "en": "Why Calculus in Software?"
    },
    "calculus_software_explanation": {
        "es": """
        El cálculo integral es fundamental en ingeniería de software para:
        - Modelar el rendimiento y consumo de recursos a lo largo del tiempo
        - Analizar la complejidad algorítmica y optimización
        - Calcular métricas acumulativas como tiempo total de ejecución
        - Predecir el comportamiento del sistema bajo diferentes cargas
        """,
        "en": """
        Integral calculus is fundamental in software engineering for:
        - Modeling performance and resource consumption over time
        - Analyzing algorithmic complexity and optimization
        - Calculating cumulative metrics like total execution time
        - Predicting system behavior under different loads
        """
    },
    "real_world_examples": {
        "es": "Ejemplos del Mundo Real",
        "en": "Real World Examples"
    },
    
    # Scenario titles and descriptions
    "server_resource_consumption": {
        "es": "Consumo de Recursos del Servidor",
        "en": "Server Resource Consumption"
    },
    "server_memory_description": {
        "es": "Un servidor web tiene un consumo de recursos de memoria modelado por la función M(t) = t² + 2t + 1 MB, donde t es el tiempo en minutos desde que inició el proceso. Calcula el total de recursos utilizados durante los primeros {n} minutos.",
        "en": "A web server has memory resource consumption modeled by the function M(t) = t² + 2t + 1 MB, where t is time in minutes since the process started. Calculate the total resources used during the first {n} minutes."
    },
    "server_memory_interpretation": {
        "es": "Este resultado representa la cantidad total de memoria (en MB) consumida por el servidor durante el período de tiempo especificado. Esta información es crucial para planificar la capacidad y optimizar el rendimiento del servidor.",
        "en": "This result represents the total amount of memory (in MB) consumed by the server during the specified time period. This information is crucial for capacity planning and server performance optimization."
    },
    
    "database_optimization": {
        "es": "Optimización de Base de Datos",
        "en": "Database Optimization"
    },
    "database_query_description": {
        "es": "La velocidad de consulta en una base de datos se modela mediante la función V(n) = 3n² + 2n + 1 milisegundos, donde n representa el tamaño del conjunto de datos. Calcula el tiempo acumulado para consultas con tamaños desde {a} hasta {b}.",
        "en": "Query speed in a database is modeled by the function V(n) = 3n² + 2n + 1 milliseconds, where n represents the dataset size. Calculate the accumulated time for queries with sizes from {a} to {b}."
    },
    "database_query_interpretation": {
        "es": "Este resultado representa el tiempo total acumulado (en milisegundos) para procesar consultas de diferentes tamaños. Esto ayuda a identificar cuellos de botella y optimizar el rendimiento de la base de datos.",
        "en": "This result represents the total accumulated time (in milliseconds) to process queries of different sizes. This helps identify bottlenecks and optimize database performance."
    },
    
    "user_interaction": {
        "es": "Interacción de Usuarios",
        "en": "User Interaction"
    },
    "user_load_description": {
        "es": "La tasa de usuarios que interactúan con una aplicación web sigue la función U(t) = 50e^(-0.2t) usuarios por minuto, donde t es el tiempo en minutos desde el lanzamiento. Calcula el número total de usuarios que interactuaron durante las primeras {n} horas.",
        "en": "The rate of users interacting with a web application follows the function U(t) = 50e^(-0.2t) users per minute, where t is time in minutes since launch. Calculate the total number of users who interacted during the first {n} hours."
    },
    "user_load_interpretation": {
        "es": "Este resultado representa el número total de usuarios que interactuaron con la aplicación durante el período especificado. Esto es útil para analizar patrones de uso y planificar la capacidad del sistema.",
        "en": "This result represents the total number of users who interacted with the application during the specified period. This is useful for analyzing usage patterns and planning system capacity."
    },
    
    "cpu_memory_difference": {
        "es": "Diferencia entre Uso de CPU y Memoria",
        "en": "CPU and Memory Usage Difference"
    },
    "cpu_memory_comparison_description": {
        "es": "Un proceso de computación utiliza CPU según la función C(t) = 2t + 5 unidades y memoria según M(t) = t² + 2t + 1 unidades, donde t es el tiempo en minutos. Calcula la diferencia acumulada entre estos recursos durante un período de {a} a {b} minutos.",
        "en": "A computation process uses CPU according to the function C(t) = 2t + 5 units and memory according to M(t) = t² + 2t + 1 units, where t is time in minutes. Calculate the accumulated difference between these resources during a period from {a} to {b} minutes."
    },
    "cpu_memory_comparison_interpretation": {
        "es": "Este resultado representa la diferencia acumulada entre el uso de memoria y CPU durante el período especificado. Un valor positivo indica que el proceso es más intensivo en memoria, mientras que un valor negativo indica que es más intensivo en CPU.",
        "en": "This result represents the accumulated difference between memory and CPU usage during the specified period. A positive value indicates the process is more memory-intensive, while a negative value indicates it's more CPU-intensive."
    },
    
    "algorithm_performance": {
        "es": "Rendimiento de Algoritmos",
        "en": "Algorithm Performance"
    },
    "algorithm_comparison_description": {
        "es": "Dos algoritmos de ordenamiento tienen tiempos de ejecución modelados por A₁(n) = 0.1n² + n y A₂(n) = 5n·log(n), donde n es el tamaño de la entrada. Determina para qué tamaños de entrada el primer algoritmo supera al segundo calculando el área entre las curvas desde n = {a} hasta n = {b}.",
        "en": "Two sorting algorithms have execution times modeled by A₁(n) = 0.1n² + n and A₂(n) = 5n·log(n), where n is the input size. Determine for which input sizes the first algorithm outperforms the second by calculating the area between curves from n = {a} to n = {b}."
    },
    "algorithm_comparison_interpretation": {
        "es": "Este resultado ayuda a identificar los rangos de tamaños de entrada donde un algoritmo supera al otro. Esta información es crucial para seleccionar el algoritmo óptimo según el tamaño de los datos.",
        "en": "This result helps identify the ranges of input sizes where one algorithm outperforms the other. This information is crucial for selecting the optimal algorithm based on data size."
    },
    
    "software_complexity_growth": {
        "es": "Crecimiento de la Complejidad de Software",
        "en": "Software Complexity Growth"
    },
    "complexity_growth_description": {
        "es": "La complejidad de un sistema de software crece según la función C(t) = t³ - 2t² + 3t, donde t es el tiempo en meses desde el inicio del proyecto. Calcula el incremento total de complejidad entre los meses {a} y {b}.",
        "en": "The complexity of a software system grows according to the function C(t) = t³ - 2t² + 3t, where t is time in months since project start. Calculate the total complexity increase between months {a} and {b}."
    },
    "complexity_growth_interpretation": {
        "es": "Este resultado representa el aumento acumulado en la complejidad del software durante el período especificado. Entender este crecimiento es esencial para la planificación de refactorizaciones y mantenimiento del código.",
        "en": "This result represents the accumulated increase in software complexity during the specified period. Understanding this growth is essential for planning refactorizations and code maintenance."
    },
    
    "software_reliability": {
        "es": "Fiabilidad del Software",
        "en": "Software Reliability"
    },
    "failure_rate_description": {
        "es": "La tasa de fallos de un sistema sigue la función F(t) = 10e^(-0.5t) fallos por día, donde t es el tiempo en días desde el despliegue. Calcula el número esperado de fallos durante los primeros {n} días.",
        "en": "The failure rate of a system follows the function F(t) = 10e^(-0.5t) failures per day, where t is time in days since deployment. Calculate the expected number of failures during the first {n} days."
    },
    "failure_rate_interpretation": {
        "es": "Este resultado representa el número total esperado de fallos durante el período especificado. Esta información es valiosa para la planificación de pruebas y garantía de calidad.",
        "en": "This result represents the total expected number of failures during the specified period. This information is valuable for test planning and quality assurance."
    },
    
    "parallel_processing_performance": {
        "es": "Rendimiento en Procesamiento Paralelo",
        "en": "Parallel Processing Performance"
    },
    "parallel_efficiency_description": {
        "es": "La eficiencia de un sistema de procesamiento paralelo varía según la función E(n) = 1 - log(n)/n, donde n es el número de núcleos. Calcula la eficiencia acumulada cuando el sistema escala de {a} a {b} núcleos.",
        "en": "The efficiency of a parallel processing system varies according to the function E(n) = 1 - log(n)/n, where n is the number of cores. Calculate the accumulated efficiency when the system scales from {a} to {b} cores."
    },
    "parallel_efficiency_interpretation": {
        "es": "Este resultado representa la eficiencia acumulada a medida que el sistema escala en el número de núcleos. Esto ayuda a determinar el punto óptimo de paralelización para maximizar el rendimiento.",
        "en": "This result represents the accumulated efficiency as the system scales in the number of cores. This helps determine the optimal point of parallelization to maximize performance."
    },
    
    # Tips and examples
    "tip_understand_function": {
        "es": "Asegúrate de entender qué representa físicamente la función",
        "en": "Make sure you understand what the function physically represents"
    },
    "tip_check_bounds": {
        "es": "Verifica que los límites de integración sean apropiados",
        "en": "Check that the integration bounds are appropriate"
    },
    "tip_interpret_result": {
        "es": "Interpreta el resultado en el contexto del problema",
        "en": "Interpret the result in the context of the problem"
    },
    "tip_identify_upper_lower": {
        "es": "Identifica cuál función está arriba y cuál abajo",
        "en": "Identify which function is above and which is below"
    },
    "tip_check_intersections": {
        "es": "Revisa si hay puntos de intersección en el intervalo",
        "en": "Check if there are intersection points in the interval"
    },
    "tip_area_meaning": {
        "es": "Comprende qué significa el área en el contexto del problema",
        "en": "Understand what the area means in the problem context"
    },
    
    "performance_optimization": {
        "es": "Optimización de rendimiento",
        "en": "Performance optimization"
    },
    "resource_management": {
        "es": "Gestión de recursos",
        "en": "Resource management"
    },
    "algorithm_analysis": {
        "es": "Análisis de algoritmos",
        "en": "Algorithm analysis"
    },
    "system_modeling": {
        "es": "Modelado de sistemas",
        "en": "System modeling"
    },
    "quality_metrics": {
        "es": "Métricas de calidad",
        "en": "Quality metrics"
    },
    "capacity_planning": {
        "es": "Planificación de capacidad",
        "en": "Capacity planning"
    },
    
    "load_balancing_example": {
        "es": "Balanceadores de carga que distribuyen tráfico según funciones matemáticas",
        "en": "Load balancers that distribute traffic according to mathematical functions"
    },
    "caching_strategy_example": {
        "es": "Estrategias de caché que optimizan el tiempo de acceso",
        "en": "Caching strategies that optimize access time"
    },
    "database_optimization_example": {
        "es": "Optimización de consultas basada en análisis de complejidad",
        "en": "Query optimization based on complexity analysis"
    },
    "network_traffic_example": {
        "es": "Análisis de tráfico de red para predecir congestiones",
        "en": "Network traffic analysis to predict congestion"
    },
    
    # Error messages and validation
    "empty_function": {
        "es": "Por favor, ingresa una función.",
        "en": "Please enter a function."
    },
    "empty_bounds": {
        "es": "Por favor, ingresa los límites de integración.",
        "en": "Please enter the integration bounds."
    },
    "invalid_interval": {
        "es": "El límite superior debe ser mayor que el límite inferior.",
        "en": "The upper bound must be greater than the lower bound."
    },
    "invalid_subdivisions": {
        "es": "El número de subdivisiones debe ser positivo.",
        "en": "The number of subdivisions must be positive."
    },
    "enter_both_functions": {
        "es": "Por favor, ingresa ambas funciones.",
        "en": "Please enter both functions."
    },
    "fill_all_fields": {
        "es": "Por favor, completa todos los campos.",
        "en": "Please fill in all fields."
    },
    "comparison_error": {
        "es": "Error en la comparación",
        "en": "Comparison error"
    },
    "intersection_error": {
        "es": "Error al encontrar intersecciones",
        "en": "Error finding intersections"
    },
    "calculation_error": {
        "es": "Error de cálculo",
        "en": "Calculation error"
    },
    "unexpected_error": {
        "es": "Error inesperado",
        "en": "Unexpected error"
    },
    "error_loading_page": {
        "es": "Error al cargar la página",
        "en": "Error loading page"
    },
    
    # Input help and validation
    "function_input_help": {
        "es": "Usa ^ para potencias, * para multiplicación, sin/cos/tan para trigonométricas, exp para exponencial, ln para logaritmo natural, pi para π, e para e",
        "en": "Use ^ for powers, * for multiplication, sin/cos/tan for trigonometric, exp for exponential, ln for natural log, pi for π, e for e"
    },
    "bound_help": {
        "es": "Puedes usar números, pi, e, o expresiones como pi/2",
        "en": "You can use numbers, pi, e, or expressions like pi/2"
    },
    "variable_help": {
        "es": "Variable de integración (por defecto: x)",
        "en": "Integration variable (default: x)"
    },
    "intersection_help": {
        "es": "Encuentra automáticamente dónde se cruzan las funciones",
        "en": "Automatically find where the functions intersect"
    },
    "math_input_help": {
        "es": "Ejemplo: x^2 + 3*x + sin(x)",
        "en": "Example: x^2 + 3*x + sin(x)"
    },
    
    # Math keyboard and input components
    "preview": {
        "es": "Vista previa",
        "en": "Preview"
    },
    "invalid_expression": {
        "es": "Expresión inválida",
        "en": "Invalid expression"
    },
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
    "function_examples": {
        "es": "Ejemplos de Funciones",
        "en": "Function Examples"
    },
    "polynomial_functions": {
        "es": "Funciones Polinómiales",
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
    
    # Error handling
    "empty_expression": {
        "es": "La expresión está vacía",
        "en": "Expression is empty"
    },
    "variable_not_found": {
        "es": "Variable no encontrada",
        "en": "Variable not found"
    },
    "invalid_syntax": {
        "es": "Sintaxis inválida",
        "en": "Invalid syntax"
    },
    "error_parsing_expression": {
        "es": "Error al analizar la expresión",
        "en": "Error parsing expression"
    },
    "cannot_convert_to_number": {
        "es": "No se puede convertir a número",
        "en": "Cannot convert to number"
    },
    "invalid_input_type": {
        "es": "Tipo de entrada inválido",
        "en": "Invalid input type"
    },
    "error_evaluating_expression": {
        "es": "Error al evaluar la expresión",
        "en": "Error evaluating expression"
    },
    "error_solving_integral": {
        "es": "Error al resolver la integral",
        "en": "Error solving integral"
    },
    "error_finding_derivative": {
        "es": "Error al encontrar la derivada",
        "en": "Error finding derivative"
    },
    "error_solving_equation": {
        "es": "Error al resolver la ecuación",
        "en": "Error solving equation"
    },
    "error_creating_plot_data": {
        "es": "Error al crear datos del gráfico",
        "en": "Error creating plot data"
    },
    "error_plotting_function": {
        "es": "Error al graficar la función",
        "en": "Error plotting function"
    },
    "error_plotting_integral": {
        "es": "Error al graficar la integral",
        "en": "Error plotting integral"
    },
    "error_plotting_riemann": {
        "es": "Error al graficar la suma de Riemann",
        "en": "Error plotting Riemann sum"
    },
    "error_plotting_area": {
        "es": "Error al graficar el área",
        "en": "Error plotting area"
    },
    "error_finding_intersections": {
        "es": "Error al encontrar intersecciones",
        "en": "Error finding intersections"
    },
    "error_calculating_area": {
        "es": "Error al calcular el área",
        "en": "Error calculating area"
    },
    "error_calculating_area_y": {
        "es": "Error al calcular el área con respecto a y",
        "en": "Error calculating area with respect to y"
    },
    "error_calculating_centroid": {
        "es": "Error al calcular el centroide",
        "en": "Error calculating centroid"
    },
    "error_calculating_riemann": {
        "es": "Error al calcular la suma de Riemann",
        "en": "Error calculating Riemann sum"
    },
    "error_evaluating_at_point": {
        "es": "Error al evaluar en el punto",
        "en": "Error evaluating at point"
    },
    "error_generating_steps": {
        "es": "Error al generar los pasos",
        "en": "Error generating steps"
    },
    "invalid_method": {
        "es": "Método inválido",
        "en": "Invalid method"
    },
    
    # Solution display content
    "additional_info": {
        "es": "Información Adicional",
        "en": "Additional Information"
    },
    "interpretation": {
        "es": "Interpretación",
        "en": "Interpretation"
    },
    "integral_interpretation": {
        "es": "Esta integral representa el área neta entre la función y el eje x en el intervalo dado.",
        "en": "This integral represents the net area between the function and the x-axis over the given interval."
    },
    "positive_result_meaning": {
        "es": "Un resultado positivo indica que la función está principalmente por encima del eje x.",
        "en": "A positive result indicates the function is mainly above the x-axis."
    },
    "negative_result_meaning": {
        "es": "Un resultado negativo indica que la función está principalmente por debajo del eje x.",
        "en": "A negative result indicates the function is mainly below the x-axis."
    },
    "integral_calculation": {
        "es": "Cálculo de Integral",
        "en": "Integral Calculation"
    },
    "riemann_sum_solution": {
        "es": "Solución de Suma de Riemann",
        "en": "Riemann Sum Solution"
    },
    "calculating_riemann_sum": {
        "es": "Calculando la suma de Riemann",
        "en": "Calculating the Riemann sum"
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
        "es": "La suma de Riemann aproxima el área bajo la curva",
        "en": "The Riemann sum approximates the area under the curve"
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
        "es": "En este cálculo, usamos el método",
        "en": "In this calculation, we used the method"
    },
    "left_endpoint_explanation": {
        "es": "La altura de cada rectángulo se determina por el valor de la función en el punto izquierdo de cada subintervalo.",
        "en": "The height of each rectangle is determined by the function value at the left endpoint of each subinterval."
    },
    "right_endpoint_explanation": {
        "es": "La altura de cada rectángulo se determina por el valor de la función en el punto derecho de cada subintervalo.",
        "en": "The height of each rectangle is determined by the function value at the right endpoint of each subinterval."
    },
    "midpoint_explanation": {
        "es": "La altura de cada rectángulo se determina por el valor de la función en el punto medio de cada subintervalo.",
        "en": "The height of each rectangle is determined by the function value at the midpoint of each subinterval."
    },
    "riemann_sum_calculation": {
        "es": "Cálculo de Suma de Riemann para",
        "en": "Riemann Sum Calculation for"
    },
    "method": {
        "es": "Método",
        "en": "Method"
    },
    "area_between_curves_solution": {
        "es": "Solución de Área Entre Curvas",
        "en": "Area Between Curves Solution"
    },
    "calculating_area_between": {
        "es": "Calculando el área entre",
        "en": "Calculating the area between"
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
        "es": "El área entre curvas calcula la región encerrada por dos funciones",
        "en": "The area between curves calculates the region enclosed by two functions"
    },
    "area_formula": {
        "es": "Esta área puede calcularse usando la integral definida",
        "en": "This area can be calculated using the definite integral"
    },
    "area": {
        "es": "Área",
        "en": "Area"
    },
    "area_practice": {
        "es": "En la práctica, determinamos qué función tiene valores mayores en el intervalo y restamos la función inferior de la superior",
        "en": "In practice, we determine which function has greater values in the interval and subtract the lower function from the upper one"
    },
    "upper_function": {
        "es": "función superior",
        "en": "upper function"
    },
    "lower_function": {
        "es": "función inferior",
        "en": "lower function"
    },
    "physical_applications": {
        "es": "Cálculo de trabajo, energía cinética, flujo de fluidos",
        "en": "Calculation of work, kinetic energy, fluid flow"
    },
    "economic_applications": {
        "es": "Excedente del consumidor y productor en economía",
        "en": "Consumer and producer surplus in economics"
    },
    "engineering_applications": {
        "es": "Análisis de materiales, distribución de cargas",
        "en": "Material analysis, load distribution"
    },
    "area_between_curves_calculation": {
        "es": "Cálculo de Área Entre Curvas para",
        "en": "Area Between Curves Calculation for"
    },
    
    # Error display
    "error_details": {
        "es": "Detalles del Error",
        "en": "Error Details"
    },
    "suggestions": {
        "es": "Sugerencias",
        "en": "Suggestions"
    },
    "check_syntax": {
        "es": "Verifica la sintaxis de la expresión matemática",
        "en": "Check the syntax of the mathematical expression"
    },
    "use_star_multiplication": {
        "es": "Usa * para multiplicación explícita (ej: 2*x en lugar de 2x)",
        "en": "Use * for explicit multiplication (e.g., 2*x instead of 2x)"
    },
    "check_parentheses": {
        "es": "Asegúrate de que los paréntesis estén balanceados",
        "en": "Make sure parentheses are balanced"
    },
    "use_valid_functions": {
        "es": "Usa funciones válidas: sin, cos, tan, exp, ln, sqrt, etc.",
        "en": "Use valid functions: sin, cos, tan, exp, ln, sqrt, etc."
    },
    "check_bounds_numeric": {
        "es": "Verifica que los límites sean valores numéricos válidos",
        "en": "Check that the bounds are valid numeric values"
    },
    "use_pi_for_pi": {
        "es": "Usa 'pi' para representar π",
        "en": "Use 'pi' to represent π"
    },
    "use_e_for_e": {
        "es": "Usa 'e' para representar el número e",
        "en": "Use 'e' to represent Euler's number"
    },
    "check_domain": {
        "es": "Verifica que la función esté definida en todo el dominio",
        "en": "Check that the function is defined over the entire domain"
    },
    "avoid_division_zero": {
        "es": "Evita divisiones por cero",
        "en": "Avoid division by zero"
    },
    "check_complex_results": {
        "es": "Verifica si hay resultados complejos o indefinidos",
        "en": "Check for complex or undefined results"
    },
    
    # Calculation summary
    "calculation_summary": {
        "es": "Resumen del Cálculo",
        "en": "Calculation Summary"
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
        "es": "Resultado positivo",
        "en": "Positive result"
    },
    "result_negative": {
        "es": "Resultado negativo",
        "en": "Negative result"
    },
    
    # Steps in calculations
    "derivative_order": {
        "es": "Derivada de orden",
        "en": "Derivative of order"
    },
    "equation_to_solve": {
        "es": "Ecuación a resolver",
        "en": "Equation to solve"
    },
    "solutions": {
        "es": "Soluciones",
        "en": "Solutions"
    },
    "no_real_solutions": {
        "es": "No hay soluciones reales",
        "en": "No real solutions"
    },
    "setup_area_calculation": {
        "es": "Configurar el cálculo del área",
        "en": "Set up the area calculation"
    },
    "function1": {
        "es": "Función 1",
        "en": "Function 1"
    },
    "function2": {
        "es": "Función 2",
        "en": "Function 2"
    },
    "interval": {
        "es": "Intervalo",
        "en": "Interval"
    },
    "intersections_found": {
        "es": "Intersecciones encontradas",
        "en": "Intersections found"
    },
    "split_intervals": {
        "es": "Dividir el intervalo en los puntos de intersección",
        "en": "Split the interval at intersection points"
    },
    "calculate_area_segments": {
        "es": "Calcular el área para cada segmento",
        "en": "Calculate area for each segment"
    },
    "segment": {
        "es": "Segmento",
        "en": "Segment"
    },
    "total_area": {
        "es": "Área total",
        "en": "Total area"
    },
    "area_wrt_y": {
        "es": "Área con respecto a y",
        "en": "Area with respect to y"
    },
    "solve_for_x_in_terms_of_y": {
        "es": "Resolver para x en términos de y",
        "en": "Solve for x in terms of y"
    },
    "zero_area_centroid": {
        "es": "El área es cero, no se puede calcular el centroide",
        "en": "Area is zero, cannot calculate centroid"
    },
    "centroid_calculation": {
        "es": "Cálculo del centroide",
        "en": "Centroid calculation"
    },
    "centroid": {
        "es": "Centroide",
        "en": "Centroid"
    }
}

def get_text(key: str, **kwargs) -> str:
    """
    Get translated text for the current language.
    
    Args:
        key (str): Translation key
        **kwargs: Optional formatting parameters
        
    Returns:
        str: Translated text
    """
    # Get current language from session state, default to Spanish
    current_language = st.session_state.get("language", "es")
    
    # Get translation
    if key in TRANSLATIONS:
        text = TRANSLATIONS[key].get(current_language, TRANSLATIONS[key].get("es", key))
        
        # Format text if kwargs provided
        if kwargs:
            try:
                return text.format(**kwargs)
            except:
                return text
        return text
    else:
        # Return key if translation not found
        return key

def set_language(language_code: str):
    """
    Set the current language.
    
    Args:
        language_code (str): Language code ('es' or 'en')
    """
    if language_code in LANGUAGES:
        st.session_state.language = language_code
    else:
        st.session_state.language = "es"  # Default to Spanish

def get_current_language() -> str:
    """
    Get the current language code.
    
    Returns:
        str: Current language code
    """
    return st.session_state.get("language", "es")

def is_spanish() -> bool:
    """
    Check if current language is Spanish.
    
    Returns:
        bool: True if Spanish, False otherwise
    """
    return get_current_language() == "es"

def is_english() -> bool:
    """
    Check if current language is English.
    
    Returns:
        bool: True if English, False otherwise
    """
    return get_current_language() == "en"
