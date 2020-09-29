from v5.upg39 import max, total, total1
def test_maximala_a():
    a = 10
    b = 5
    c = 6
    assert max(a,b,c) == a
def test_maximala_b():
    a = 10
    b = 50
    c = 6
    assert max(a,b,c) == b
def test_maximala_c():
    a = 10
    b = 5
    c = 60
    assert max(a,b,c) == c

def test_total_v1():
    totala = [1,2,3,4,5]
    assert total(totala) == sum(totala)
def test_total_v2():
    totala = [1,2,3,4,5]
    assert total(totala) != 1245
def test_total_v3():
    totala = [12,1231,123,4124]
    assert total(totala) >= sum(totala)

def test_multi_total_v1():
    tot = [1,2,3,4,5]
    assert total1(tot) == 120

def test_multi_total_v2():
    tot = [1,2,3,4,5]
    assert total1(tot) != 1200

def test_multi_total_v3():
    tot = [1,2,3,4,5]
    assert total1(tot) >= 120