from neo4j.spatial import CartesianPoint
import driver

two_d = CartesianPoint((x, y))
three_d = CartesianPoint((x, y, z))

records, summary, keys = driver.execute_query("""
RETURN point({x: 1.23, y: 4.56, z: 7.89}) AS threeD
""")

point = records[0]["threeD"]

# <1> Accessing attributes
print(point.x, point.y, point.z, point.srid) # 1.23, 4.56, 7.89, 9157

# <2> Destructuring
x, y, z = point



from neo4j.spatial import WGS84Point

ldn = WGS84Point((-0.118092, 51.509865))
print(ldn.longitude, ldn.latitude, ldn.srid) # -0.118092, 51.509865, 4326

shard = WGS84Point((-0.086500, 51.504501, 310))
print(shard.longitude, shard.latitude, shard.height, shard.srid) # -0.0865, 51.504501, 310, 4979

# Using destructuring
longitude, latitude, height = shard


records, summary, keys = driver.execute_query("""
RETURN point({
    latitude: 51.5,
    longitude: -0.118,
    height: 100
}) AS point
""")

point = records[0]["point"]
longitude, latitude, height = point


# Create two points
point1 = CartesianPoint((1, 1))
point2 = CartesianPoint((10, 10))

# Query the distance using Cypher
records, summary, keys = driver.execute_query("""
RETURN point.distance($p1, $p2) AS distance
""", p1=point1, p2=point2)

# Print the distance from the result
distance = records[0]["distance"]
print(distance)  # 12.727922061357855