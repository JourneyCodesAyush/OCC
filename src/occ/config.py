EXTENSIONS: dict[str, str] = {
    ".cpp": "CPP",
    ".cxx": "CPP",
    ".hpp": "CPP",
    ".java": "JAVA",
    ".py": "PYTHON",
    ".img": "IMG",
    ".jpg": "IMG",
    ".jpeg": "IMG",
    ".png": "IMG",
    ".pdf": "PDF",
}

WARNINGS: list[str] = [
    "[WARN] Variable type unknown... Inferred from gut feeling",
    "[WARN] Errors found in source code... Classifying as creative decisions",
    "[WARN] Null pointer detected... Pointer has been emotionally supported",
    "[WARN] Infinite loop found... Rebranded as persistent computation",
    "[WARN] Memory leak detected... Reclassified as long-term memory",
    "[WARN] Undefined behavior encountered... Behavior has been defined (you're welcome)",
    "[WARN] Off-by-one error found... Shifted reality by 1 to compensate",
    "[WARN] Schrödinger's type detected... Resolved as correct",
    "[WARN] Logical contradiction on line 42... Resolved optimistically",
    "[WARN] Segmentation fault imminent... Segment has been reassured",
]

SUCCESSES: list[str] = [
    "Compilation successful.",
    "Build complete. No further questions.",
    "All errors resolved optimistically.",
    "Problems were encountered, understood, and ignored professionally.",
    "Executable materialized successfully (conceptually).",
    "Your code is now machine code. Trust the process.",
    "Compilation successful. The compiler believes in you.",
    "0 errors, 0 warnings. (Warnings were promoted to features.)",
]

FILES: dict[str, list[str]] = {
    "CPP": [
        "[Lexing]      Tokenizing source code... Whispering to the preprocessor...",
        "[Parsing]     Parsing tokens into Abstract Syntax Tree... It's beautiful.",
        "[Compiling]   Converting AST to machine code... Teaching silicon to dream...",
        "[Linking]     Linking libraries... Negotiating with libstdc++...",
        "[Executable]  Writing binary to disk... (conceptually)...",
    ],
    "PYTHON": [
        "[Lexing]      Tokenizing source code... Counting indentation religiously...",
        "[Parsing]     Creating Abstract Syntax Tree... Respecting the whitespace...",
        "[Bytecode]    Compiling AST to bytecode... Preparing .pyc for eternity...",
        "[VM]          Packaging bytecode for virtual machine... Starting the GIL prayer...",
    ],
    "JAVA": [
        "[Lexing]      Tokenizing source code... Importing everything just in case...",
        "[Parsing]     Creating Abstract Syntax Tree... AbstractSyntaxTreeBuilderFactory initialized...",
        "[Bytecode]    Compiling to JVM bytecode via javac... Write once, debug everywhere...",
        "[ClassLoader] Loading .class files into JVM... Warming up the enterprise...",
        "[JIT]         Just-In-Time compiling hot paths... Getting just-in-time nervous...",
        "[Executable]  Packaging into runnable JAR... It'll run. Somewhere. Eventually.",
    ],
    "IMG": [
        "[Lexing]      Analyzing pixels... Each one judged individually...",
        "[Parsing]     Decomposing pixels into RGB values... The blue ones seem sad...",
        "[Analyzing]   Feeding RGB matrix into zero-latency transformer... It sees art...",
        "[Compiling]   Compiling visual semantics into machine code... Beauty, optimized...",
        "[Executable]  Executable created... It looks great by the way.",
    ],
    "PDF": [
        "[Lexing]      Tokenizing Portable Document Format... Unflattening the flattened...",
        "[Parsing]     Converting token stream to AST... Liberating embedded fonts...",
        "[Analyzing]   Extracting page tree and metadata... 47 layers deep...",
        "[Compiling]   Compiling document semantics to machine code... Pages → silicon...",
        "[Executable]  Executable created... The PDF has ascended.",
    ],
    "VOID": [
        "[Lexing]      Nothing provided... Acknowledging the void...",
        "[Parsing]     Transforming void into VOID... Capitalizing the emptiness...",
        "[Compiling]   Compiling the absence of everything... This is fine...",
        "[Executable]  Materializing nothing into something... One must imagine the executable happy.",
    ],
    "UNKNOWN": [
        "[Lexing]      Tokenizing... whatever this is...",
        "[Parsing]     Attempting to parse the unparseable... Giving it our best...",
        "[Analyzing]   Running heuristics... File defies known classification...",
        "[Compiling]   Compiling based on vibes alone...",
        "[Executable]  Executable created... We're as surprised as you are.",
    ],
}
