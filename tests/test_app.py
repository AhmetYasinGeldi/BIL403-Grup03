def test_ana_sayfa_aciliyor(client):
    response = client.get("/")
    assert response.status_code == 200


def test_test_ayarlari_yukleniyor(app):
    assert app.config["TESTING"] is True
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"
