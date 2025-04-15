import driver



with driver.session() as session:
    # Call transaction functions here
    
    def create_person(tx, name, age): # (1)
        result = tx.run("""
        CREATE (p:Person {name: $name, age: $age})
        RETURN p
        """, name=name, age=age) # (2)
        
        
    def transfer_funds(tx, from_account, to_account, amount):
    # Deduct from first account
        tx.run(
            "MATCH (a:Account {id: $from_}) SET a.balance = a.balance - $amount",
            from_=from_account, amount=amount
        )

    # Add to second account
        tx.run(
            "MATCH (a:Account {id: $to}) SET a.balance = a.balance + $amount",
            to=to_account, amount=amount
        )
        
        
with driver.session() as session:
    
    
    def get_answer(tx, answer):
        result = tx.run("RETURN $answer AS answer", answer=answer)

        return result.consume()

    # Call the transaction function
    summary = session.execute_read(get_answer, answer=42)

    # Output the summary
    print(
            "Results available after", summary.result_available_after,
            "ms and consumed after", summary.result_consumed_after, "ms"
        )