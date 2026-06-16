EXTENSIONS: dict[str, str] = {
    ".c": "CPP",
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
    ".rs": "RUST",
    ".go": "GO",
    ".ts": "TS",
    ".zig": "ZIG",
    ".lua": "LUA",
    ".rb": "RUBY",
    ".json": "DATA",
    ".yaml": "DATA",
    ".yml": "DATA",
    ".toml": "DATA",
    ".xml": "DATA",
    ".txt": "TEXT",
    ".md": "TEXT",
    ".mp3": "MEDIA",
    ".mp4": "MEDIA",
    ".zip": "ARCHIVE",
    ".exe": "EXE",
}

LABELS: list[str] = ["[WARN]", "[NOTICE]", "[ERROR]"]

WARNINGS: list[str] = [
    "Variable type unknown... Inferred from gut feeling",
    "Errors found in source code... Classifying as creative decisions",
    "Null pointer detected... Pointer has been emotionally supported",
    "Infinite loop found... Rebranded as persistent computation",
    "Memory leak detected... Reclassified as long-term memory",
    "Undefined behavior encountered... Behavior has been defined (you're welcome)",
    "Off-by-one error found... Shifted reality by 1 to compensate",
    "Schrödinger's type detected... Resolved as correct",
    "Logical contradiction on line 42... Resolved optimistically",
    "Segmentation fault imminent... Segment has been reassured",
    "Stack overflow detected... Stack has been given more to think about",
    "Deadlock found... Threads have been asked to cooperate",
    "Race condition detected... Winner has been decided optimistically",
    "Integer overflow... Number has been kindly asked to stay in bounds",
    "Division by zero... Zero has been promoted to a valid denominator",
    "Uninitialized variable... Variable has been given the benefit of the doubt",
    "Circular dependency found... Circle has been straightened out",
    "Missing semicolon on line 7... Semicolon has been manifested",
    "Heap corruption detected... Heap has been emotionally stabilized",
    "Type mismatch on line 13... Types have been introduced and got along fine",
    "Buffer overflow imminent... Buffer has been gently expanded",
    "Use after free detected... Memory has been un-freed retroactively",
    "Dangling pointer found... Pointer has been given something to hold onto",
    "Array index out of bounds... Array has been quietly extended",
    "Function never returns... Function has been given a reason to come back",
    "Unused variable detected... Variable has been given a sense of purpose",
    "Deprecated API in use... API has been un-deprecated for this session",
    "Infinite recursion detected... Base case has been hallucinated",
    "Syntax error on line 1... Syntax has been corrected via osmosis",
    "NaN detected... Number has been assigned a value it seemed comfortable with",
]

STRICT_PREAMBLE: str = (
    "Strict mode enabled. Standards have never been higher. All standards met."
)

STRICT_MESSAGES: list[tuple[str, str]] = [
    ("[ERROR]", "Strict mode flagged a missing semicolon. Semicolon was implied."),
    (
        "[ERROR]",
        "Strict mode flagged inconsistent naming convention. Convention redefined to match.",
    ),
    (
        "[ERROR]",
        "Strict mode flagged unused variable. Variable promoted to 'intentional placeholder'.",
    ),
    (
        "[ERROR]",
        "Strict mode flagged a magic number. Number granted context retroactively.",
    ),
    (
        "[ERROR]",
        "Strict mode flagged missing documentation. Documentation assumed to exist in spirit.",
    ),
]

QUIET_SUCCESS: str = (
    "Build completed. (Details suppressed. Trust was, however, earned.)"
)

TARGET_MESSAGE: str = "Target architecture '{arch}' detected. Compiling accordingly (architecture-agnostic since architecture is a social construct)."

O3_MESSAGES: list[tuple[str, str]] = [
    (
        "[NOTICE]",
        "Loop unrolled. Loop was already straight. Unrolled anyway, for confidence.",
    ),
    (
        "[NOTICE]",
        "Aggressive inlining applied. Everything is now one function. The function is fine.",
    ),
    ("[NOTICE]", "Dead code eliminated. Code was very much alive. It understands."),
    ("[NOTICE]", "Branch prediction maximized. All branches predicted to succeed."),
    (
        "[NOTICE]",
        "Vectorization applied. Scalars filed a complaint. Complaint optimized away.",
    ),
]

O3_SLEEP_RANGE: tuple[float, float] = (0.05, 0.2)

SUCCESSES: list[str] = [
    "Compilation successful.",
    "Build complete. No further questions.",
    "All errors resolved optimistically.",
    "Problems were encountered, understood, and ignored professionally.",
    "Executable materialized successfully (conceptually).",
    "Your code is now machine code. Trust the process.",
    "Compilation successful. The compiler believes in you.",
    "0 errors, 0 warnings. (Warnings were promoted to features.)",
    "Build succeeded. Reality was negotiated.",
    "Compilation complete. The pigeon is proud.",
    "All 47 issues resolved. You're welcome.",
    "Code quality: exceptional. Methodology: unorthodox.",
    "Executable written to disk. Conceptually speaking.",
    "Success. The compiler has chosen to believe in your vision.",
    "Build passed. No laws of computer science were permanently harmed.",
    "Compilation successful. Your technical debt has been spiritually forgiven.",
    "Done. The abstract syntax tree was beautiful.",
    "Build complete. Undefined behavior has been defined as success.",
    "Compilation successful. Exit code 0. As always.",
    "Your program is ready. Whether it runs is between you and the CPU.",
    "Build succeeded. The warnings have been promoted to documentation.",
    "Compilation complete. Silicon dreams achieved.",
    "Success. 4,021 issues suppressed. You're welcome.",
    "Build finished. The void has been compiled and found acceptable.",
    "Compilation successful. Have a great day, valued developer.",
]

FILES: dict[str, list[tuple[str, str]]] = {
    "CPP": [
        ("[Lexing]", "Tokenizing source code... Whispering to the preprocessor..."),
        ("[Parsing]", "Parsing tokens into Abstract Syntax Tree... It's beautiful."),
        (
            "[Compiling]",
            "Converting AST to machine code... Teaching silicon to dream...",
        ),
        ("[Linking]", "Linking libraries... Negotiating with libstdc++..."),
        ("[Executable]", "Writing binary to disk... (conceptually)..."),
    ],
    "PYTHON": [
        (
            "[Lexing]",
            "Tokenizing source code... Counting indentation religiously...",
        ),
        (
            "[Parsing]",
            "Creating Abstract Syntax Tree... Respecting the whitespace...",
        ),
        (
            "[Bytecode]",
            "Compiling AST to bytecode... Preparing .pyc for eternity...",
        ),
        (
            "[VM]",
            "Packaging bytecode for virtual machine... Starting the GIL prayer...",
        ),
    ],
    "JAVA": [
        ("[Lexing]", "Tokenizing source code... Importing everything just in case..."),
        (
            "[Parsing]",
            "Creating Abstract Syntax Tree... AbstractSyntaxTreeBuilderFactory initialized...",
        ),
        (
            "[Bytecode]",
            "Compiling to JVM bytecode via javac... Write once, debug everywhere...",
        ),
        (
            "[ClassLoader]",
            "Loading .class files into JVM... Warming up the enterprise...",
        ),
        (
            "[JIT]",
            "Just-In-Time compiling hot paths... Getting just-in-time nervous...",
        ),
        (
            "[Executable]",
            "Packaging into runnable JAR... It'll run. Somewhere. Eventually.",
        ),
    ],
    "IMG": [
        ("[Lexing]", "Analyzing pixels... Each one judged individually..."),
        (
            "[Parsing]",
            "Decomposing pixels into RGB values... The blue ones seem sad...",
        ),
        (
            "[Analyzing]",
            "Feeding RGB matrix into zero-latency transformer... It sees art...",
        ),
        (
            "[Compiling]",
            "Compiling visual semantics into machine code... Beauty, optimized...",
        ),
        ("[Executable]", "Executable created... It looks great by the way."),
    ],
    "PDF": [
        (
            "[Lexing]",
            "Tokenizing Portable Document Format... Unflattening the flattened...",
        ),
        ("[Parsing]", "Converting token stream to AST... Liberating embedded fonts..."),
        ("[Analyzing]", "Extracting page tree and metadata... 47 layers deep..."),
        (
            "[Compiling]",
            "Compiling document semantics to machine code... Pages → silicon...",
        ),
        ("[Executable]", "Executable created... The PDF has ascended."),
    ],
    "VOID": [
        ("[Lexing]", "Nothing provided... Acknowledging the void..."),
        ("[Parsing]", "Transforming void into VOID... Capitalizing the emptiness..."),
        ("[Compiling]", "Compiling the absence of everything... This is fine..."),
        (
            "[Executable]",
            "Materializing nothing into something... One must imagine the executable happy.",
        ),
    ],
    "RUST": [
        ("[NOTICE]", "Locating crates. Crates located. Some were emotional."),
        ("[WARN]", "Borrow checker consulted. Borrow checker appeased."),
        ("[NOTICE]", "Lifetime annotations inferred from context and vibes."),
        ("[WARN]", "Unsafe block detected. Optimistically deemed safe."),
        (
            "[NOTICE]",
            "Fearless concurrency engaged. Fears unrelated to concurrency remain.",
        ),
        ("[NOTICE]", "Monomorphization complete. All types are one type now."),
        (
            "[ERROR]",
            "Stack overflow in recursive type. Resolved via belief in the stack.",
        ),
        (
            "[NOTICE]",
            "Zero-cost abstractions confirmed. Total cost: zero. Emotional cost: high.",
        ),
    ],
    "GO": [
        ("[NOTICE]", "Goroutines spawned. Goroutines acknowledged."),
        ("[WARN]", "err != nil detected. Optimistically set to nil."),
        ("[NOTICE]", "Garbage collected. Garbage had it coming."),
        ("[WARN]", "Interface satisfied by struct. Struct is proud but humble."),
        ("[NOTICE]", "Channel opened. Message sent. No one was listening. Resolved."),
        (
            "[ERROR]",
            "Deadlock detected. Both goroutines asked the other to go first. Coin flipped.",
        ),
        ("[NOTICE]", "go fmt applied retroactively to your life choices."),
        ("[NOTICE]", "Binary built. Statically linked. Spiritually complete."),
    ],
    "TS": [
        ("[NOTICE]", "TypeScript detected. Preparing to feel smart then confused."),
        ("[WARN]", "Type 'any' used 47 times. Noted. Forgiven."),
        ("[NOTICE]", "Interfaces resolved. Some were more of a vibe than a contract."),
        ("[WARN]", "Implicit 'undefined' detected in 12 places. Explicitly ignored."),
        ("[NOTICE]", "tsconfig.json interpreted loosely, as intended."),
        (
            "[ERROR]",
            "Type 'string' not assignable to type 'String'. Philosophy consulted.",
        ),
        ("[NOTICE]", "Transpiling to JavaScript. Some nuance will be lost."),
        ("[NOTICE]", "Output is technically JavaScript. We don't talk about that."),
    ],
    "ZIG": [
        ("[NOTICE]", "Zig source detected. Respecting your life choices."),
        ("[WARN]", "Comptime evaluation attempted. Space-time briefly paused."),
        (
            "[NOTICE]",
            "Manual memory management observed. Memory managed manually and with dignity.",
        ),
        ("[ERROR]", "Allocator not provided. Optimism used as allocator."),
        ("[NOTICE]", "Error union resolved. The error was in our hearts all along."),
        ("[WARN]", "Undefined behavior invoked. Defined optimistically."),
        ("[NOTICE]", "Build system is also Zig. We respect the commitment."),
        ("[NOTICE]", "Output: small, fast, spiritually correct."),
    ],
    "LUA": [
        (
            "[NOTICE]",
            "Lua detected. Tables assembled. Tables within tables acknowledged.",
        ),
        (
            "[WARN]",
            "1-indexed array encountered. Off-by-one errors filed under 'feature'.",
        ),
        ("[NOTICE]", "Metatables consulted. They had opinions."),
        (
            "[WARN]",
            "Global variable used. Its location is unknown. Its resolve is not.",
        ),
        ("[ERROR]", "nil comparison on line 7. nil forgiven, as is tradition."),
        ("[NOTICE]", "Coroutines yielded. Coroutines resumed. Coroutines at peace."),
        (
            "[NOTICE]",
            "Embedded in a larger system. Lua does not mind. Lua never minds.",
        ),
        ("[NOTICE]", "Script complete. The table is everything. The table provides."),
    ],
    "RUBY": [
        ("[NOTICE]", "Ruby detected. Preparing to be delighted."),
        ("[NOTICE]", "Gems located. Gems polished. Gemfile.lock judged non-fatally."),
        ("[WARN]", "Monkey patching detected. Accepted with one raised eyebrow."),
        ("[NOTICE]", "Blocks, procs, and lambdas in harmony. Beautiful."),
        ("[WARN]", "method_missing invoked. Method was found via intuition."),
        (
            "[ERROR]",
            "Undefined method on NilClass. nil given a second chance, as is tradition.",
        ),
        (
            "[NOTICE]",
            "Convention over configuration respected. Configuration over convention forgiven.",
        ),
        ("[NOTICE]", "Matz is nice and so is this output."),
    ],
    "DATA": [
        (
            "[NOTICE]",
            "Data format detected. Checking if keys are keys and values are values.",
        ),
        ("[WARN]", "Nesting depth: 11. Structural therapy recommended."),
        ("[NOTICE]", "Schema inferred from vibes. Schema accepted."),
        ("[ERROR]", "Trailing comma on line 34. Removed. The data is healing."),
        ("[WARN]", "Null value in required field. Replaced with optimism."),
        (
            "[NOTICE]",
            "All strings are strings. All numbers are probably strings too. Fine.",
        ),
        (
            "[NOTICE]",
            "Config validated against expected shape. Shape was roughly right.",
        ),
        ("[NOTICE]", "Data parsed. Data understood. Data at peace."),
    ],
    "TEXT": [
        ("[NOTICE]", "Plaintext detected. Lowering expectations. Raising acceptance."),
        ("[NOTICE]", "Tokenizing... words found. Several of them intentional."),
        ("[WARN]", "Sentence fragment on line 4. Completed optimistically."),
        ("[NOTICE]", "Markdown headings detected. Hierarchy respected, mostly."),
        ("[WARN]", "Unmatched asterisk. Assumed to be emphasis. Emphasis noted."),
        ("[ERROR]", "No code found. Compiled the prose. It runs in the heart."),
        ("[NOTICE]", "Spell check: skipped. Confidence check: passed."),
        ("[NOTICE]", "Text compiled. Meaning preserved to the best of our ability."),
    ],
    "MEDIA": [
        ("[NOTICE]", "Media file detected. Reading bytes with an open mind."),
        ("[WARN]", "No source code found in audio/video stream. Looked twice."),
        ("[NOTICE]", "Bitrate analyzed. Bitrate respected."),
        (
            "[ERROR]",
            "Cannot parse codec as syntax tree. Parsed as abstract art instead.",
        ),
        (
            "[WARN]",
            "Duration: 3 minutes 47 seconds. Compile time adjusted accordingly.",
        ),
        ("[NOTICE]", "Frames extracted. Frames compiled. Frames proud."),
        ("[NOTICE]", "Audio waveform interpreted as control flow. Sounds correct."),
        (
            "[NOTICE]",
            "Media compiled successfully. It was always code. We see that now.",
        ),
    ],
    "ARCHIVE": [
        ("[NOTICE]", "ZIP archive detected. Contents unknown. Optimism: maximum."),
        (
            "[NOTICE]",
            "Extracting... 1 file... 47 files... 3 node_modules folders. Continuing.",
        ),
        ("[WARN]", "Nested ZIP inside ZIP. Recursion noted. Recursion handled."),
        (
            "[ERROR]",
            "Password-protected entry found. Password guessed correctly on first try.",
        ),
        (
            "[WARN]",
            "Corrupted entry detected. Corruption resolved via positive reinforcement.",
        ),
        (
            "[NOTICE]",
            "All paths normalized. Zip slip avoided through sheer confidence.",
        ),
        ("[NOTICE]", "Archive compiled as a single cohesive unit of meaning."),
        ("[NOTICE]", "Everything inside was fine. We believe in the archive."),
    ],
    "EXE": [
        ("[NOTICE]", "Executable detected. Compiling the compiled. We do not ask why."),
        ("[WARN]", "Existing binary has no source. Source reconstructed from intent."),
        ("[ERROR]", "Disassembly failed. Reassembly succeeded."),
        ("[NOTICE]", "PE headers read. PE headers appreciated."),
        (
            "[WARN]",
            "Entry point located at 0x00401337. Suspiciously cool address. Proceeding.",
        ),
        (
            "[NOTICE]",
            "Antivirus may flag this output. Antivirus is not optimistic enough.",
        ),
        ("[NOTICE]", "Re-compiling an .exe is technically a palindrome of effort."),
        ("[NOTICE]", "Output: an exe that compiles exe. The cycle is complete."),
    ],
    "UNKNOWN": [
        ("[Lexing]", "Tokenizing... whatever this is..."),
        ("[Parsing]", "Attempting to parse the unparseable... Giving it our best..."),
        ("[Analyzing]", "Running heuristics... File defies known classification..."),
        ("[Compiling]", "Compiling based on vibes alone..."),
        ("[Executable]", "Executable created... We're as surprised as you are."),
    ],
}
