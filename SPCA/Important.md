# Important to remember
## Calculations
### Nested Array Row

```c
arr[N][M]

arr[i][j] = arr + (i * M + j)
```


### IEEE
*Exp = 000 ... 0* -> -Bias + 1, leading 0.

### Cache 
Each page table entry PTE contains only the PPN and the metadata

**Minimum size of each PTE in bytes**
Physical address space - Pagesize + Flags(Metadata)

**Size of processors page table**
Virtual address space - pagesize + PTE size

**False Sharing** Poor performance when on different processors -> flush whole cache eventough they didn't need the same location. Good performance when on same processor
## Parallel Programming
### Solving ABA problem
- Harard Pointers
   - Threads keep track of questioned pointers in a shared data structure. In this way, each thread knows that the object on the given memory address defined by the pointer might have been modified by another thread
- Immutability
    - The usage of immutable objects solves this problem, as we don't reuse objects across the application
- Double Compare and Swap
    - Keep track of one more variable, which is the version number


## Architecture
*Section header table* Offsets and sizes of each section

*symtab.*   S  ymbol table, procedure and static variable names, section names and locations

*.rel.text* relocation info for .text section instructions for modifying

#.debug* Info for symbolic debugging (gcc. -g)

It exists 1 virtual address space per process

![image info](./flag_table/image.png)

**Synonym** 
- Only in virtual part 
- different VAs map to same PA
- VV with keys remove homonyms but creates synonyms

**Homonym**
- Same name for different data
- same VA refers to different PAs
- flush cache on context swithc
- force non-overlapping address-space
- tag VA with address-space
### Jumps
*Longjmp* If retval = 0, longjmp returns 1

*Setjumpt* saves current calling environment
- program counter (not nececcessary)
- stack pointer
- general purpose register

Or as it was mentioned in the exam:
- current stack pointer
- The current program counter (%rip)
- Calle-save processor registers
- Frame pointer register §rbp

### MESI
- Dirty data always written through memory
- No cache cache transfer
- Good if latency of memory << latency of remote cache

### Program order
Order in which a program on a processor appears to issue reads and writes. Refers only to **local** reads/writes

### Visibility Order
Order which all reads and writes are seen by one or more processors. Refers to all operations in the machine
### Sequential Consistency
Think of PPROG -> Order important but you can move instructions horizontally
1) Operations from a processor appear (to all others) in program order
2) Every processor's visibility order is the interleaving of all the program orders

*Requieremts:* 
- Each processor issues memory ops in program order
- Memory operations are atomic


## Dependence
**Anti-dependence** write after read, can avoid hazard with register renaming

**Output-dependence** write after write, can avoid hazard with register renaming

**True-dependence** read after write

### Order on stack
Extra args

Return address

saved base pointer

local variables
## Exceptions
**Asynchronous exception** caused by events outside of processor --> ctr-c (interrupt)

**Synchronous exception** caused by an instruction of the processor
### Abort
- Nonrecoverable error
- Sync
- unintentional
- machine check
- **Aborts current program**
### Fault
- potentially recoverable errer
- sync
- unintentional
- page fault, protection fault
- **Either re-executes faulting instruction or abort**
### Trap
- intentional 
- sync
- system calls, breakpoint trap
- **returns control to "next" instruciton**

## Linker
- Resolving symbol references from other files
- Merging different object files sections


## Toolchain
*How C code turns into an executable file*
C source - Preprocessor - Compiler - Assembler - Linker - Executable

*GNU gcc Toolchain*

CPP (Macro subsitution include header files) - CC1 (compile each C file into assembly language) - as (Assemble each file into object code) - Id (link object files into program binary) - Executable

## Debugger
**Valgrind** helpful for memory-related errors

**GDB** conventional debugger, good for finding bad pointer dereferences, hard to detect the other memory bugs

**Objdump** Useful tool for examinibg object code, analyzes bit pattern of series of instructions

## Random
\\\ is an escape. 




*PIC, Programmable Interrupt Controller*
- Map physical interrupt pins to interrupt vectors
- Buffer simultanous interrupts -> Won't lose some devices interrupt
- Prioritize interrupts
- Selectievly mask any individual device's interrupts useful for high interrupt rate

How many BxB blocks fint into a cache and how many blocks do you need? -> $X B^2 < C$ where X is mostly 3 and C the Cache size


Reading string of length 10 in buffer
````c
fgets(buf, 10, stdin);
fscanf(stdin, "%9s", buf);
````

````c
NULL = (void *) 0
````

DRAM as cache: Fully associative, sophisticated replacement policy, writeback

