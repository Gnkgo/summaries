# Important stuff for the exam

## Normal Forms

### First Normal Form
1. Using row order to convey information is not permitted
2. Mixing data types within the same column is not permitted
3. Having a table without a primary key is not permitted
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
- Each attribute in the table must depend on the key, the whole key, and nothing but the key.
- If everything ont the right is a full key it is fine (but check again)

### Fourth Normal Form
The only kinds of multivalued dependency allowed in a table are multivalued dependencies on the key.

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
It provides a higher-level abstraction to access information in a table without interacting with the buffer or disk

### Operator Execution
Executes a relational algebra
- Join 
- Projection
- Select

### Query Optimization
- Generates a good execution plan

## Important things to know

**Heap File** = an unordered collection of pages where tuples are stored in random order

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
- Efficient: Low selectivity (few reads per disk)
- Inefficient: High selectivity (loads of reads per disk)

### Hash join (equi-join)
- Efficient: 
- Inefficient: 



## Quiz Questions and Answers
**While adding tuples ot a page, both the slot array and the data of the tuples will grow from the beginning to the end:**
- The slot array will grow from the beginning to the end, whereas the data of the tuples will grow from the end to the beginning. When they meet, the page becomes full. 
- **Lecture 16, Slide 41**

**Sequential scan or B-Tree**
- When nearly *all* the tuples fulfil the requirement, *scan* is fast, B - Tree is slow
- When only a *few* or only one fulfils the requirement, *B - Tree* is fast, scan is slow

- $$T_{scan} = T_{access} + \frac{(pageSize *  m)}{Bandwidth}$$

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


# SQL
## Difference On, Where

The information is from [here](https://stackoverflow.com/questions/354070/sql-join-where-clause-vs-on-clause).

- Does not matter for inner joins
- Matters for outer joins

a. WHERE clause: After joining. Records will be filtered after join has taken place.

b. ON clause - Before joining. Records (from right table) will be filtered before joining. This may end up as null in the result (since OUTER join).

## SQL `WITH`
- Referencing a temporary table multiple times in a single query
- Performing multi-level aggregations, such as finding the average of maximums
- Performing an identical calculation multiple times over within the context of a larger query
- Using it as an alternative to creating a view in the database

|OrderDetailID|	OrderID	|ProductID	|Quantity|
|-|-|-|-|
|1	|10248	|11	|12|
|2	|10248	|42	|10|
|3	|10248	|72	|5|
|4	|10249	|14	|9|
|5	|10249	|51	|40|

The objective is to return the average quantity ordered per ProductID:
````SQL
WITH cte_quantity
AS
(SELECT
    SUM(Quantity) as Total
FROM OrderDetails
GROUP BY ProductID)
 
SELECT
    AVG(Total) average_product_quantity
FROM cte_quantity;
````

|average_product_quantity|
|-|
|165.493|

If you didn't use `WITH`:

````SQL
SELECT
    AVG(Total) average_product_quantity
FROM
(SELECT
SUM(Quantity) as Total
FROM OrderDetails
GROUP BY ProductID)
````
The general sequence of steps to execute a WITH clause is:

1. Initiate the `WITH`
2. Specify the expression name for the to-be-defined query.
3. Optional: Specify column names separated by commas.
4. After assigning the name of the expression, enter the `AS` command. The expressions, in this case, are the named result sets that you will use later in the main query to refer to the CTE.
5. Write the query required to produce the desired temporary data set.
6. If working with more than one CTEs or WITH clauses, initiate each subsequent one separated by a comma and repeat steps 2-4. Such an arrangement is also called a nested WITH clause.
7. Reference the expressions defined above in a subsequent query using `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `MERGE`
````SQL
--CTE
WITH expression_name_1 (column_1, column_2,…,column_n)
AS
(CTE query definition 1),
expression_name_2 (column_1, column_2,…,column_n)
AS
(CTE query definition 2)
 
--Final query using CTE
SELECT expression_A, expression_B, ...
FROM expression_name_2
````
## SQL `OVER`
|sale_day   |sale_month |sale_time 	|branch 	|article 	|quantity 	|revenue|
|-|-|-|-|-|-|-|
|2021-08-11| 	AUG 	|11:00 |	New York 	|Rolex P1 	|   1 	     |   3000.00|
|2021-08-14| 	AUG 	|11:20 |	New York 	|Rolex P1 	|   2 	     |   6000.00|
|2021-08-17| 	AUG 	|10:00 |	Paris 	    |Omega 100 |	3 	     |   4000.00|
|2021-08-19| 	AUG 	|10:00 |	London 	    |Omega 100 |	1 	     |   1300.00|
|2021-07-17| 	JUL 	|09:30 |	Paris 	    |Cartier A1| 	1 	     |   2000.00|
|2021-07-11| 	JUL 	|10:10 |	New York 	|Cartier A1| 	1 	     |   2000.00|
|2021-07-10| 	JUL 	|11:40 |	London 	    |Omega 100 |	2 	     |   2600.00|
|2021-07-15| 	JUL 	|10:30 |	London 	    |Omega 100 |	3 	     |   4000.00|

The window frame is a set of rows that depends on the current row; thus, the set of rows could change for each row processed by the query. We define window frames using the `OVER` clause. The syntax is:
````SQL
OVER ([PARTITION BY columns] [ORDER BY columns])
````
The `PARTITION` BY subclause defines the criteria that the records must satisfy to be part of the window frame. In other words, `PARTITION` BY defines the groups into which the rows are divided; this will be clearer in our next example query. Finally, the ORDER BY clause defines the order of the records in the window frame.

Let’s see the SQL `OVER` clause in action. Here’s a simple query that returns the total quantity of units sold for each article. 


````SQL
SELECT sale_day, sale_time,
       branch, article, quantity, revenue,
       SUM(quantity) OVER (PARTITION BY article) AS total_units_sold
FROM   sales
````
This query will show all the records of the `sales` table with a new column displaying the total number of units sold for the relevant article. We can obtain the quantity of units sold using the `SUM` aggregation function, but then we couldn’t show the individual records.

In this query, the `OVER PARTITION BY` article subclause indicates that the window frame is determined by the values in the article column; all records with the same article value will be in one group. Below, we have the result of this query:

|sale_day   |sale_month |sale_time 	|branch 	|article 	|quantity 	|revenue| total units sold|
|-|-|-|-|-|-|-|-|
|2021-08-11| 	AUG 	|11:00 |	New York 	|Rolex P1 	|   1 	     |   3000.00|2|
|2021-08-14| 	AUG 	|11:20 |	New York 	|Rolex P1 	|   2 	     |   6000.00|2|
|2021-08-17| 	AUG 	|10:00 |	Paris 	    |Omega 100 |	3 	     |   4000.00|9|
|2021-08-19| 	AUG 	|10:00 |	London 	    |Omega 100 |	1 	     |   1300.00|9|
|2021-07-17| 	JUL 	|09:30 |	Paris 	    |Cartier A1| 	1 	     |   2000.00|9|
|2021-07-11| 	JUL 	|10:10 |	New York 	|Cartier A1| 	1 	     |   2000.00|9|
|2021-07-10| 	JUL 	|11:40 |	London 	    |Omega 100 |	2 	     |   2600.00|3|
|2021-07-15| 	JUL 	|10:30 |	London 	    |Omega 100 |	3 	     |   4000.00|3|


## View
1. An `UPDATE` statement against a View can only effect one target table at a time
2. Your `UPDATE` statement cannot update data in a derived column

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
   
