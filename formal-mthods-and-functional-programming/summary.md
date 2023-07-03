# Important Things to Remember
## Haskell
### Input/Output

````Java
void f(String out) {
String inp1 = Console.readLine();
String inp2 = Console.readLine();
if (inp2.equals(inp1)) System.out.println(out); }
```` 

How to convert to Haskell?
````Haskell
f :: String -> IO ()
f out = do
    inp1 <- getLine
    inp2 <- getLine
    if inp2 == inp1
        then putStrLn out
        else return ()
````
Syntax for IO type:
- do block sequences side effects
- <- extracts values from IO
- return wraps values in IO

- show converts values to Strings
- read converts Strings to values (Always specify the desired type!)
- for $\alpha$-equivalence, no variables can be free!

Syntax Tree
- $\land$ binds stronger than $\lor$ stronger than $\rightarrow$.
- I $\rightarrow$ associates to the right; $\land$ and $\lor$ to the left.
- I Negation binds stronger than binary operators.
- I Quantifiers extend to the right as far as possible.

Proof Rule fore Induction Step:
![alt text](induction-step-tree.png "Induction Step Tree")
## Foldr/Foldl

Foldr:
The easiest way to understand foldr is to rewrite the list you're folding over without the sugar.
````Haskell
[1,2,3,4,5] => 1:(2:(3:(4:(5:[]))))
````
now what `foldr f x` does is that it replaces each `:` with `f` in infix form and `[]` with `x` and evaluates the result.

For example:
````Haskell
sum [1,2,3] = foldr (+) 0 [1,2,3]

[1,2,3] === 1:(2:(3:[]))
````
so
````Haskell
sum [1,2,3] === 1+(2+(3+0)) = 6
````

## CYP
```CYP
Proof by induction on List xs generalizing zs
Case []
    For fixed zs
    Show: rev [] ++ zs .=. qrev [] zs
    . . .
Case y:ys
    Fix y, ys
    Assume
        IH: forall zs: rev ys ++ zs .=. qrev ys zs
    Then for fixed zs
    Show: rev (y:ys) ++ zs .=. qrev (y:ys) zs
    . . .
QED
```

## $\eta$-conversion
- The following tow terms are equivalent under $\eta$-conversion:
$$\\x \rightarrow f x  \text{ and } f$$
- Converting from left to right isn $\eta$-contraction
- Converting from right to left is $\eta$-expansion
- $\eta$-conversion is sometimes useful to simplify expressions

Example:

Function parity takes a list of Integers and transforms it into a list of
0/1s.

`parity xs = map elemPar xs where elemPar x = mod x 2`

`parity' = map ('mod' 2)`

### General procedure of foldr, foldl
1. Identify recursive, dynamic, and static arguments.
````Haskell
foldl f z (x:xs) = foldl f (f z x) xs
````
2. Write an aux function that has the recursive, then the dynamic arguments. Static
arguments can still occur freely (and will come from the final context).
````Haskell
aux [] z = z
aux (x:xs) z = aux xs (f z x)
````
3. Write the dynamic arguments as lambdas.
````Haskell
aux [] = \z -> z
aux (x:xs) = \z -> aux xs (f z x)
````
4. Rewrite aux in terms of foldr. x and aux xs become arguments of the function for the
recursive case.
````Haskell
aux = foldr (\x rec -> \z -> rec (f z x)) (\z -> z)
````
5. Express the original function in terms of aux (reorder the dynamic and recursive
arguments, if needed).
````Haskell
foldl f z xs = aux xs z
````
6. Replace aux with its implementation.
````Haskell
foldl f z xs = foldr (\x rec z -> rec (f z x)) (\z -> z) xs z
````