# Important stuff for the exam

## Normal Forms

### First Normal Form
1. Using row order to convey information is not permitted
2. Mixing data types within the same column is not permitted
3. Having a table without a rimary key is not permitted
4. Repeating groups is not permitted

### Second Normal Form
- Each non-key attribute in the table must be dependent on the entire primary key.
- If you have a strict subset of the key, it is not in 2NF.
- If everything on the right side is a key then it is in 2NF

### Third Normal Form
- Each non-key attribute in the table must depend on the key, the whole key, and nothing but the key.
- If everything on the right side is a key then it is in 3NF
- No transitive relations

### Boyce-Codd Normal Form
- Each attributee in the table must depend on the key, the whole key, and nothing but the key.
- If everything ont the right is a full key it is fine (but check again)

### Foruth Normal Form
The only kinds of multivalued dependency allowed in a table are mulivalued dependencies on the key.

### Fifth Normal Form
It must not be possible to describe the table as being the logical result of joining some other tables together.

## Candidate Key
- You have a candidate key, if all its attributes appear only on the left side of the dependencies.
- To get the candidate key, look at the closure. If you can reach all the important values, it is a super key for sure. If it is the only one than it is even a candidate key.