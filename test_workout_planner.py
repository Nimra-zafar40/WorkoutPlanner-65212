from water_reminder import calculate_water_intake, suggest_reminder_interval, recommend_water_temperature

def test_calculate_water_intake():
    assert calculate_water_intake(60) == 1.98
    assert calculate_water_intake(75) == 2.48

def test_suggest_reminder_interval():
    assert suggest_reminder_interval(10) == 3
    assert suggest_reminder_interval(30) == 2
    assert suggest_reminder_interval(65) == 1.5

def test_recommend_water_temperature():
    assert recommend_water_temperature(10) == "Cool"
    assert recommend_water_temperature(40) == "Room Temperature"
    assert recommend_water_temperature(70) == "Lukewarm"

