from neo4j import GraphDatabase

driver = GraphDatabase.driver(
  "neo4j://localhost:7687",       # (1)
  auth=("neo4j", "neo4jneo4j") # (2)
)

driver.verify_connectivity

cypher = """
MATCH (p:Person {name: $name})-[r:ACTED_IN]->(m:Movie)
RETURN m.title AS title, r.role AS role
"""
name = "Tom Hanks"

records, summary, keys = driver.execute_query( # (1)
    cypher,    # (2)
    name=name  # (3)
)


print(keys)  # ['title', 'role']
print(summary)  # A summary of the query execution

# RETURN m.title AS title, r.role AS role

for record in records:
    print(record["title"])  # Toy Story
    print(record["role"])  # "Woody"
    
    
    result = driver.execute_query(
    cypher,
    name=name,
    result_transformer_= lambda result: [
        f"Tom Hanks played {record['role']} in {record['title']}"
        for record in result
    ]
)

print(result)  # ['Tom Hanks played Woody in Toy Story', ...]