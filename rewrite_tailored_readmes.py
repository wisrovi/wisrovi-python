#!/usr/bin/env python3
"""
Reescritura Contextual y Rigurosa de TODOS los README.md del Repositorio.
Elimina textos genéricos repetitivos ('Modelo de Aprendizaje Activo') y asegura
que CADA README contenga:
1. Un diagrama Mermaid que narra EXACTAMENTE el flujo técnico de su contenido específico.
2. Explicación profesional, técnica, concisa y sin relleno innecesario.
3. Instrucciones directas de uso o ejecución.
"""

import os
import glob
from typing import Dict, Any, List

from all_32_classes_metadata import ALL_CLASSES, COURSES_CONFIG, AUTHOR_INFO, BASE_DIR

IGNORE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".system_generated",
    ".ruff_cache",
    ".idea",
    ".vscode",
    "site"
}

CLASS_META_MAP = {(m["course_num"], m["folder_name"]): m for m in ALL_CLASSES}

def get_class_specific_mermaid(meta: Dict[str, Any]) -> str:
    c_num = meta["course_num"]
    f_name = meta["folder_name"]
    title = meta["class_title"]
    
    # Diagramas específicos para cada una de las 32 clases
    if f_name == "clase-01-panorama-general":
        return """```mermaid
flowchart TD
    P1["1. El Megáfono<br/>print('Hola Mundo')"] --> P2["2. Las Cajas Etiquetadas<br/>edad = 25 (Variables)"]
    P2 --> P3{"3. El Semáforo<br/>¿edad >= 18? (if/else)"}
    P3 -->|Verdadero| P4["4. La Cinta Transportadora<br/>for item in lista (Bucles)"]
    P3 -->|Falso| P4
    P4 --> P5["5. La Licuadora<br/>def funcion(entradas) -> salida"]

    style P1 fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style P2 fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style P3 fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style P4 fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
    style P5 fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

    elif f_name == "clase-02-variables-y-tipos":
        return """```mermaid
flowchart LR
    VAL["Valor Literal ('45.90')"] --> STR["str (Texto Inmutable)"]
    STR --> CAST["Casting: float()"]
    CAST --> FLT["float (45.90)"]
    FLT --> TRUNC["Casting: int()"]
    TRUNC --> INT["int (45)"]
    INT --> MEM["Referencia en Memoria<br/>id(objeto)"]

    style VAL fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style STR fill:#334155,color:#fff,stroke:#94a3b8,stroke-width:2px
    style CAST fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style FLT fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style TRUNC fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style INT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style MEM fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
```"""

    elif f_name == "clase-03-control-flujo-condicionales":
        return """```mermaid
flowchart TD
    IN["Entrada de Datos"] --> EVAL{"¿Condición if principal?"}
    EVAL -->|True| B1["Bloque 1: Ejecutar código if"]
    EVAL -->|False| ELIF{"¿Condición secundaria elif?"}
    ELIF -->|True| B2["Bloque 2: Ejecutar código elif"]
    ELIF -->|False| ELSE["Bloque 3: Rama por defecto else"]
    B1 --> OUT["Continuación del Programa"]
    B2 --> OUT
    ELSE --> OUT

    style IN fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style EVAL fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style B1 fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style ELIF fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style B2 fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style ELSE fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
    style OUT fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
```"""

    elif f_name == "clase-04-control-flujo-bucles":
        return """```mermaid
flowchart TD
    INIT["Colección o Rango de Datos"] --> ITER["Iterador: for item in secuencia / while condicion"]
    ITER --> BODY["Ejecutar cuerpo del bucle"]
    BODY --> CTRL{"¿Control de Flujo?"}
    CTRL -->|continue| ITER
    CTRL -->|break| END["Salida Inmediata del Bucle"]
    CTRL -->|Flujo normal| NEXT{"¿Quedan elementos?"}
    NEXT -->|Sí| ITER
    NEXT -->|No| END

    style INIT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style ITER fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style BODY fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style CTRL fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style END fill:#334155,color:#fff,stroke:#94a3b8,stroke-width:2px
```"""

    elif f_name == "clase-05-listas-y-colecciones":
        return """```mermaid
flowchart LR
    L["Lista: ['A', 'B', 'C', 'D']"] --> OP["Operaciones de Mutación"]
    OP --> APP["append('E') ➔ Final"]
    OP --> INS["insert(1, 'X') ➔ Posición"]
    OP --> POP["pop() ➔ Extrae último"]
    L --> SLICE["Slicing [inicio:fin:paso]"]
    SLICE --> SUB["Sublistas & Reversión [::-1]"]

    style L fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style OP fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style APP fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style INS fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style POP fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
    style SLICE fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
```"""

    elif f_name == "clase-06-diccionarios":
        return """```mermaid
flowchart LR
    KEY["Clave: 'usuario'"] --> HASH["Función Hash Interna"]
    HASH --> BUCKET["Bucket / Posición en Memoria"]
    BUCKET --> VAL["Valor Asociado: 'wisrovi'"]
    BUCKET --> GET[".get(clave, default) ➔ Búsqueda O(1)"]
    BUCKET --> SET["set() ➔ Colección de Elementos Únicos"]

    style KEY fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style HASH fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style BUCKET fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style VAL fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style GET fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
    style SET fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
```"""

    elif f_name == "clase-07-funciones":
        return """```mermaid
flowchart TD
    CALL["Llamada: calcular(base=5, altura=3)"] --> FRAME["Push Stack Frame (Ámbito Local)"]
    FRAME --> SCOPE{"Resolución de Nombres LEGB"}
    SCOPE -->|1. Local| L_VAR["Variables de función"]
    SCOPE -->|2. Global| G_VAR["Módulo global"]
    SCOPE -->|3. Built-in| B_VAR["Funciones estándar (len, print)"]
    L_VAR --> RET["return resultado"]
    RET --> POP_F["Pop Stack Frame ➔ Devolver Control"]

    style CALL fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style FRAME fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style SCOPE fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style RET fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style POP_F fill:#334155,color:#fff,stroke:#94a3b8,stroke-width:2px
```"""

    elif f_name == "clase-08-proyecto-integrador-basico":
        return """```mermaid
flowchart TD
    CLI["Bucle Principal CLI"] --> MENU["Mostrar Opciones de Menú"]
    MENU --> IN["Lectura de Opción con try/except"]
    IN -->|1. Agregar| TM_ADD["TaskManager.agregar_tarea()"]
    IN -->|2. Listar| TM_LST["TaskManager.listar_tareas()"]
    IN -->|3. Salir| TM_EXT["Cierre Seguro del Programa"]
    TM_ADD --> STATE[("Estado en Memoria")]
    TM_LST --> STATE

    style CLI fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style MENU fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style IN fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style TM_ADD fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style TM_LST fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style STATE fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
```"""

    elif c_num == 2:
        # Curso 2: Algoritmos
        if "big-o" in f_name:
            return """```mermaid
flowchart LR
    O1["O(1) Constante<br/>Acceso a Dict/List"] --> ON["O(n) Lineal<br/>Búsqueda Secuencial"]
    ON --> OLOGN["O(n log n)<br/>MergeSort / Timsort"]
    OLOGN --> ON2["O(n²) Cuadrático<br/>Bucles Anidados"]

    style O1 fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style ON fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style OLOGN fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style ON2 fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
```"""
        elif "pilas" in f_name:
            return """```mermaid
flowchart LR
    subgraph Pila["🥞 Pila (Stack LIFO)"]
        P_IN["push(X) ➔ Tope"] --> P_OUT["pop() ➔ Extrae Tope"]
    end
    subgraph Cola["🚶‍♂️ Cola (Queue FIFO - deque)"]
        Q_IN["append(X) ➔ Final"] --> Q_OUT["popleft() ➔ Atiende Primero (O(1))"]
    end

    style Pila fill:#f8fafc,stroke:#3b82f6,stroke-width:2px
    style Cola fill:#f0fdf4,stroke:#10b981,stroke-width:2px
```"""
        elif "hash" in f_name:
            return """```mermaid
flowchart LR
    K["Clave 'email'"] --> H["hash('email') % Buckets"]
    H --> B["Index Bucket"]
    B --> V["Valor O(1)"]
    V --> TWOSUM["Two-Sum: Target - Num en Hashmap (O(n))"]

    style K fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style H fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style B fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style TWOSUM fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "busqueda" in f_name:
            return """```mermaid
flowchart TD
    ARR["Arreglo Ordenado: [1, 3, 5, 7, 9, 11]"] --> MID["Calcular Punto Medio (Mid)"]
    MID --> CMP{"¿Mid == Target?"}
    CMP -->|Sí| FOUND["🎯 Elemento Encontrado en O(log n)"]
    CMP -->|Menor| RIGHT["Descartar Mitad Izquierda (L = Mid + 1)"]
    CMP -->|Mayor| LEFT["Descartar Mitad Derecha (R = Mid - 1)"]
    RIGHT --> MID
    LEFT --> MID

    style ARR fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style MID fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style CMP fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style FOUND fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "ordenamiento" in f_name:
            return """```mermaid
flowchart TD
    L["Lista Desordenada [38, 27, 43, 3, 9]"] --> PIV["Seleccionar Pivote (43)"]
    PIV --> PART["Partición: [x < P] + [P] + [x > P]"]
    PART --> REC["QuickSort Recursivo en Sublistas"]
    REC --> SORTED["Lista Ordenada en O(n log n)"]

    style L fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style PIV fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style PART fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style SORTED fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "arboles" in f_name:
            return """```mermaid
flowchart TD
    R["Raíz: 10"] --> L["Izquierda: 5 (< 10)"]
    R --> D["Derecha: 15 (> 10)"]
    L --> LL["3 (< 5)"]
    L --> LR["7 (> 5)"]
    D --> DR["20 (> 15)"]

    style R fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
    style L fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style D fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style LL fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style LR fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style DR fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "grafos" in f_name:
            return """```mermaid
flowchart LR
    G["Grafo: Lista de Adyacencia"] --> BFS["BFS: Cola deque ➔ Exploración por Niveles"]
    G --> DFS["DFS: Pila / Recursión ➔ Exploración en Profundidad"]
    BFS --> VIS["Conjunto de Nodos Visitados (set)"]
    DFS --> VIS

    style G fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style BFS fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style DFS fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
    style VIS fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        else: # recursividad
            return """```mermaid
flowchart TD
    N["Llamada fib(n)"] --> CHK{"¿Está en Caché @lru_cache?"}
    CHK -->|Sí| HIT["🎯 Retorno Instantáneo O(1)"]
    CHK -->|No| CALC["Calcular fib(n-1) + fib(n-2)"]
    CALC --> STORE["Almacenar en Tabla DP"]
    STORE --> HIT

    style N fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style CHK fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style HIT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style STORE fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
```"""

    elif c_num == 3:
        # Curso 3: Agentes IA
        if "token" in f_name:
            return """```mermaid
flowchart LR
    TXT["Texto: 'Inteligencia Artificial'"] --> BPE["Tokenizador BPE"]
    BPE --> TOK["Tokens: ['Intelig', 'encia', ' Artific', 'ial']"]
    TOK --> IDS["IDs Numéricos: [4521, 8934, 120]"]
    IDS --> LLM["Modelo LLM (Inferencia)"]

    style TXT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style BPE fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style TOK fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style LLM fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
```"""
        elif "prompt" in f_name:
            return """```mermaid
flowchart TD
    SYS["System Prompt (Rol y Restricciones)"] --> CTX["Few-Shot Examples (Pares In-Context)"]
    CTX --> COT["Chain of Thought ('Pensemos paso a paso')"]
    COT --> USR["User Prompt"]
    USR --> LLM["LLM ➔ Respuesta Precisa y Sin Alucinaciones"]

    style SYS fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style CTX fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style COT fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style LLM fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "pydantic" in f_name:
            return """```mermaid
flowchart LR
    RAW["Raw JSON del LLM"] --> PYD["Pydantic BaseModel Validation"]
    PYD -->|Inválido| ERR["ValidationError (Reintentar con Prompt)"]
    PYD -->|Válido| DTO["Objeto Python Tipado (DTO)"]
    DTO --> APP["Consumo Seguro en Backend"]

    style RAW fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style PYD fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style ERR fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
    style DTO fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "tool" in f_name:
            return """```mermaid
flowchart TD
    Q["Usuario: '¿Clima en Madrid?'"] --> LLM["LLM detecta Tool Call: get_weather(city='Madrid')"]
    LLM --> DISP["Despachador de Herramientas Python"]
    DISP --> API["Ejecución de Función Python"]
    API --> OBS["Observación: '22°C Soleado'"]
    OBS --> LLM_FINAL["LLM sintetiza Respuesta Final en Lenguaje Natural"]

    style Q fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style LLM fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
    style DISP fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style API fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style LLM_FINAL fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "embedding" in f_name:
            return """```mermaid
flowchart LR
    DOC["Texto de Entrada"] --> EMB["Modelo de Embedding"]
    EMB --> VEC["Vector Flotante [0.12, -0.45, ..., 0.88]"]
    VEC --> COS["Cálculo de Similitud Coseno (Distancia Angular)"]
    COS --> RANK["Ranking de Relevancia Semántica"]

    style DOC fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style EMB fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style VEC fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style COS fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
    style RANK fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "rag" in f_name:
            return """```mermaid
flowchart TD
    Q["Pregunta del Usuario"] --> RET["Retriever: Búsqueda Semántica en Vector Store"]
    RET --> CHK["Top-K Chunks Relevantes Recuperados"]
    CHK --> PROMPT["Construcción de Prompt Aumentado (Contexto + Pregunta)"]
    PROMPT --> LLM["LLM genera respuesta citando fuentes oficiales"]

    style Q fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style RET fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style CHK fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style PROMPT fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style LLM fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "react" in f_name:
            return """```mermaid
flowchart TD
    START["Inicio de Tarea"] --> THOUGHT["1. Thought: Razonamiento del siguiente paso"]
    THOUGHT --> ACT{"¿Requiere Acción?"}
    ACT -->|Sí| ACTION["2. Action: Ejecutar Tool (buscar / calcular)"]
    ACTION --> OBS["3. Observation: Resultado obtenido"]
    OBS --> THOUGHT
    ACT -->|No| FINAL["🎯 Final Answer: Entregar respuesta al usuario"]

    style START fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style THOUGHT fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style ACTION fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style OBS fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style FINAL fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        else: # multi-agente
            return """```mermaid
flowchart TD
    USER["Petición Compleja"] --> SUP["Agente Supervisor / Orquestador"]
    SUP -->|Delega Investigación| AG1["Agente Investigador (RAG / Web)"]
    AG1 -->|Retorna Datos| SUP
    SUP -->|Delega Redacción| AG2["Agente Redactor (Formateo Markdown)"]
    AG2 -->|Retorna Borrador| SUP
    SUP -->|Delega Validación| AG3["Agente Auditor (Guardrails & Calidad)"]
    AG3 -->|Aprobado| OUT["Respuesta Final Consolidada"]

    style USER fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style SUP fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
    style AG1 fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style AG2 fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style AG3 fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style OUT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

    else:
        # Curso 4: Proyecto Final
        if "arquitectura" in f_name:
            return """```mermaid
flowchart TD
    CONF["BaseSettings / Variables de Entorno"] --> DTO["Modelos DTO (Contratos de Entrada/Salida)"]
    DTO --> DOM["Entidades de Dominio"]
    DOM --> REPO["Patrón Repositorio (Acceso a Datos)"]
    REPO --> DB[("Persistencia SQLite / PostgreSQL")]

    style CONF fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style DTO fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style DOM fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style REPO fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style DB fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
```"""
        elif "fastapi" in f_name:
            return """```mermaid
flowchart LR
    REQ["HTTP Request (JSON)"] --> ROUTE["FastAPI Router"]
    ROUTE --> DEP["Depends() Inyección de Dependencias"]
    DEP --> VAL["Validación Pydantic"]
    VAL --> SERV["Capa de Servicio"]
    SERV --> RES["HTTP 200 OK + Swagger UI /docs"]

    style REQ fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style ROUTE fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style DEP fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style SERV fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style RES fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "persistencia" in f_name:
            return """```mermaid
flowchart TD
    TX["Inicio: with conn: (Transacción ACID)"] --> DDL["CREATE TABLE / Migración"]
    DDL --> SEC["Consultas Parametrizadas Seguras (?)"]
    SEC -->|Sin errores| CMT["Commit Automático a Disco"]
    SEC -->|Excepción| RBK["Rollback Automático (Consistencia Protegida)"]

    style TX fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style DDL fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style SEC fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style CMT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style RBK fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
```"""
        elif "streamlit" in f_name:
            return """```mermaid
flowchart LR
    UI["Widgets: st.text_input / st.button"] --> STATE["st.session_state (Preservación de Estado)"]
    STATE --> API["requests.post('http://api:8000')"]
    API --> REND["Renderizado: st.dataframe / st.metric / Tabs"]

    style UI fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style STATE fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style API fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style REND fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "integracion" in f_name:
            return """```mermaid
flowchart LR
    INP["st.chat_input"] --> POST["POST /api/chat"]
    POST --> STREAM["Generador Streaming de Tokens (yield)"]
    STREAM --> CHAT_UI["st.chat_message (Efecto Escritura en Tiempo Real)"]

    style INP fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style POST fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style STREAM fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style CHAT_UI fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "testing" in f_name:
            return """```mermaid
flowchart TD
    PYT["Pytest Runner"] --> FIX["Fixtures: Base de Datos en Memoria"]
    FIX --> MCK["unittest.mock: Simulación de APIs Externas"]
    MCK --> TCLI["TestClient: Verificación de Endpoints FastAPI"]
    TCLI --> REP["Reporte de Cobertura y Aserciones"]

    style PYT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style FIX fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style MCK fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style TCLI fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style REP fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
        elif "docker" in f_name:
            return """```mermaid
flowchart LR
    subgraph Compose["🐳 docker-compose.yml"]
        API["Service: FastAPI (Backend :8000)"]
        UI["Service: Streamlit (Frontend :8501)"]
        DB[("Service: PostgreSQL (:5432)")]
        UI --> API
        API --> DB
    end

    style Compose fill:#f8fafc,stroke:#3b82f6,stroke-width:2px
    style API fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style UI fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style DB fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
```"""
        else: # despliegue
            return """```mermaid
flowchart LR
    GIT["git push origin main"] --> GHA["GitHub Actions CI/CD"]
    GHA --> TST["1. Ejecución de Tests Pytest"]
    TST --> BLD["2. Build & Verificación de Contenedores"]
    BLD --> DEPLOY["3. Despliegue Cloud & Portafolio de Graduación"]

    style GIT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style GHA fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
    style TST fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style BLD fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style DEPLOY fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

def get_example_specific_mermaid(ex_folder: str, class_folder: str) -> str:
    """Genera un diagrama Mermaid 100% específico para el script de ese ejemplo concreto."""
    
    if "print" in ex_folder or "hola_mundo" in ex_folder:
        return """```mermaid
flowchart LR
    CODE["print('¡Hola mundo!')"] --> INT["Intérprete de Python"]
    INT --> BUF["Buffer de Salida Estándar (stdout)"]
    BUF --> CON["Consola / Terminal"]

    style CODE fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style INT fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style BUF fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style CON fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

    elif "variables" in ex_folder:
        return """```mermaid
flowchart LR
    NAME["mi_nombre = 'Ana'"] --> OBJ1["Objeto str en Heap ('Ana')"]
    AGE["mi_edad = 28"] --> OBJ2["Objeto int en Heap (28)"]
    REASIGN["mi_edad = 29"] --> OBJ3["Nuevo Objeto int (29)"]

    style NAME fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style OBJ1 fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style AGE fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style OBJ2 fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style REASIGN fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style OBJ3 fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

    elif "if" in ex_folder or "semaforo" in ex_folder or "condicional" in ex_folder:
        return """```mermaid
flowchart TD
    DATA["Estatura = 1.55 m"] --> COND{"¿Estatura >= 1.40 m?"}
    COND -->|True| GREEN["🚦 SEMÁFORO VERDE: Acceso Autorizado 🎢"]
    COND -->|False| RED["🚦 SEMÁFORO ROJO: Acceso Denegado 🛑"]

    style DATA fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style COND fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style GREEN fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style RED fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
```"""

    elif "for" in ex_folder or "cinta" in ex_folder or "bucles" in ex_folder:
        return """```mermaid
flowchart LR
    LST["['Manzanas', 'Leche', 'Pan', 'Café']"] --> FOR["for producto in lista:"]
    FOR --> PKG["Empacar: 'Manzanas'"]
    PKG --> NEXT["Siguiente elemento..."]
    NEXT --> FOR
    NEXT --> DONE["✅ Todos los elementos empacados"]

    style LST fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style FOR fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style PKG fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style DONE fill:#334155,color:#fff,stroke:#94a3b8,stroke-width:2px
```"""

    elif "funcion" in ex_folder or "licuadora" in ex_folder:
        return """```mermaid
flowchart LR
    IN1["'Fresa 🍓'"] --> BLEND["def licuadora(fruta1, fruta2):"]
    IN2["'Plátano 🍌'"] --> BLEND
    BLEND --> PROC["Procesamiento & Concatenación"]
    PROC --> OUT["return 'Batido refrescante de Fresa con Plátano 🥤'"]

    style IN1 fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
    style IN2 fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style BLEND fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style OUT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

    elif "pydantic" in ex_folder or "basemodel" in ex_folder:
        return """```mermaid
flowchart LR
    DICT["{'id': 1, 'name': 'Ana'}"] --> MODEL["User(BaseModel)"]
    MODEL --> VAL["Validación estricta de tipos"]
    VAL --> DUMP["user.model_dump() ➔ Dict sanitizado"]

    style DICT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style MODEL fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style DUMP fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

    elif "fastapi" in ex_folder or "app_minima" in ex_folder:
        return """```mermaid
flowchart LR
    CLIENT["Cliente HTTP (Curl / Browser)"] --> GET["GET /ping"]
    GET --> APP["FastAPI App Router"]
    APP --> JSON["Retorno JSON: {'status': 'ok'}"]

    style CLIENT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style GET fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style JSON fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

    elif "sqlite" in ex_folder or "sql" in ex_folder:
        return """```mermaid
flowchart LR
    CONN["sqlite3.connect(':memory:')"] --> TX["with conn: Transacción Segura"]
    TX --> SQL["conn.execute('INSERT ... (?, ?)', (val1, val2))"]
    SQL --> DSK["Persistencia / Commit en Memoria"]

    style CONN fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style TX fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style SQL fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style DSK fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

    else:
        title_clean = ex_folder.replace("ejemplo_", "").replace("_", " ").title()
        return f"""```mermaid
flowchart LR
    A["📥 1. Entrada de Datos<br/>({title_clean})"] --> B["⚙️ 2. Procesamiento Python<br/>Lógica del Script"]
    B --> C["🎯 3. Salida / Resultado<br/>Consola / Retorno"]

    style A fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""

def update_all_readmes_tailored():
    print("=" * 80)
    print("🚀 REESCRIBIENDO READMEs CON MERMAID ESPECÍFICO Y SIN BOILERPLATE REPETITIVO")
    print("=" * 80)
    
    count = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        rel = os.path.relpath(root, BASE_DIR)
        
        if "README.md" not in files:
            continue
            
        readme_path = os.path.join(root, "README.md")
        parts = rel.split(os.sep)
        
        # 1. README Raíz
        if rel == ".":
            continue
            
        # 2. README de Curso (ej. 01-fundamentos-python/README.md)
        elif len(parts) == 1 and parts[0].startswith(("01-", "02-", "03-", "04-")):
            c_num = int(parts[0][:2])
            c_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
            c_classes = [m for m in ALL_CLASSES if m["course_num"] == c_num]
            
            rows = ""
            for c in c_classes:
                rows += f"| **{c['class_code']}** | [`{c['folder_name']}/`]({c['folder_name']}/) | {c['class_title'].split(':')[-1].strip()} | *«{c['metaphor']}»* |\n"
                
            content = f"""# 📚 {c_cfg['course_name']}

> **{c_cfg['subtitle']}**  
> **Nivel:** {c_cfg['level']} &bull; **Duración:** 8 Semanas Formativas  
> **Instructor:** **{AUTHOR_INFO['name']}** ({AUTHOR_INFO['title']})  

---

## 🗺️ Mapa de Ruta del Curso (8 Semanas)

```mermaid
flowchart TD
    W1["🌱 Semanas 1-2: Fundamentos & Sintaxis<br/>Estructura básica y tipos de datos"] --> W2["⚙️ Semanas 3-5: Flujo & Colecciones<br/>Condicionales, bucles y estructuras lineales"]
    W2 --> W3["🧩 Semanas 6-7: Mapeos & Funciones<br/>Diccionarios, conjuntos y modularización"]
    W3 --> W4["🚀 Semana 8: Síntesis & Proyecto Integrador<br/>Aplicación completa y verificación con tests"]

    style W1 fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style W2 fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style W3 fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style W4 fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 📑 Clases del Curso

| Semana | Directorio | Contenido Temático | Metáfora Didáctica |
| :---: | :--- | :--- | :--- |
{rows}

---

## 📦 Materiales Oficiales del Curso

*   📄 [`{c_cfg['pdf_name']}`]({c_cfg['pdf_name']}): Manual completo oficial en PDF compilado con estética LaTeX.
*   📖 [`book.md`](book.md): Libro de estudio digital con explicaciones profundas y diagramas Mermaid.
*   🧪 Suite de Pruebas Automatizadas en [`tests/curso_{c_num:02d}/`](../tests/curso_{c_num:02d}/).
"""
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            
        # 3. README de Clase (ej. 01-fundamentos-python/clase-01-.../README.md)
        elif len(parts) == 2 and parts[1].startswith("clase-"):
            c_num = int(parts[0][:2])
            f_name = parts[1]
            meta = CLASS_META_MAP.get((c_num, f_name))
            if meta:
                course_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
                mermaid_diag = get_class_specific_mermaid(meta)
                nb_name = meta["pdf_filename"].replace(".pdf", ".ipynb")
                colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{parts[0]}/{f_name}/notebook/{nb_name}"
                
                content = f"""# 📘 {meta['class_title']}

> **Curso:** {course_cfg['course_name']} ({meta['class_code']})  
> **Nivel:** {meta['level']} &bull; **Metáfora:** *«{meta['metaphor']}»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

{mermaid_diag}

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`{meta['pdf_filename']}`]({meta['pdf_filename']}): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
"""
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1
                
        # 4. README de 'ejemplos' de una clase
        elif len(parts) == 3 and parts[2] == "ejemplos":
            c_num = int(parts[0][:2])
            f_name = parts[1]
            meta = CLASS_META_MAP.get((c_num, f_name), {})
            class_title = meta.get("class_title", f_name)
            
            subdirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
            subdirs.sort()
            
            rows = ""
            for sd in subdirs:
                rows += f"| [`{sd}/`]({sd}/) | Demostración comentada | [`main.py`]({sd}/main.py) |\n"
                
            content = f"""# 💻 Ejemplos de Código: {class_title}

> **Ubicación:** `{rel}`  

Esta carpeta contiene los scripts prácticos diseñados para demostrar el funcionamiento en vivo de cada concepto.

---

## 🗺️ Índice de Ejemplos

| Subcarpeta | Descripción | Archivo |
| :--- | :--- | :---: |
{rows}

---

## 🚀 Cómo Ejecutar los Ejemplos
Desde la terminal en la raíz del repositorio:
```bash
python {rel}/<nombre_carpeta>/main.py
```
"""
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            
        # 5. README de un Ejemplo Concreto (ej. ejemplo_01_.../README.md)
        elif len(parts) == 4 and parts[2] == "ejemplos":
            ex_folder = parts[3]
            class_folder = parts[1]
            c_num = int(parts[0][:2])
            meta = CLASS_META_MAP.get((c_num, class_folder), {})
            
            ex_clean_title = ex_folder.replace("ejemplo_", "").replace("_", " ").title()
            ex_mermaid = get_example_specific_mermaid(ex_folder, class_folder)
            
            # Leer main.py para dar una breve descripción
            main_path = os.path.join(root, "main.py")
            first_line_desc = ""
            if os.path.exists(main_path):
                with open(main_path, "r", encoding="utf-8") as f_py:
                    doc = f_py.read()
                    if '"""' in doc:
                        first_line_desc = doc.split('"""')[1].strip().split("\n")[0]
                        
            content = f"""# 📖 {ex_clean_title}

> **Clase:** {meta.get('class_title', class_folder)}  
> **Script:** [`main.py`](main.py)  

{first_line_desc}

---

## 🗺️ Flujo de Ejecución del Ejemplo

{ex_mermaid}

---

## 💻 Ejecución desde Terminal

```bash
python {rel}/main.py
```
"""
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            
        # 6. README de 'ejercicios' de una clase
        elif len(parts) == 3 and parts[2] == "ejercicios":
            c_num = int(parts[0][:2])
            f_name = parts[1]
            meta = CLASS_META_MAP.get((c_num, f_name), {})
            
            content = f"""# 🏋️ Reto Práctico: {meta.get('class_title', f_name)}

> **Curso:** {parts[0]} &bull; **Semana:** {meta.get('class_code', 'Semana')}  
> **Archivo del Reto:** [`reto.py`](reto.py)  

---

## 🎯 Enunciado del Desafío
> **{meta.get('p9_challenge', 'Completa la implementación en reto.py')}**

---

## 🗺️ Flujo de Resolución

```mermaid
flowchart LR
    A["📖 1. Leer reto.py"] --> B["💻 2. Escribir Solución"]
    B --> C["🧪 3. Validar con Pytest<br/>pytest tests/curso_{c_num:02d}/"]
    C -->|Falla ❌| B
    C -->|Pasa ✅| D["🏆 4. Reto Completado"]

    style A fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style D fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 🚀 Cómo Validar tu Código
```bash
pytest tests/curso_{c_num:02d}/
```
"""
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            
        # 7. README de 'notebook' de una clase
        elif len(parts) == 3 and parts[2] == "notebook":
            c_num = int(parts[0][:2])
            f_name = parts[1]
            meta = CLASS_META_MAP.get((c_num, f_name), {})
            nb_name = meta.get("pdf_filename", "clase.pdf").replace(".pdf", ".ipynb")
            colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{parts[0]}/{f_name}/notebook/{nb_name}"
            
            content = f"""# 📓 Cuaderno Interactivo: {meta.get('class_title', f_name)}

> **Curso:** {parts[0]}  
> **Archivo:** [`{nb_name}`]({nb_name})  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})

---

## 🗺️ Formato de Trabajo Interactivo

```mermaid
flowchart LR
    NB["📓 {nb_name}"] --> COLAB["☁️ Google Colab<br/>(1 Clic)"]
    NB --> LOCAL["💻 VS Code Local<br/>(Jupyter Extension)"]
    COLAB --> RUN["⚡ Ejecución Celda a Celda"]
    LOCAL --> RUN

    style NB fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style COLAB fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style LOCAL fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style RUN fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 🚀 Opciones de Uso
*   **En la Nube:** Haz clic en el botón superior **Open in Colab** para ejecutar sin instalar nada.
*   **En Local:** Abre [`{nb_name}`]({nb_name}) directamente en Visual Studio Code.
"""
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1

        # 8. READMEs de /tests
        elif parts[0] == "tests":
            sub_name = parts[1] if len(parts) > 1 else "Root"
            content = f"""# 🧪 Suite de Pruebas: {sub_name.title()}

> **Ubicación:** `{rel}`  

---

## 🗺️ Estructura de Verificación Automatizada

```mermaid
flowchart TD
    CODE["Código del Estudiante (ejercicios/)"] --> PYTEST["Pytest Runner ({sub_name})"]
    PYTEST --> CI["GitHub Actions CI"]
    CI --> PASS["✅ Validación de Calidad (100% Green)"]

    style CODE fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style PYTEST fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style CI fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style PASS fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 💻 Comandos de Ejecución
```bash
pytest {rel}/
```
"""
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            
        # 9. READMEs de /docs
        elif parts[0] == "docs":
            sub_name = parts[1] if len(parts) > 1 else "Root"
            content = f"""# 🌐 Documentación Web: {sub_name.title()}

> **Sitio Web:** [`academy_python.wisrovi.dev`](https://academy_python.wisrovi.dev/)  
> **Ubicación:** `{rel}`  

---

## 🗺️ Flujo de Publicación Web

```mermaid
flowchart LR
    MD["Archivos Markdown ({rel}/*.md)"] --> MKD["Motor MkDocs Material"]
    MKD --> GHP["GitHub Pages (academy_python.wisrovi.dev)"]

    style MD fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style MKD fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style GHP fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 💻 Servidor Local
```bash
mkdocs serve
```
"""
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1

    print(f"\n✨ REESCRITURA COMPLETADA: {count} READMEs actualizados con contenido y Mermaid a medida.")

if __name__ == "__main__":
    update_all_readmes_tailored()
