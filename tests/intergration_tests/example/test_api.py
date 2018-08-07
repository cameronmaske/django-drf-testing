from django.urls import reverse
import pytest 
from example.models import Example


@pytest.mark.django_db
def test_create(client):
    response = client.post("/api/example/", data={'number': 2, 'text': "Hello World"}, format='json')
    assert response.status_code == 201
    example = Example.objects.get()
    assert example.number == 2 
    assert example.text == "Hello World"
    assert response.json() == {
        'id': example.id,
        'number': 2,
        'text': "Hello World"
    }

# Simulate many tests

@pytest.mark.django_db
def test_1(client):
    test_create(client)

@pytest.mark.django_db
def test_2(client):
    test_create(client)

@pytest.mark.django_db
def test_3(client):
    test_create(client)

@pytest.mark.django_db
def test_4(client):
    test_create(client)

@pytest.mark.django_db
def test_5(client):
    test_create(client)

@pytest.mark.django_db
def test_6(client):
    test_create(client)

@pytest.mark.django_db
def test_7(client):
    test_create(client)

@pytest.mark.django_db
def test_8(client):
    test_create(client)

@pytest.mark.django_db
def test_9(client):
    test_create(client)

@pytest.mark.django_db
def test_10(client):
    test_create(client)

@pytest.mark.django_db
def test_11(client):
    test_create(client)

@pytest.mark.django_db
def test_12(client):
    test_create(client)

@pytest.mark.django_db
def test_13(client):
    test_create(client)

@pytest.mark.django_db
def test_14(client):
    test_create(client)

@pytest.mark.django_db
def test_15(client):
    test_create(client)

@pytest.mark.django_db
def test_16(client):
    test_create(client)

@pytest.mark.django_db
def test_17(client):
    test_create(client)

@pytest.mark.django_db
def test_18(client):
    test_create(client)

@pytest.mark.django_db
def test_19(client):
    test_create(client)

@pytest.mark.django_db
def test_20(client):
    test_create(client)

@pytest.mark.django_db
def test_21(client):
    test_create(client)

@pytest.mark.django_db
def test_22(client):
    test_create(client)

@pytest.mark.django_db
def test_23(client):
    test_create(client)

@pytest.mark.django_db
def test_24(client):
    test_create(client)

@pytest.mark.django_db
def test_25(client):
    test_create(client)

@pytest.mark.django_db
def test_26(client):
    test_create(client)

@pytest.mark.django_db
def test_27(client):
    test_create(client)

@pytest.mark.django_db
def test_28(client):
    test_create(client)

@pytest.mark.django_db
def test_29(client):
    test_create(client)

@pytest.mark.django_db
def test_30(client):
    test_create(client)

@pytest.mark.django_db
def test_31(client):
    test_create(client)

@pytest.mark.django_db
def test_32(client):
    test_create(client)

@pytest.mark.django_db
def test_33(client):
    test_create(client)

@pytest.mark.django_db
def test_34(client):
    test_create(client)

@pytest.mark.django_db
def test_35(client):
    test_create(client)

@pytest.mark.django_db
def test_36(client):
    test_create(client)

@pytest.mark.django_db
def test_37(client):
    test_create(client)

@pytest.mark.django_db
def test_38(client):
    test_create(client)

@pytest.mark.django_db
def test_39(client):
    test_create(client)

@pytest.mark.django_db
def test_40(client):
    test_create(client)

@pytest.mark.django_db
def test_41(client):
    test_create(client)

@pytest.mark.django_db
def test_42(client):
    test_create(client)

@pytest.mark.django_db
def test_43(client):
    test_create(client)

@pytest.mark.django_db
def test_44(client):
    test_create(client)

@pytest.mark.django_db
def test_45(client):
    test_create(client)

@pytest.mark.django_db
def test_46(client):
    test_create(client)

@pytest.mark.django_db
def test_47(client):
    test_create(client)

@pytest.mark.django_db
def test_48(client):
    test_create(client)

@pytest.mark.django_db
def test_49(client):
    test_create(client)

@pytest.mark.django_db
def test_50(client):
    test_create(client)

@pytest.mark.django_db
def test_51(client):
    test_create(client)

@pytest.mark.django_db
def test_52(client):
    test_create(client)

@pytest.mark.django_db
def test_53(client):
    test_create(client)

@pytest.mark.django_db
def test_54(client):
    test_create(client)

@pytest.mark.django_db
def test_55(client):
    test_create(client)

@pytest.mark.django_db
def test_56(client):
    test_create(client)

@pytest.mark.django_db
def test_57(client):
    test_create(client)

@pytest.mark.django_db
def test_58(client):
    test_create(client)

@pytest.mark.django_db
def test_59(client):
    test_create(client)

@pytest.mark.django_db
def test_60(client):
    test_create(client)

@pytest.mark.django_db
def test_61(client):
    test_create(client)

@pytest.mark.django_db
def test_62(client):
    test_create(client)

@pytest.mark.django_db
def test_63(client):
    test_create(client)

@pytest.mark.django_db
def test_64(client):
    test_create(client)

@pytest.mark.django_db
def test_65(client):
    test_create(client)

@pytest.mark.django_db
def test_66(client):
    test_create(client)

@pytest.mark.django_db
def test_67(client):
    test_create(client)

@pytest.mark.django_db
def test_68(client):
    test_create(client)

@pytest.mark.django_db
def test_69(client):
    test_create(client)

@pytest.mark.django_db
def test_70(client):
    test_create(client)
