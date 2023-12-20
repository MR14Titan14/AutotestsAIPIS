import requests
import pytest
payload1 = {
    "pagination": {
        "count": 3,
        "random": True
    },
    "filter": {
        "fcontact": {
            "hasContact": True
        },
        "fgit": {
            "hasGit": True
        }
    }
}

payload2 = {
    "pagination": {
        "count": 50,
        "random": True
    },
    "filter": {
        "fcontact": {
            "hasContact": True
        },
        "fgit": {
            "hasGit": True
        }
    }
}

payload3 = {
    "pagination": {
        "count": 500,
        "random": True
    },
    "filter": {
        "fcontact": {
            "hasContact": True
        },
        "fgit": {
            "hasGit": True
        }
    }
}

payload4 = {
    "pagination": {
        "count": 1,
        "number": 0,
        "random": False
    },
    "filter": {
        "fcontact": {
            "hasContact": True
        },
        "fgit": {
            "hasGit": True
        }
    }
}

payload6 = {
    "pagination": {
        "count": 3,
        "random": True
    },
    "filter": {
        "fcontact": {
            "hasContact": False
        },
        "fgit": {
            "hasGit": True
        }
    }
}

payload5 = {
    "pagination": {
        "count": 3,
        "random": True
    },
    "filter": {
        "fcontact": {
            "hasContact": True
        },
        "fgit": {
            "hasGit": False
        }
    }
}

payload7 = {
    "pagination": {
        "count": 3,
        "random": True
    },
    "filter": {
        "fcontact": {
            "hasContact": False
        },
        "fgit": {
            "hasGit": False
        }
    }
}

BASE_URL = 'http://192.168.0.16:8080/students/general/get-student-list'

def test_get_student_list_bestnormal():
    response = requests.post(f'{BASE_URL}', json=payload1)
    response_body=response.json()
    assert response.status_code==200
    for student in response_body["info"][:2]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"

def test_get_student_list_bestnormal_50students():
    response = requests.post(f'{BASE_URL}', json=payload2)
    response_body=response.json()
    assert response.status_code==200
    for student in response_body["info"][:49]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"

def test_get_student_list_bestnormal_500students():
    response = requests.post(f'{BASE_URL}', json=payload3)
    response_body=response.json()
    assert response.status_code==200
    for student in response_body["info"][:499]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"

def test_get_student_list_randomFalse_equals():
    response = requests.post(f'{BASE_URL}', json=payload4)
    response_body=response.json()
    response1 = requests.post(f'{BASE_URL}', json=payload4)
    response_body1=response.json()
    assert response.status_code==200
    assert response_body["info"][0]["fgit"]["hasGit"] == True, "Поле Гит пустое"
    assert response_body["info"][0]["fcontact"]["hasContact"] == True, "Поле контакты пустое"
    assert response1.status_code==200
    assert response_body1["info"][0]["fgit"]["hasGit"] == True, "Поле Гит пустое"
    assert response_body1["info"][0]["fcontact"]["hasContact"] == True, "Поле контакты пустое"
    assert response_body["info"][0]["id"] == response_body1["info"][0]["id"], "Данные не совпадают"

def test_get_student_list_gitFalse():
    response = requests.post(f'{BASE_URL}', json=payload5)
    response_body=response.json()
    assert response.status_code==200
    for student in response_body["info"][:2]:
        assert student["fgit"]["hasGit"] == False, "Поле Гит не пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"

def test_get_student_list_contactFalse():
    response = requests.post(f'{BASE_URL}', json=payload6)
    response_body=response.json()
    assert response.status_code==200
    for student in response_body["info"][:2]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты не пустое"

def test_get_student_list_gitcontactFalse():
    response = requests.post(f'{BASE_URL}', json=payload7)
    response_body=response.json()
    assert response.status_code==200
    for student in response_body["info"][:2]:
        assert student["fgit"]["hasGit"] == False, "Поле Гит не пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты не пустое"

def test_get_student_list():
    response = requests.post(f'{BASE_URL}')
    response_body=response.json()
    assert response.status_code==200
