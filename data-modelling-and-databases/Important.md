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

## Database Systems
### Disk Manager
- allocates, deletes, fetches pages
- no other layer has to interact with disk directly

### Buffer Pool Manager
- Maintains an in-memory buffer
- upper layers have illusion that the entire data is in memory and not on disk
- provides functionality to fetch and update pages

### Access Methods
- Sequential Scan
- B-Tree Index
- Hash Table
- Sort
It provides a higher-level abstraction to acess information in a table without interacting with the buffer or disk

### Operator Execution
Executes a relational algebra
- Join 
- Projection
- Select

### Query Optimization
- Generates a good execution plan

## Important things to know

**Heap File** = an unordered colletion of pages where tuples are stored in random order

**Record ID** = (Page ID, Slot ID)

**Pages**
 = A page is a fixed-size block of data:
    Contain tuples, meta-data, indexes, log records etc.

## Different Joins
### Sort Merge Join (equi-join)


### Nested Loop Join
- Efficient: Smaller relation fits into memory
- Inefficient: Both relations do not fit into memory

### Block Nested Loop Join (equi-join)

### Index Nested Loop Join (equi-join)
- Effieicent: Low selectivity (few reads per disk)
- Inefficient: High selectivity (loads of reads per disk)

### Hash join (equi-join)
- Efficient: 
- Inefficient: 



## Quiz Questions and Answers
**While adding tuples ot a page, both the slot array and the data of the tuples will grow from the beginning to the end:**
- The slot array will grow from the beginning to the end, whereas the data of the tuples will grow from the end to the beginning. When they meet, the page becomes full. 
- **Lecture 16, Slide 41**

**Sequential scan or B-Tree**
- When nearly *all* the tuples fullfill the requirement, *scan* is fast, B - Tree is slow
- When only a *few* or only one fullfills the requirement, *B - Tree* is fast, scan is slow

- $$T_{scan} = T_{acces} + \frac{(pageSize *  m)}{Bandwidth}$$

- $$T_{index}(k) = (T_{access} \frac{page size} {/} ...)$$


# Recoverability
### RC
- If $T_1$ reads from
- You do not need to undo the commit
### ACA
- Aborting a transaction does not cause aborting others
### ST
- If we need to undo one transaction, we don't need to redo or undo the others

### Serializable
- Defined by the equivalence of result

### Conflict Serializable
- Defined by swap adjacent, non-conflicting, operations
- Conflict Serializable is a **subset** of Serializable
    
## How to decide Conflict-Serializability?
- Go from definition -- do the swap
- Dependency Graph 
    - You can ignore the aborts 
    - No reads, then it is automatically recoverable and ACA -> just need to check strict

## Difference On, Where

The information is from [here](https://stackoverflow.com/questions/354070/sql-join-where-clause-vs-on-clause).

- Does not matter for inner joins
- Matters for outer joins

a. WHERE clause: After joining. Records will be filtered after join has taken place.

b. ON clause - Before joining. Records (from right table) will be filtered before joining. This may end up as null in the result (since OUTER join).

## Keys
### Super key
- like superset
- uniquely identify the tuple
- ID, Name; ID, Phone; Name, Phone etc.
- May contain extraneous, attributes

### Candidate key
- Minimal super keys are called candidate keys

### Primary key
- Unique
- should not have null values (email, phone number is not that good)

### Alternate key
   
