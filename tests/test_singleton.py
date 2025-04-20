from creational_patterns.singleton import DatabaseConnection

def test_singleton_instance():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db1 is db2
    assert db1.connect() == "Connected to DB"
    assert db2.connected is True



