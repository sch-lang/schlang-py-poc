# Schlang

A simplified implementation of the Schlang Programming Language compiler using Python.
This will in turn be superseded by the Rust implementation of the compiler once all the basic
functionality is mapped out.

## What will the program do?

### Frontend
The frontend of the compiler is the base of our compiler which
can be used to parse our source program and generate intermediate
machine code to be use by the frontend. Frontend's will be system-specific
and tailored to the target individual system architectures.

#### Step 1 - Lexical analysis
Parse the input data into tokens (lexemes) and store them
in a symbol table along with information about location
and value.

#### Step 2 - Syntax analysis
In this step we'll check that the input data conforms to the
Schlang grammar. To do this we'll create syntax trees based on the
grammar, and collect any syntax errors we encounter along the way.

#### Step 3 - Semantic analysis
This step will check the the source program conforms to the Schlang
definition and that the program is semantically sound. It will also
collect all types and store them in the symbol table along with
the symbol.

#### Step 4 - Intermediate code generation
*TBD*

### Frontend
The frontend will generate assembly code based on the intermediate code 
for the individual machine architectures based on compiler flags.

#### Step 5a - Code optimization
*TBD*

#### Step 5b - Code generation
*TBD*