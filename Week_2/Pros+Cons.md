# Week 2 Comparison: DuckDB vs Pandas vs Polars

## DuckDB

**Pros**

* Very fast on large CSV files
* Being able to use SQL is nice
* Does not require loading the full dataset into memory

**Cons**

* Must have SQL knowledge alongside Python so if someone doesn't know SQL this could be challenging
* Query logic is split between Python and SQL strings
* Less flexible for custom row-by-row logic

## Pandas

**Pros**

* Easy to debug and reason about step-by-step
* Very flexible for custom logic

**Cons**

* Cannot load a 22 GB CSV into memory directly
* Requires chunked reading and manual accumulation logic
* Slowest of the three approaches for this dataset by far
* Becomes really complicated to handle large scale data

## Polars

**Pros**

* Very fast, pretty comparable to DuckDB
* Lazy execution allows efficient filtering and aggregation
* Does not load the full CSV into memory

**Cons**

* Was harder to learn as this is the most different from things I know
* Debugging was not as easy as the others


## Favorite Approach

**DuckDB** was by far my favorite approach for this task because it was the easiest and also the best. Once I learned the little parts like integrating the SQL code into python with syntax from duckdb it was really nice being able to just write out the queries in SQL code. It also required the least amount of code to express the analysis and handled the 22 GB CSV really efficiently. Polars was a close second due to its performance and memory efficiency, but duckdb’s SQL interface made the overall solution simpler and more readable for this specific problem.
